# -*- coding: utf8 -*-
# Copyright (c) 2014 by Ecreall under licence AGPL terms
# available on http://www.gnu.org/licenses/agpl.html

# licence: AGPL
# author: Amen Souissi

import datetime
import pytz
import deform
import colander
from zope.interface import implementer
from persistent.list import PersistentList

from substanced.content import content
from substanced.schema import NameSchemaNode
from substanced.util import renamer

from dace.util import getSite, get_obj
from dace.descriptors import SharedUniqueProperty
from pontus.core import VisualisableElementSchema
from pontus.widget import RichTextWidget, CheckboxChoiceWidget, Select2Widget

from .interface import IEvent
from novaideo import _, log, EUROPEAN_LOCALES, EUROPEAN_ZONES
from novaideo.core import (
    SearchableEntity,
    SearchableEntitySchema)
from novaideo.utilities.util import truncate_text


KINDS = {
    'physical': _('Physical'),
    'virtual': _('Virtual')
}


@colander.deferred
def locale_widget(node, kw):
    request = node.bindings['request']
    localizer = request.localizer
    sorted_locales = sorted(
        [(key, localizer.translate(title))
         for key, title in EUROPEAN_LOCALES.items()])
    return Select2Widget(values=sorted_locales)


@colander.deferred
def tzname_widget(node, kw):
    zones = sorted( [(title, title) for title in EUROPEAN_ZONES])
    return Select2Widget(values=zones)


@colander.deferred
def kind_choices(node, kw):
    request = node.bindings['request']
    localizer = request.localizer
    values = [(key, localizer.translate(title))
              for key, title in KINDS.items()]
    return deform.widget.RadioChoiceWidget(values=sorted(values))


def context_is_a_event(context, request):
    return request.registry.content.istype(context, 'event')


class EventSchema(VisualisableElementSchema, SearchableEntitySchema):
    """Schema for event"""

    name = NameSchemaNode(
        editing=context_is_a_event,
        )

    text = colander.SchemaNode(
        colander.String(),
        widget=deform.widget.TextAreaWidget(),
        title=_("Details"),
        description=_('The details of the event. For example an address or a link ...'),
        )

    date = colander.SchemaNode(
        colander.DateTime(),
        title=_('Date'),
        description=_('The date of the event.'),
    )

    kind = colander.SchemaNode(
        colander.String(),
        widget=kind_choices,
        title=_('Mode'),
        description=_('The event mode.'),
        default='physical',
    )

    tzname = colander.SchemaNode(
        colander.String(),
        title=_('Timezone'),
        description=_('You can specify the timezone of the date of the event.'),
        widget=tzname_widget,
        validator=colander.OneOf(EUROPEAN_ZONES)
    )

    locale = colander.SchemaNode(
        colander.String(),
        title=_('Language'),
        description=_('You can specify the language of the event.'),
        widget=locale_widget,
        validator=colander.OneOf(EUROPEAN_LOCALES),
        default='en'
    )


@content(
    'event',
    icon='glyphicon glyphicon-calendar',
    )
@implementer(IEvent)
class Event(SearchableEntity):
    """Event class"""

    type_title = _('Discussion event')
    icon = 'glyphicon glyphicon-calendar'
    templates = {'default': 'novaideo:views/templates/event_result.pt',
                 'bloc': 'novaideo:views/templates/event_bloc.pt',
                 'small': 'novaideo:views/templates/small_event_result.pt',
                 'popover': 'novaideo:views/templates/event_popover.pt'}
    template = 'novaideo:views/templates/event_list_element.pt'
    name = renamer()
    author = SharedUniqueProperty('author', 'events')
    subject = SharedUniqueProperty('subject', 'events')

    def __init__(self, **kwargs):
        super(Event, self).__init__(**kwargs)
        self.set_data(kwargs)

    @property
    def relevant_data(self):
        subject_relevant_data = getattr(self.subject, 'relevant_data', [])
        subject_relevant_data.extend([getattr(self, 'title', '')])
        return subject_relevant_data

    def init_published_at(self):
        setattr(self, 'published_at', datetime.datetime.now(tz=pytz.UTC))

    def presentation_text(self, nb_characters=400):
        return truncate_text(getattr(self, 'text', ""), nb_characters)

    def update(self):
        if 'expired' not in self.state and self.is_expired:
            self.state = PersistentList(['expired'])
            self.reindex()

    @property
    def is_expired(self):
        if 'expired' in self.state: return True
        try:
            now = datetime.datetime.now(tz=pytz.timezone(self.tzname))
            return self.date < now
        except Exception as e:
            return True


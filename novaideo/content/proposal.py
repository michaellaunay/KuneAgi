# Copyright (c) 2014 by Ecreall under licence AGPL terms 
# avalaible on http://www.gnu.org/licenses/agpl.html 

# licence: AGPL
# author: Amen Souissi

import colander
from collections import OrderedDict
from webob.multidict import MultiDict
from persistent.list import PersistentList
from zope.interface import implementer

from substanced.content import content
from substanced.schema import NameSchemaNode
from substanced.util import renamer

from dace.util import get_obj
from dace.descriptors import (
    CompositeMultipleProperty,
    SharedUniqueProperty)
from pontus.widget import RichTextWidget, AjaxSelect2Widget, Length
from pontus.core import VisualisableElementSchema

from .interface import IProposal
from novaideo.content.correlation import CorrelationType
from novaideo.core import Commentable
from novaideo import _, log
from novaideo.views.widget import LimitedTextAreaWidget
from novaideo.core import (
    SearchableEntity,
    SearchableEntitySchema,
    CorrelableEntity,
    DuplicableEntity,
    VersionableEntity,
    PresentableEntity)
from novaideo.content.processes.proposal_management import WORK_MODES


OPINIONS = OrderedDict([
    ('favorable', _('Favorable')),
    ('to_study', _('To study')),
    ('unfavorable', _('Unfavorable'))
])


@colander.deferred
def ideas_choice(node, kw):
    context = node.bindings['context']
    request = node.bindings['request']
    values = []
    ajax_url = request.resource_url(context,
                                    '@@novaideoapi',
                                    query={'op': 'find_ideas'})

    def title_getter(oid):
        try:
            obj = get_obj(int(oid), None)
            if obj:
                return obj.title
            else:
                return oid
        except Exception as e:
            log.warning(e)
            return oid

    return AjaxSelect2Widget(
        values=values,
        ajax_url=ajax_url,
        multiple=True,
        title_getter=title_getter,
        )


def context_is_a_proposal(context, request):
    return request.registry.content.istype(context, 'proposal')


class ProposalSchema(VisualisableElementSchema, SearchableEntitySchema):
    """Schema for Proposal"""

    name = NameSchemaNode(
        editing=context_is_a_proposal,
        )

    description = colander.SchemaNode(
        colander.String(),
        validator=colander.Length(max=300),
        widget=LimitedTextAreaWidget(rows=5,
                                     cols=30,
                                     limit=300),
        title=_("Abstract")
        )

    text = colander.SchemaNode(
        colander.String(),
        widget=RichTextWidget(),
        title=_("Text")
        )

    related_ideas  = colander.SchemaNode(
        colander.Set(),
        widget=ideas_choice,
        title=_('Related ideas'),
        validator=Length(_, min=1),
        default=[],
        )


@content(
    'proposal',
    icon='icon novaideo-icon icon-proposal',
    )
@implementer(IProposal)
class Proposal(Commentable,
               VersionableEntity,
               SearchableEntity,
               DuplicableEntity,
               CorrelableEntity,
               PresentableEntity):
    """Proposal class"""

    type_title = _('Proposal')
    icon = 'icon novaideo-icon icon-proposal'
    templates = {'default': 'novaideo:views/templates/proposal_result.pt'}
    template = 'novaideo:views/templates/proposal_list_element.pt'
    name = renamer()
    author = SharedUniqueProperty('author')
    working_group = SharedUniqueProperty('working_group', 'proposal')
    tokens_opposition = CompositeMultipleProperty('tokens_opposition')
    tokens_support = CompositeMultipleProperty('tokens_support')
    amendments = CompositeMultipleProperty('amendments', 'proposal')
    corrections = CompositeMultipleProperty('corrections', 'proposal')

    def __init__(self, **kwargs):
        super(Proposal, self).__init__(**kwargs)
        self.set_data(kwargs)
        # [(user_oid, date, support_type), ...], support_type = {1:support, 0:oppose, -1:withdraw}
        self._support_history = PersistentList()
        self._amendments_counter = 1

    @property
    def related_ideas(self):
        lists_targets = [(c.targets, c) for c in self.source_correlations
                         if c.type == CorrelationType.solid and
                         'related_ideas' in c.tags]
        return MultiDict([(target, c) for targets, c in lists_targets
                          for target in targets])

    @property
    def tokens(self):
        result = list(self.tokens_opposition)
        result.extend(list(self.tokens_support))
        return result

    @property
    def opinion_value(self):
        return OPINIONS.get(getattr(self, 'opinion', None), None)

    @property
    def is_published(self):
        return 'draft' not in self.state

    @property
    def work_mode(self):
        mode_id = getattr(self, 'work_mode_id', None)
        if mode_id:
            return WORK_MODES.get(mode_id, None)

        root = self.__parent__
        if hasattr(root, 'get_work_modes') and len(root.get_work_modes()) == 1:
            return root.get_default_work_mode()

        return None

    def get_more_contents_criteria(self):
        "return specific query, filter values"
        return None, {
            'metadata_filter': {
                'content_types': ['proposal', 'idea'],
                'keywords': list(self.keywords)
            }
        }

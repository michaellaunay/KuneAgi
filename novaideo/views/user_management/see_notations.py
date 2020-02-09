# Copyright (c) 2014 by Ecreall under licence AGPL terms
# avalaible on http://www.gnu.org/licenses/agpl.html

# licence: AGPL
# author: Amen Souissi

from pyramid.view import view_config


from dace.util import get_obj, getSite
from dace.processinstance.core import DEFAULTMAPPING_ACTIONS_VIEWS
from pontus.view import BasicView

from novaideo.content.processes.user_management.behaviors import (
    SeeNotations)
from novaideo.content.person import (
    Person)
from novaideo.utilities.util import to_localized_time
from novaideo import _


CONTENTS_MESSAGES = {
    '0': _(u"""No mark found"""),
    '1': _(u"""One mark found"""),
    '*': _(u"""${nember} marks found""")
}


@view_config(
    name='seenotations',
    context=Person,
    renderer='pontus:templates/views_templates/grid.pt',
)
class SeeNotationsView(BasicView):
    title = _('Marks')
    name = 'seenotations'
    behaviors = [SeeNotations]
    template = 'novaideo:views/user_management/templates/notations.pt'
    viewid = 'seenotations'
    wrapper_template = 'novaideo:views/templates/simple_wrapper.pt'
    css_class = 'simple-bloc'
    container_css_class = 'home'

    def update(self):
        self.execute(None)
        user = self.context
        root = getSite()
        notes = [
            {
                'date': to_localized_time(
                    date, self.request, translate=True),
                'user': get_obj(value[0]),
                'content': get_obj(value[1]),
                'note': value[2],
            }
            for date, value in user._notes.items()
        ]
        len_result = len(notes)
        index = str(len_result)
        if len_result > 1:
            index = '*'

        self.title = _(CONTENTS_MESSAGES[index],
                       mapping={'nember': len_result})
        values = {
            'notes': notes,
            'member': self.context,
            'time_constant': getattr(root, 'time_constant', 6),
            'length': len_result,
            'score': getattr(user, 'confidence_index', 0)
        }
        result = {}
        body = self.content(args=values, template=self.template)['body']
        item = self.adapt_item(body, self.viewid)
        result['coordinates'] = {self.coordinates: [item]}
        return result


DEFAULTMAPPING_ACTIONS_VIEWS.update({SeeNotations: SeeNotationsView})

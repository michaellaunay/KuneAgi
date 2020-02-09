# Copyright (c) 2014 by Ecreall under licence AGPL terms
# available on http://www.gnu.org/licenses/agpl.html

# licence: AGPL
# author: Amen Souissi

import deform
from pyramid.view import view_config

from dace.processinstance.core import DEFAULTMAPPING_ACTIONS_VIEWS
from pontus.default_behavior import Cancel
from pontus.form import FormView
from pontus.view import BasicView
from pontus.view_operation import MultipleView

from novaideo.content.processes.user_management.behaviors import (
    Quit)
from novaideo.content.person import Person
from novaideo.content.novaideo_application import NovaIdeoApplication
from novaideo import _


class QuitViewStudyReport(BasicView):
    title = 'Alert: quit the platform'
    name = 'alertforquit'
    template = 'novaideo:views/user_management/templates/alert_quit_platform.pt'

    def update(self):
        result = {}
        values = {'context': self.context}
        body = self.content(args=values, template=self.template)['body']
        item = self.adapt_item(body, self.viewid)
        result['coordinates'] = {self.coordinates: [item]}
        return result


class QuitView(FormView):
    title = _('Quit the platform')
    name = 'quitform'
    formid = 'formquit'
    behaviors = [Quit, Cancel]
    validate_behaviors = False

    def before_update(self):
        self.action = self.request.resource_url(
            self.context, 'novaideoapi',
            query={'op': 'update_action_view',
                   'node_id': Quit.node_definition.id})
        self.schema.widget = deform.widget.FormWidget(
            css_class='deform novaideo-ajax-form')


@view_config(
    name='quit',
    context=Person,
    renderer='pontus:templates/views_templates/grid.pt',
)
class QuitViewMultipleView(MultipleView):
    title = _('Quit the platform')
    name = 'quit'
    viewid = 'quit'
    template = 'pontus:templates/views_templates/simple_multipleview.pt'
    views = (QuitViewStudyReport, QuitView)
    validators = [Quit.get_validator()]


@view_config(
    name='resignationsubmitted',
    context=NovaIdeoApplication,
    renderer='pontus:templates/views_templates/grid.pt',
)
class ResignationSubmittedView(BasicView):
    template = 'novaideo:views/user_management/templates/resignationsubmitted.pt'
    title = _('Please confirm your resignation')
    name = 'resignationsubmitted'
    viewid = 'resignation'
    css_class = 'panel-transparent'

    def update(self):
        result = {}
        body = self.content(args={}, template=self.template)['body']
        item = self.adapt_item(body, self.viewid)
        result['coordinates'] = {self.coordinates: [item]}
        return result


DEFAULTMAPPING_ACTIONS_VIEWS.update(
    {Quit: QuitViewMultipleView})

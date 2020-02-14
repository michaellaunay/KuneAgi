# Copyright (c) 2014 by Ecreall under licence AGPL terms
# available on http://www.gnu.org/licenses/agpl.html

# licence: AGPL
# author: Amen Souissi

from pyramid.view import view_config

from dace.processinstance.core import DEFAULTMAPPING_ACTIONS_VIEWS
from pontus.view import BasicView
from pontus.view_operation import MultipleView
from pontus.form import FormView
from pontus.schema import select

from novaideo.content.processes.user_management.behaviors import (
    ConfirmRegistration)
from novaideo.content.person import Preregistration, PersonSchema
from novaideo import _
from .reset_password import Cancel


class ConfirmRegistrationViewStudyReport(BasicView):
    title = 'Confirm: registration'
    name = 'alertconfirmregistration'
    template = 'novaideo:views/user_management/templates/alert_confirm_registration.pt'

    def update(self):
        result = {}
        values = {'context': self.context}
        body = self.content(args=values, template=self.template)['body']
        item = self.adapt_item(body, self.viewid)
        result['coordinates'] = {self.coordinates: [item]}
        return result


class ConfirmRegistrationViewFrom(FormView):
    title = _('Registration confirmation')
    behaviors = [ConfirmRegistration, Cancel]
    formid = 'formregistration'
    name = ''
    css_class = 'panel-transparent'


@view_config(
    name='',
    context=Preregistration,
    renderer='pontus:templates/views_templates/grid.pt',
)
class ConfirmRegistrationView(MultipleView):
    title = _('Registration confirmation')
    name = ''
    viewid = 'disactivate'
    template = 'daceui:templates/mergedmultipleview.pt'
    views = (ConfirmRegistrationViewStudyReport, ConfirmRegistrationViewFrom)
    validators = [ConfirmRegistration.get_validator()]
    css_class = 'panel-transparent'


DEFAULTMAPPING_ACTIONS_VIEWS.update(
    {ConfirmRegistration: ConfirmRegistrationView})

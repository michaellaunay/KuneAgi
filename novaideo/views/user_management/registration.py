# Copyright (c) 2014 by Ecreall under licence AGPL terms
# avalaible on http://www.gnu.org/licenses/agpl.html

# licence: AGPL
# author: Amen Souissi

import colander
from zope.interface import invariant
from pyramid.view import view_config

from dace.processinstance.core import DEFAULTMAPPING_ACTIONS_VIEWS
from pontus.default_behavior import Cancel
from pontus.form import FormView
from pontus.view import BasicView
from pontus.schema import select
from pontus.view_operation import MultipleView

from novaideo.views.widget import ReCAPTCHAWidget
from novaideo.content.processes.user_management.behaviors import (
    Registration)
from novaideo.content.person import PersonSchema, Preregistration
from novaideo.content.novaideo_application import (
    NovaIdeoApplication)
from novaideo import _


class RegistrationSchema(PersonSchema):

    captcha = colander.SchemaNode(
        colander.String(),
        widget=ReCAPTCHAWidget(),
        label=_('I have read and accept the terms and conditions.'),
        title='',
        missing=''
    )

    @invariant
    def captcha_invariant(self, appstruct):
        captcha = appstruct.get('captcha', '')
        if not captcha:
            raise colander.Invalid(
                self, _('Invalid captcha'))


class RegistrationViewStudyReport(BasicView):
    title = 'Alert: registration'
    name = 'alertforregistration'
    template = 'novaideo:views/user_management/templates/alert_registration.pt'

    def update(self):
        result = {}
        values = {'context': self.context}
        body = self.content(args=values, template=self.template)['body']
        item = self.adapt_item(body, self.viewid)
        result['coordinates'] = {self.coordinates: [item]}
        return result


class RegistrationForm(FormView):
    title = _('Your registration')
    schema = select(RegistrationSchema(
                        factory=Preregistration,
                        editable=True,            
                        omit=['captcha']),
                    ['user_title',
                     'first_name',
                     'last_name',
                     'birth_date',
                     'birthplace',
                     'email',
                     'Keep_me_anonymous',
                     'pseudonym',
                     'accept_conditions',
                     'captcha'])
    behaviors = [Registration, Cancel]
    formid = 'formregistration'
    name = 'formregistration'
    requirements = {'css_links': [],
                    'js_links': ['novaideo:static/js/user_management.js']}


@view_config(
    name='registration',
    context=NovaIdeoApplication,
    renderer='pontus:templates/views_templates/grid.pt',
    )
class RegistrationView(MultipleView):
    title = _('Your registration')
    name = 'registration'
    viewid = 'registration'
    template = 'daceui:templates/mergedmultipleview.pt'
    views = (RegistrationViewStudyReport, RegistrationForm)
    validators = [Registration.get_validator()]


@view_config(
    name='registrationsubmitted',
    context=NovaIdeoApplication,
    renderer='pontus:templates/views_templates/grid.pt',
    )
class RegistrationSubmittedView(BasicView):
    template = 'novaideo:views/user_management/templates/registrationsubmitted.pt'
    title = _('Please confirm your registration')
    name = 'registrationsubmitted'
    viewid = 'deactivateview'

    def before_update(self):
        moderate_registration = getattr(
            self.context, 'moderate_registration', False)
        if moderate_registration:
            self.title = _('Your registration is submitted to moderation')

    def update(self):
        result = {}
        body = self.content(args={}, template=self.template)['body']
        item = self.adapt_item(body, self.viewid)
        result['coordinates'] = {self.coordinates: [item]}
        return result


DEFAULTMAPPING_ACTIONS_VIEWS.update({Registration: RegistrationView})

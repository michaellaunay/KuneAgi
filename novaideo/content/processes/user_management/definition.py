# Copyright (c) 2014 by Ecreall under licence AGPL terms
# available on http://www.gnu.org/licenses/agpl.html

# licence: AGPL
# author: Amen Souissi

from dace.processdefinition.processdef import ProcessDefinition
from dace.processdefinition.activitydef import ActivityDefinition
from dace.processdefinition.gatewaydef import (
    ExclusiveGatewayDefinition,
    ParallelGatewayDefinition)
from dace.processdefinition.transitiondef import TransitionDefinition
from dace.processdefinition.eventdef import (
    StartEventDefinition,
    EndEventDefinition)
from dace.objectofcollaboration.services.processdef_container import (
    process_definition)
from pontus.core import VisualisableElement

from .behaviors import (
    Registration,
    LogIn,
    LogOut,
    Edit,
    Discuss,
    GeneralDiscuss,
    Activate,
    Deactivate,
    GetAPIToken,
    SeePerson,
    AssignRoles,
    ConfirmRegistration,
    Remind,
    SeeRegistration,
    SeeRegistrations,
    RemoveRegistration,
    ModerationVote,
    SeeNotations,
    ExtractAlerts)
from novaideo import _
from novaideo.content.person import Preregistration
from novaideo.content.processes.content_ballot_management import (
    BALLOT_DATA)
from novaideo.content.processes.content_ballot_management.definition import (
    ContentBallot)


@process_definition(name='usermanagement', id='usermanagement')
class UserManagement(ProcessDefinition, VisualisableElement):
    isUnique = True

    def __init__(self, **kwargs):
        super(UserManagement, self).__init__(**kwargs)
        self.title = _('User management')
        self.description = _('User management')

    def _init_definition(self):
        self.defineNodes(
                start = StartEventDefinition(),
                pg = ParallelGatewayDefinition(),
                login = ActivityDefinition(contexts=[LogIn],
                                       description=_("Log in"),
                                       title=_("Log in"),
                                       groups=[_("Access")]),
                logout = ActivityDefinition(contexts=[LogOut],
                                       description=_("Log out"),
                                       title=_("Log out"),
                                       groups=[_("Access")]),
                edit = ActivityDefinition(contexts=[Edit],
                                       description=_("Edit"),
                                       title=_("Edit"),
                                       groups=[]),
                deactivate = ActivityDefinition(contexts=[Deactivate],
                                       description=_("Disactivate the profile"),
                                       title=_("Disactivate the profile"),
                                       groups=[]),
                activate = ActivityDefinition(contexts=[Activate],
                                       description=_("Activate the profile"),
                                       title=_("Activate the profile"),
                                       groups=[]),
                assign_roles = ActivityDefinition(contexts=[AssignRoles],
                                       description=_("Assign roles to user"),
                                       title=_("Assign roles"),
                                       groups=[]),
                see = ActivityDefinition(contexts=[SeePerson],
                                       description=_("Details"),
                                       title=_("Details"),
                                       groups=[]),
                see_notations = ActivityDefinition(contexts=[SeeNotations],
                                       description=_("The marks"),
                                       title=_("The marks"),
                                       groups=[]),
                discuss = ActivityDefinition(contexts=[Discuss],
                                       description=_("Discuss"),
                                       title=_("Discuss"),
                                       groups=[]),
                get_api_token = ActivityDefinition(contexts=[GetAPIToken],
                                       description=_("Get API token"),
                                       title=_("Get API token"),
                                       groups=[]),
                general_discuss = ActivityDefinition(contexts=[GeneralDiscuss],
                                       description=_("Discuss"),
                                       title=_("Discuss"),
                                       groups=[]),
                extract_alerts = ActivityDefinition(contexts=[ExtractAlerts],
                                       description=_("Extract the user's alerts"),
                                       title=_("Extract alerts"),
                                       groups=[]),
                eg = ExclusiveGatewayDefinition(),
                end = EndEventDefinition(),
        )
        self.defineTransitions(
                TransitionDefinition('start', 'pg'),
                TransitionDefinition('pg', 'login'),
                TransitionDefinition('pg', 'logout'),
                TransitionDefinition('login', 'eg'),
                TransitionDefinition('pg', 'extract_alerts'),
                TransitionDefinition('extract_alerts', 'eg'),
                TransitionDefinition('logout', 'eg'),
                TransitionDefinition('pg', 'discuss'),
                TransitionDefinition('discuss', 'eg'),
                TransitionDefinition('pg', 'general_discuss'),
                TransitionDefinition('general_discuss', 'eg'),
                TransitionDefinition('pg', 'edit'),
                TransitionDefinition('edit', 'eg'),
                TransitionDefinition('pg', 'get_api_token'),
                TransitionDefinition('get_api_token', 'eg'),
                TransitionDefinition('pg', 'deactivate'),
                TransitionDefinition('deactivate', 'eg'),
                TransitionDefinition('pg', 'activate'),
                TransitionDefinition('activate', 'eg'),
                TransitionDefinition('pg', 'assign_roles'),
                TransitionDefinition('assign_roles', 'eg'),
                TransitionDefinition('pg', 'see_notations'),
                TransitionDefinition('see_notations', 'eg'),
                TransitionDefinition('pg', 'see'),
                TransitionDefinition('see', 'eg'),
                TransitionDefinition('eg', 'end'),
        )


@process_definition(name='registrationmanagement', id='registrationmanagement')
class RegistrationManagement(ProcessDefinition, VisualisableElement):
    isUnique = True

    def __init__(self, **kwargs):
        super(RegistrationManagement, self).__init__(**kwargs)
        self.title = _('Registration management')
        self.description = _('Registration management')

    def _init_definition(self):
        self.defineNodes(
                start = StartEventDefinition(),
                pg = ParallelGatewayDefinition(),
                registration = ActivityDefinition(contexts=[Registration],
                                       description=_("User registration"),
                                       title=_("User registration"),
                                       groups=[]),
                confirmregistration = ActivityDefinition(contexts=[ConfirmRegistration],
                                       description=_("Confirm registration"),
                                       title=_("Confirm registration"),
                                       groups=[]),
                remind = ActivityDefinition(contexts=[Remind],
                                       description=_("Remind user"),
                                       title=_("Remind"),
                                       groups=[]),
                see_registration = ActivityDefinition(contexts=[SeeRegistration],
                                       description=_("Details"),
                                       title=_("Details"),
                                       groups=[]),
                see_registrations = ActivityDefinition(contexts=[SeeRegistrations],
                                       description=_("See registrations"),
                                       title=_("Registrations"),
                                       groups=[_('See')]),
                remove = ActivityDefinition(contexts=[RemoveRegistration],
                                       description=_("Remove the registration"),
                                       title=_("Remove"),
                                       groups=[]),
                eg = ExclusiveGatewayDefinition(),
                end = EndEventDefinition(),
        )
        self.defineTransitions(
                TransitionDefinition('start', 'pg'),
                TransitionDefinition('pg', 'registration'),
                TransitionDefinition('registration', 'eg'),
                TransitionDefinition('pg', 'confirmregistration'),
                TransitionDefinition('confirmregistration', 'eg'),
                TransitionDefinition('pg', 'remind'),
                TransitionDefinition('remind', 'eg'),
                TransitionDefinition('pg', 'see_registration'),
                TransitionDefinition('see_registration', 'eg'),
                TransitionDefinition('pg', 'see_registrations'),
                TransitionDefinition('see_registrations', 'eg'),
                TransitionDefinition('pg', 'remove'),
                TransitionDefinition('remove', 'eg'),
                TransitionDefinition('eg', 'end'),
        )


REGISTRATION_GROUP = {
    'group_id': 'vote_new_registration',
    'group_title': _('Vote to confirm or not the identity of the user'),
    'group_activate': False,
    'group_activator_title': _('Vote to confirm or not the identity of the user'),
    'group_activator_class_css': 'vote-action',
    'group_activator_style_picto': 'octicon octicon-check',
    'group_activator_order': 100
}

BALLOT_DATA[Preregistration.__name__+'-registrationmoderation'] = {
    'ballot_description_template': 'novaideo:views/templates/ballots/new_registration.pt',
    'ballot_title': _("Confirm the user identity"),
    'true_value': _("Identity confirmed"),
    'false_value': _("Identity NOT confirmed"),
    'process_id': 'registrationmoderation',
    'group': REGISTRATION_GROUP
}


@process_definition(
    name='registrationmoderation',
    id='registrationmoderation')
class RegistrationModeration(ContentBallot):
    ballot_action = ModerationVote

    def __init__(self, **kwargs):
        super(RegistrationModeration, self).__init__(**kwargs)

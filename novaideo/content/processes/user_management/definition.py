# Copyright (c) 2014 by Ecreall under licence AGPL terms
# avalaible on http://www.gnu.org/licenses/agpl.html

# licence: AGPL
# author: Amen Souissi
import datetime
from persistent.list import PersistentList

from dace.processdefinition.processdef import ProcessDefinition
from dace.processdefinition.activitydef import (
    ActivityDefinition,
    SubProcessDefinition as OriginSubProcessDefinition)
from dace.processdefinition.gatewaydef import (
    ExclusiveGatewayDefinition,
    ParallelGatewayDefinition)
from dace.processdefinition.transitiondef import TransitionDefinition
from dace.processdefinition.eventdef import (
    StartEventDefinition,
    EndEventDefinition)
from dace.processinstance.activity import (
    SubProcess as OriginSubProcess)
from dace.objectofcollaboration.services.processdef_container import (
    process_definition)
from dace.util import getSite
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
    SeePerson,
    AssignRoles,
    ConfirmRegistration,
    Remind,
    SeeRegistration,
    SeeRegistrations,
    RemoveRegistration,
    ModerationVote,
    close_votes)
from novaideo import _
from novaideo.content.ballot import Ballot


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
                                       description=_("Deactivate the profile"),
                                       title=_("Deactivate the profile"),
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
                discuss = ActivityDefinition(contexts=[Discuss],
                                       description=_("Discuss"),
                                       title=_("Discuss"),
                                       groups=[]),
                general_discuss = ActivityDefinition(contexts=[GeneralDiscuss],
                                       description=_("Discuss"),
                                       title=_("Discuss"),
                                       groups=[]),
                eg = ExclusiveGatewayDefinition(),
                end = EndEventDefinition(),
        )
        self.defineTransitions(
                TransitionDefinition('start', 'pg'),
                TransitionDefinition('pg', 'login'),
                TransitionDefinition('pg', 'logout'),
                TransitionDefinition('login', 'eg'),
                TransitionDefinition('logout', 'eg'),
                TransitionDefinition('pg', 'discuss'),
                TransitionDefinition('discuss', 'eg'),
                TransitionDefinition('pg', 'general_discuss'),
                TransitionDefinition('general_discuss', 'eg'),
                TransitionDefinition('pg', 'edit'),
                TransitionDefinition('edit', 'eg'),
                TransitionDefinition('pg', 'deactivate'),
                TransitionDefinition('deactivate', 'eg'),
                TransitionDefinition('pg', 'activate'),
                TransitionDefinition('activate', 'eg'),
                TransitionDefinition('pg', 'assign_roles'),
                TransitionDefinition('assign_roles', 'eg'),
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


MODERATION_DESCRIPTION = _("Vous êtes invité à vérifier et confirmer l'identité de "
                           "l'utilisateur enregistré. Cela afin de garantir l'unicité "
                           "de ce compte. Si la majorité confirme l'identité de ce compte, "
                           "le compte sera validé, sinon le compte sera supprimé.")


class SubProcessFirstVote(OriginSubProcess):

    def __init__(self, definition):
        super(SubProcessFirstVote, self).__init__(definition)

    def stop(self):
        request = get_current_request()
        for process in self.sub_processes:
            exec_ctx = process.execution_context
            vote_processes = exec_ctx.get_involved_collection('vote_processes')
            vote_processes = [process for process in vote_processes
                              if not process._finished]
            if vote_processes:
                close_votes(None, request, vote_processes)

        super(SubProcessFirstVote, self).stop()


class SubProcessDefinition(OriginSubProcessDefinition):
    """Run the voting process for the moderation of registrations"""

    factory = SubProcessFirstVote

    def _init_subprocess(self, process, subprocess):
        root = getSite()
        duration = datetime.timedelta(
            days=getattr(root, 'duration_moderation_vote', 7))
        preregistration = process.execution_context.created_entity(
            'preregistration')
        electors = preregistration.moderators
        subjects = [preregistration]
        ballot = Ballot('Referendum', electors, subjects, duration,
                        true_val=_("Confirmed identity"),
                        false_val=_("Not confirmed identity"))
        preregistration.addtoproperty('ballots', ballot)
        ballot.report.description = MODERATION_DESCRIPTION
        ballot.title = _("Confirm the user identity")
        processes = ballot.run_ballot()
        subprocess.ballots = PersistentList()
        subprocess.ballots.append(ballot)
        preregistration.moderation_ballot = ballot
        subprocess.execution_context.add_involved_collection(
            'vote_processes', processes)
        subprocess.duration = duration


@process_definition(
    name='registrationmoderation',
    id='registrationmoderation')
class RegistrationModeration(ProcessDefinition, VisualisableElement):
    isControlled = True
    isVolatile = True

    def __init__(self, **kwargs):
        super(RegistrationModeration, self).__init__(**kwargs)
        self.title = _('Registration moderation')
        self.description = _('Registration moderation')

    def _init_definition(self):
        self.defineNodes(
                start = StartEventDefinition(),
                moderation_vote = SubProcessDefinition(pd='ballotprocess', contexts=[ModerationVote],
                                       description=_("Start voting for moderation"),
                                       title=_("Start voting for moderation"),
                                       groups=[]),
                end = EndEventDefinition(),
        )
        self.defineTransitions(
                TransitionDefinition('start', 'moderation_vote'),
                TransitionDefinition('moderation_vote', 'end'),
        )

# Copyright (c) 2014 by Ecreall under licence AGPL terms
# available on http://www.gnu.org/licenses/agpl.html

# licence: AGPL
# author: Amen Souissi
"""
This module represent the Event management process definition
powered by the dace engine. This process is unique, which means that
this process is instantiated only once.
"""
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
    Create,
    Edit,
    Remove,
    SeeEvent,
    SeeRelatedEvents)
from novaideo import _


@process_definition(name='eventmanagement', id='eventmanagement')
class EventManagement(ProcessDefinition, VisualisableElement):
    isUnique = True

    def __init__(self, **kwargs):
        super(EventManagement, self).__init__(**kwargs)
        self.title = _('Event management')
        self.description = _('Event management')

    def _init_definition(self):
        self.defineNodes(
                start = StartEventDefinition(),
                pg = ParallelGatewayDefinition(),
                create = ActivityDefinition(contexts=[Create],
                                       description=_("Organise a discussion event"),
                                       title=_("Organise a discussion event"),
                                       groups=[]),
                edit = ActivityDefinition(contexts=[Edit],
                                       description=_("Edit the discussion event"),
                                       title=_("Edit"),
                                       groups=[]),
                remove = ActivityDefinition(contexts=[Remove],
                                       description=_("Remove the discussion event"),
                                       title=_("Remove"),
                                       groups=[]),
                see_events = ActivityDefinition(contexts=[SeeRelatedEvents],
                                       description=_("The organised discussion events"),
                                       title=_("The organised discussion events"),
                                       groups=[]),
                see = ActivityDefinition(contexts=[SeeEvent],
                                       description=_("Details"),
                                       title=_("Details"),
                                       groups=[]),
                eg = ExclusiveGatewayDefinition(),
                end = EndEventDefinition(),
        )
        self.defineTransitions(
                TransitionDefinition('start', 'pg'),
                TransitionDefinition('pg', 'create'),
                TransitionDefinition('create', 'eg'),
                TransitionDefinition('pg', 'edit'),
                TransitionDefinition('edit', 'eg'),
                TransitionDefinition('pg', 'remove'),
                TransitionDefinition('remove', 'eg'),
                TransitionDefinition('pg', 'see_events'),
                TransitionDefinition('see_events', 'eg'),
                TransitionDefinition('pg', 'see'),
                TransitionDefinition('see', 'eg'),
                TransitionDefinition('eg', 'end'),
        )

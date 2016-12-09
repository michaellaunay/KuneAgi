# Copyright (c) 2014 by Ecreall under licence AGPL terms
# avalaible on http://www.gnu.org/licenses/agpl.html

# licence: AGPL
# author: Amen Souissi
"""
This module represent the member notation process definition
powered by the dace engine. This process is vlolatile, which means
that this process is automatically removed after the end. And is controlled,
which means that this process is not automatically instanciated.
"""

from dace.processdefinition.processdef import ProcessDefinition
from dace.processdefinition.activitydef import ActivityDefinition
from dace.processdefinition.transitiondef import TransitionDefinition
from dace.processdefinition.eventdef import (
    StartEventDefinition,
    EndEventDefinition)
from dace.objectofcollaboration.services.processdef_container import(
    process_definition)
from pontus.core import VisualisableElement

from .behaviors import Note
from novaideo import _


@process_definition(
    name='membernotationmanagement',
    id='membernotationmanagement')
class MemberNotationProcess(ProcessDefinition, VisualisableElement):
    isVolatile = True
    isControlled = True
    discriminator = 'Member notation process'

    def __init__(self, **kwargs):
        super(MemberNotationProcess, self).__init__(**kwargs)
        self.title = _('Member notation process')
        self.description = _('Member notation process')

    def _init_definition(self):
        self.defineNodes(
                start = StartEventDefinition(),
                note = ActivityDefinition(contexts=[Note],
                                       description=_("Note"),
                                       title=_("Note"),
                                       groups=[]),
                end = EndEventDefinition(),
        )
        self.defineTransitions(
                TransitionDefinition('start', 'note'),
                TransitionDefinition('note', 'end'),
        )

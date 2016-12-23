# Copyright (c) 2014 by Ecreall under licence AGPL terms
# avalaible on http://www.gnu.org/licenses/agpl.html

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
    AddSmartFolder,
    AddSubSmartFolder,
    EditSmartFolder,
    RemoveSmartFolder,
    SeeSmartFolder,
    SeeSmartFolders,
    PublishSmartFolder,
    WithdrawSmartFolder,
    OrderSmartFolders,
    OrderSubSmartFolders,
    )
from novaideo import _


@process_definition(name='smartfoldermanagement',
                    id='smartfoldermanagement')
class SmartFolderProcess(ProcessDefinition, VisualisableElement):
    isUnique = True

    def __init__(self, **kwargs):
        super(SmartFolderProcess, self).__init__(**kwargs)
        self.title = _('Smart folders management')
        self.description = _('Smart folders management')

    def _init_definition(self):
        self.defineNodes(
                start = StartEventDefinition(),
                pg = ParallelGatewayDefinition(),
                add_smart_folder = ActivityDefinition(contexts=[AddSmartFolder],
                                       description=_("Create a center of interest"),
                                       title=_("Create a center of interest"),
                                       groups=[_("Add")]),
                addsub_smart_folder = ActivityDefinition(contexts=[AddSubSmartFolder],
                                       description=_("Create a sub center of interest"),
                                       title=_("Create a sub center of interest"),
                                       groups=[]),
                edit_smart_folder = ActivityDefinition(contexts=[EditSmartFolder],
                                       description=_("Edit the center of interest"),
                                       title=_("Edit"),
                                       groups=[]),
                remove_smart_folder = ActivityDefinition(contexts=[RemoveSmartFolder],
                                       description=_("Remove center of interest"),
                                       title=_("Remove"),
                                       groups=[]),
                see_smart_folder = ActivityDefinition(contexts=[SeeSmartFolder],
                                       description=_("See a center of interest"),
                                       title=_("See a center of interest"),
                                       groups=[]),
                publish_smart_folder = ActivityDefinition(contexts=[PublishSmartFolder],
                                       description=_("Publish the center of interest"),
                                       title=_("Publish"),
                                       groups=[]),
                withdraw_smart_folder = ActivityDefinition(contexts=[WithdrawSmartFolder],
                                       description=_("Withdraw the center of interest"),
                                       title=_("Withdraw the center of interest"),
                                       groups=[]),
                see_smart_folders = ActivityDefinition(contexts=[SeeSmartFolders],
                                       description=_("Registered interests"),
                                       title=_("Registered interests"),
                                       groups=[_('See')]),
                order_smart_folders = ActivityDefinition(contexts=[OrderSmartFolders],
                                       description=_("Order"),
                                       title=_("Order"),
                                       groups=[]),
                order_sub_smart_folders = ActivityDefinition(contexts=[OrderSubSmartFolders],
                                       description=_("Order"),
                                       title=_("Order"),
                                       groups=[]),
                eg = ExclusiveGatewayDefinition(),
                end = EndEventDefinition(),
        )
        self.defineTransitions(
                TransitionDefinition('start', 'pg'),
                TransitionDefinition('pg', 'add_smart_folder'),
                TransitionDefinition('add_smart_folder', 'eg'),
                TransitionDefinition('pg', 'publish_smart_folder'),
                TransitionDefinition('publish_smart_folder', 'eg'),
                TransitionDefinition('pg', 'withdraw_smart_folder'),
                TransitionDefinition('withdraw_smart_folder', 'eg'),
                TransitionDefinition('pg', 'addsub_smart_folder'),
                TransitionDefinition('addsub_smart_folder', 'eg'),
                TransitionDefinition('pg', 'edit_smart_folder'),
                TransitionDefinition('edit_smart_folder', 'eg'),
                TransitionDefinition('pg', 'remove_smart_folder'),
                TransitionDefinition('remove_smart_folder', 'eg'),
                TransitionDefinition('pg', 'see_smart_folder'),
                TransitionDefinition('see_smart_folder', 'eg'),
                TransitionDefinition('pg', 'see_smart_folders'),
                TransitionDefinition('see_smart_folders', 'eg'),
                TransitionDefinition('pg', 'order_smart_folders'),
                TransitionDefinition('order_smart_folders', 'eg'),
                TransitionDefinition('pg', 'order_sub_smart_folders'),
                TransitionDefinition('order_sub_smart_folders', 'eg'),
                TransitionDefinition('eg', 'end'),
        )

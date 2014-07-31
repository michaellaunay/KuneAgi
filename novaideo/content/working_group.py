from zope.interface import implementer

from substanced.content import content
from substanced.util import renamer
from substanced.schema import NameSchemaNode

from dace.objectofcollaboration.entity import Entity
from dace.descriptors import CompositeUniqueProperty
from pontus.schema import omit
from pontus.core import VisualisableElement, VisualisableElementSchema

from .proposal import ProposalSchema, Proposal
from .interface import IWorkingGroup
from novaideo import _


def context_is_a_workinggroup(context, request):
    return request.registry.content.istype(context, 'workinggroup')


class WorkingGroupSchema(VisualisableElementSchema):

    name = NameSchemaNode(
        editing=context_is_a_workinggroup,
        )

    proposal = omit(ProposalSchema(name=_('Proposal'),
                                                factory=Proposal,
                                                editable=True),['_csrf_token_'])


@content(
    'workinggroup',
    icon='glyphicon glyphicon-align-left',
    )
@implementer(IWorkingGroup)
class WorkingGroup(VisualisableElement, Entity):
    name = renamer()
    template = 'pontus:templates/visualisable_templates/object.pt'
    proposal = CompositeUniqueProperty('proposal', 'myparent')

    def __init__(self, **kwargs):
        super(WorkingGroup, self).__init__(**kwargs)

    def setproposal(self, proposal):
        self.setproperty('proposal', proposal)



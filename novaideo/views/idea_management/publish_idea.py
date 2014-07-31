from pyramid.view import view_config

from dace.util import get_obj
from dace.processinstance.core import DEFAULTMAPPING_ACTIONS_VIEWS
from pontus.form import FormView
from pontus.view_operation import MultipleView
from pontus.schema import select
from pontus.view import BasicView, View, merge_dicts, ViewError
from pontus.default_behavior import Cancel

from novaideo.content.processes.idea_management.behaviors import  PublishIdea
from novaideo.content.idea import Idea
from novaideo import _



class PublishIdeaViewStudyReport(BasicView):
    title = _('Alert for publication')
    name='alertforpublication'
    template ='novaideo:views/idea_management/templates/alert_idea_publish.pt'

    def update(self):
        result = {}
        values = {'context': self.context}
        body = self.content(result=values, template=self.template)['body']
        item = self.adapt_item(body, self.viewid)
        result['coordinates'] = {self.coordinates:[item]}
        return result


class PublishIdeaView(FormView):
    title =  _('Publish')
    name ='publishideaform'
    formid = 'formpublishidea'
    behaviors = [PublishIdea, Cancel]
    validate_behaviors = False


@view_config(
    name='publishidea',
    context=Idea,
    renderer='pontus:templates/view.pt',
    )
class PublishIdeaViewMultipleView(MultipleView):
    title = _('Publish')
    name = 'publishidea'
    behaviors = [PublishIdea]
    viewid = 'publishidea'
    template = 'pontus.dace_ui_extension:templates/mergedmultipleview.pt'
    views = (PublishIdeaViewStudyReport, PublishIdeaView)
    validators = [PublishIdea.get_validator()]




DEFAULTMAPPING_ACTIONS_VIEWS.update({PublishIdea:PublishIdeaViewMultipleView})

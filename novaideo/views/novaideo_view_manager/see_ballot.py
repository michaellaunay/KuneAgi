# Copyright (c) 2014 by Ecreall under licence AGPL terms
# avalaible on http://www.gnu.org/licenses/agpl.html

# licence: AGPL
# author: Amen Souissi

from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

from substanced.util import Batch, get_oid

from dace.processinstance.core import (
    ValidationError, Validator)
from dace.objectofcollaboration.principal.util import (
    get_current, has_any_roles)
from dace.util import getSite, find_catalog
from dace.processinstance.core import DEFAULTMAPPING_ACTIONS_VIEWS
from pontus.view import BasicView
from pontus.util import merge_dicts
from pontus.view_operation import MultipleView

from novaideo.content.processes import get_states_mapping
from novaideo.core import BATCH_DEFAULT_SIZE
from novaideo.content.processes.novaideo_view_manager.behaviors import SeeBallot
from novaideo.content.ballot import Ballot
from novaideo.utilities.util import (
    generate_navbars, ObjectRemovedException, render_listing_objs,
    render_listing_obj)
from novaideo import _
from novaideo.content.interface import IVote
from novaideo.views.filter import (
    get_filter, FILTER_SOURCES, merge_with_filter_view, find_entities)
from novaideo.views.filter.sort import (
    sort_view_objects)


CONTENTS_MESSAGES = {
    '0': _(u"""No vote"""),
    '1': _(u"""One vote"""),
    '*': _(u"""${nember} votes""")
}


@view_config(
    name='seevotes',
    context=Ballot,
    renderer='pontus:templates/views_templates/grid.pt',
    )
class VotesView(BasicView):
    name = 'seevotes'
    viewid = 'seevotes'
    template = 'novaideo:views/novaideo_view_manager/templates/table_result.pt'
    wrapper_template = 'pontus:templates/views_templates/simple_view_wrapper.pt'
    view_icon = 'glyphicon glyphicon-saved'
    title = _('Votes')
    empty_message = _("No vote")
    empty_icon = 'glyphicon glyphicon-saved'
    selected_filter = [('temporal_filter', ['negation', 'created_date']),
                       'text_filter']

    def update(self):
        user = get_current()
        # Vote is non a searchable element
        # we need add it to the args dict
        objects = self.context.ballot_box.votes
        objects.extend(objects)
        objects.extend(objects)
        url = self.request.resource_url(self.context, self.name)
        batch = Batch(objects, self.request,
                      url=url,
                      default_size=BATCH_DEFAULT_SIZE)
        batch.target = "#results-votes"
        len_votes = batch.seqlen
        index = str(len_votes) if len_votes <= 1 else '*'
        if not self.parent:
            self.title = _(CONTENTS_MESSAGES[index],
                           mapping={'nember': len_votes})
        elif index != '*':
            self.title = _('The vote')

        result_body, result = render_listing_objs(
            self.request, batch, user)
        values = {'bodies': result_body,
                  'batch': batch,
                  'empty_message': self.empty_message,
                  'empty_icon': self.empty_icon}
        body = self.content(args=values, template=self.template)['body']
        item = self.adapt_item(body, self.viewid)
        item['isactive'] = True
        result['coordinates'] = {self.coordinates: [item]}
        return result


class BallotresultView(BasicView):
    name = 'seeballotresultballot'
    viewid = 'seeballotresultballot'
    template = 'novaideo:views/novaideo_view_manager/templates/ballotresult.pt'
    wrapper_template = 'pontus:templates/views_templates/simple_view_wrapper.pt'
    view_icon = 'glyphicon glyphicon-stats'

    title = _('Ballotresult')

    def update(self):
        result = {}
        values = {
            'object': self.context,
        }
        body = self.content(args=values, template=self.template)['body']
        item = self.adapt_item(body, self.viewid)
        result['coordinates'] = {self.coordinates: [item]}
        result = merge_dicts(self.requirements_copy, result)
        return result


class VotesDetailsView(MultipleView):
    name = 'seevotesdetails'
    viewid = 'seevotesdetails'
    template = 'novaideo:views/templates/multipleview.pt'
    wrapper_template = 'pontus:templates/views_templates/simple_view_wrapper.pt'
    css_class = 'integreted-tab-content ballot-details'
    title = ''
    views = (VotesView, BallotresultView)

    def _activate(self, items):
        pass


class SeeBallotHeaderView(BasicView):
    title = ''
    name = 'seeballotheader'
    behaviors = [SeeBallot]
    template = 'novaideo:views/novaideo_view_manager/templates/see_ballot.pt'
    wrapper_template = 'pontus:templates/views_templates/simple_view_wrapper.pt'
    viewid = 'seeballotheader'

    def update(self):
        self.execute(None)
        user = get_current()
        votes = self.context.ballot_box.votes
        len_votes = len(votes)
        index = str(len_votes)
        if len_votes > 1:
            index = '*'

        votes_title = _(CONTENTS_MESSAGES[index],
                        mapping={'nember': len_votes})
        result = {}
        values = {
            'ballot': self.context,
            # 'state': get_states_mapping(
            #     user, self.context, self.context.state[0]),
            'current_user': user,
            'votes_title': votes_title,
        }
        body = self.content(args=values, template=self.template)['body']
        item = self.adapt_item(body, self.viewid)
        result['coordinates'] = {self.coordinates: [item]}
        return result


@view_config(
    name='',
    context=Ballot,
    renderer='pontus:templates/views_templates/grid.pt',
    )
@view_config(
    name='index',
    context=Ballot,
    renderer='pontus:templates/views_templates/grid.pt',
    )
class SeeBallotView(MultipleView):
    name = 'index'
    template = 'novaideo:views/templates/entity_multipleview.pt'
    title = ''
    views = (SeeBallotHeaderView, VotesDetailsView)
    validators = [SeeBallot.get_validator()]


DEFAULTMAPPING_ACTIONS_VIEWS.update(
    {SeeBallot: SeeBallotView})

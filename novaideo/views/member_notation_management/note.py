# Copyright (c) 2014 by Ecreall under licence AGPL terms 
# avalaible on http://www.gnu.org/licenses/agpl.html 

# licence: AGPL
# author: Amen Souissi

import colander
import deform
from pyramid.view import view_config
from pyramid import renderers

from dace.processinstance.core import DEFAULTMAPPING_ACTIONS_VIEWS
from dace.objectofcollaboration.entity import Entity
from pontus.form import FormView
from pontus.view_operation import MultipleView
from pontus.view import BasicView
from pontus.schema import Schema

from novaideo.content.processes.member_notation_management.behaviors import (
    Note)
from novaideo.content.proposal import Proposal
from novaideo import _


class NoteViewStudyReport(BasicView):
    title = _('FPTP note')
    name = 'notefptp'
    template = 'novaideo:views/member_notation_management/templates/note.pt'

    def _get_ballot_description(self, ballot_process, ballot_report):
        template = getattr(ballot_report, 'description_template', None)
        if template:
            return renderers.render(
                template,
                {'ballot_report': ballot_report,
                 'process': ballot_process,
                 'context': self.context},
                self.request)

        return ballot_report.description

    def update(self):
        result = {}
        ballot_report = None
        ballot_process = None
        try:
            noteform_view = self.parent.validated_children[1]
            noteform_actions = list(noteform_view.behaviors_instances.values())
            ballot_process = noteform_actions[0].process
            ballot_report = ballot_process.ballot.report
        except Exception:
            pass

        description = self._get_ballot_description(
            ballot_process, ballot_report)
        values = {
            'context': self.context,
            'ballot_report': ballot_report,
            'description': description}
        body = self.content(args=values, template=self.template)['body']
        item = self.adapt_item(body, self.viewid)
        result['coordinates'] = {self.coordinates: [item]}
        return result


def notes_choice(ballot_report):
    values = getattr(ballot_report.ballottype, 'group_values', None)
    return deform.widget.RadioChoiceWidget(values=values)


class NotesSchema(Schema):

    note = colander.SchemaNode(
        colander.String(),
        default="0",
        title=_('Notes'),
    )


class NoteFormView(FormView):
    title = _('Note the member')
    name = 'noteform'
    formid = 'formnote'
    behaviors = [Note]
    validate_behaviors = False
    schema = NotesSchema()

    def before_update(self):
        ballot_report = None
        try:
            note_actions = list(self.behaviors_instances.values())
            ballot_report = note_actions[0].process.ballot.report
        except Exception:
            return

        notes_widget = notes_choice(ballot_report)
        note_node = self.schema.get('note')
        group_default = getattr(ballot_report.ballottype, 'group_default', None)
        if group_default:
            note_node.default = group_default

        note_node.widget = notes_widget
        self.schema.view = self
        formwidget = deform.widget.FormWidget(css_class='vote-form')
        self.action = self.request.resource_url(
            self.context, 'notefptp',
            query={'action_uid': getattr(note_actions[0], '__oid__', '')})
        self.schema.widget = formwidget


@view_config(
    name='notefptp',
    context=Proposal,
    renderer='pontus:templates/views_templates/grid.pt',
    )
class NoteViewMultipleView(MultipleView):
    title = _('Note')
    name = 'notefptp'
    viewid = 'notefptp'
    template = 'daceui:templates/simple_mergedmultipleview.pt'
    wrapper_template = 'novaideo:views/ballot_processes/templates/panel_item.pt'
    views = (NoteViewStudyReport, NoteFormView)
    validators = [Note.get_validator()]

    def get_message(self):
        ballot_report = None
        try:
            noteform_view = self.validated_children[1]
            noteform_actions = list(noteform_view.behaviors_instances.values())
            ballot_report = noteform_actions[0].process.ballot.report
        except Exception:
            pass

        return ballot_report.ballot.title


DEFAULTMAPPING_ACTIONS_VIEWS.update({Note: NoteViewMultipleView})

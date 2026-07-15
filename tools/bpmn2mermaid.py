#!/usr/bin/env python
"""BPMN-to-mermaid extractor for dace process definitions.

Statically parses (stdlib ``ast`` only — no engine import needed) every
``definition.py`` under a root package, extracts the graphs declared
through ``defineNodes``/``defineTransitions``, and emits one Markdown
file per definition module with a mermaid flowchart and a node table
for each process class found.

The diagrams show the graph *as authored*: at registration time the
engine's normalisation may add synthetic wiring (``startpg``, ``endeg``,
``mergepg``, ``mergeeg`` — see dace docs/en/architecture.md, section 3).

Usage:
    python tools/bpmn2mermaid.py novaideo \\
        --out docs/en/processes:en --out docs/fr/processes:fr

Runs on Python 3.6 and 3.12.
"""
import argparse
import ast
import os
import sys
from collections import OrderedDict


# ---------------------------------------------------------------- helpers

def const_str(node):
    """The string value of a Str/Constant node, else None."""
    if isinstance(node, ast.Constant):
        value = node.value
        return value if isinstance(value, str) else None
    if sys.version_info < (3, 8) and isinstance(node, ast.Str):
        return node.s
    return None


def const_true(node):
    """True when the node is the constant True."""
    if isinstance(node, ast.Constant):
        return node.value is True
    if sys.version_info < (3, 8) and isinstance(node, ast.NameConstant):
        return node.value is True
    return False


def call_name(node):
    """The (dotted-last) name of a Call's func, else None."""
    if not isinstance(node, ast.Call):
        return None
    func = node.func
    if isinstance(func, ast.Name):
        return func.id
    if isinstance(func, ast.Attribute):
        return func.attr
    return None


def i18n_text(node):
    """The msgid of ``_('...')`` or a plain string, else None."""
    direct = const_str(node)
    if direct is not None:
        return direct
    if isinstance(node, ast.Call) and call_name(node) == '_' and node.args:
        return const_str(node.args[0])
    return None


def callable_label(node):
    """A short label for a transition condition node."""
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        return node.attr
    if isinstance(node, ast.Lambda):
        return 'lambda'
    if isinstance(node, ast.Call):
        name = call_name(node)
        return name + '(...)' if name else 'condition'
    return None


def rstrip_lines(text):
    """Strip trailing whitespace per line (source docstrings carry some)."""
    return '\n'.join(line.rstrip() for line in text.split('\n'))


def esc(label):
    """Escape a mermaid label."""
    return (label or '').replace('"', '&quot;').replace('|', '/')


# ------------------------------------------------------------- extraction

NODE_SHAPES = (
    # (substring of the definition class name, kind)
    ('StartEventDefinition', 'start'),
    ('EndEventDefinition', 'end'),
    ('IntermediateCatchEventDefinition', 'catch'),
    ('IntermediateThrowEventDefinition', 'throw'),
    ('ExclusiveGateway', 'xor'),
    ('ParallelGateway', 'and'),
    ('InclusiveGateway', 'or'),
    ('SubProcessDefinition', 'subprocess'),
    ('ActivityDefinition', 'activity'),
)

KIND_ICONS = {
    'Timer': '&#9200;',        # alarm clock
    'Conditional': '?',
    'Signal': '&#9889;',       # high voltage
    'Terminate': '&#8856;',    # circled slash
}


class Node(object):
    def __init__(self, name, cls):
        self.name = name
        self.cls = cls
        self.kind = 'box'
        for fragment, kind in NODE_SHAPES:
            if fragment in cls:
                self.kind = kind
                break
        self.title = None
        self.contexts = []
        self.event_kind = None      # Timer/Conditional/Signal/Terminate
        self.event_param = None     # deadline/condition callable name
        self.sub_pd = None          # sub-process definition id


class Process(object):
    def __init__(self, class_name, pd_id, registered, docstring):
        self.class_name = class_name
        self.pd_id = pd_id
        self.registered = registered
        self.docstring = docstring
        self.nodes = OrderedDict()
        self.transitions = []       # (src, tgt, condition, sync)


def parse_node(name, call):
    node = Node(name, call_name(call) or '?')
    # nested event kind: first positional arg is a *EventDefinition call
    if node.kind in ('catch', 'throw', 'start', 'end') and call.args:
        kind_call = call.args[0]
        kind_name = call_name(kind_call)
        if kind_name and kind_name.endswith('EventDefinition'):
            for key in KIND_ICONS:
                if kind_name.startswith(key):
                    node.event_kind = key
                    break
            if isinstance(kind_call, ast.Call):
                params = list(kind_call.args) + \
                         [kw.value for kw in kind_call.keywords]
                for param in params:
                    label = callable_label(param)
                    if label:
                        node.event_param = label
                        break
    for kw in call.keywords:
        if kw.arg == 'title':
            node.title = i18n_text(kw.value)
        elif kw.arg == 'contexts' and isinstance(kw.value, (ast.List,
                                                            ast.Tuple)):
            node.contexts = [elt.id for elt in kw.value.elts
                             if isinstance(elt, ast.Name)]
        elif kw.arg == 'pd':
            sub_pd = const_str(kw.value) or callable_label(kw.value)
            # the source uses the *string* 'None' as a sentinel for
            # "sub-process definition resolved at runtime"
            node.sub_pd = '(dynamic)' if sub_pd in (None, 'None') else sub_pd
    return node


def parse_transition(call):
    args = call.args
    if len(args) < 2:
        return None
    src, tgt = const_str(args[0]), const_str(args[1])
    if src is None or tgt is None:
        return None
    condition = callable_label(args[2]) if len(args) > 2 else None
    sync = False
    for kw in call.keywords:
        if kw.arg == 'sync' and const_true(kw.value):
            sync = True
        elif kw.arg == 'condition':
            condition = callable_label(kw.value)
    if condition == 'always_true':
        condition = None
    return (src, tgt, condition, sync)


def parse_class(class_node, module_doc):
    pd_id = None
    registered = False
    for deco in class_node.decorator_list:
        if call_name(deco) == 'process_definition':
            registered = True
            for kw in deco.keywords:
                if kw.arg == 'id':
                    pd_id = const_str(kw.value)
    process = Process(class_node.name, pd_id or class_node.name,
                      registered, ast.get_docstring(class_node) or '')
    found = False
    for item in ast.walk(class_node):
        if not isinstance(item, ast.Call):
            continue
        name = call_name(item)
        if name == 'defineNodes':
            found = True
            for kw in item.keywords:
                if kw.arg and isinstance(kw.value, ast.Call):
                    process.nodes[kw.arg] = parse_node(kw.arg, kw.value)
        elif name == 'defineTransitions':
            for arg in item.args:
                if isinstance(arg, ast.Call) and \
                        call_name(arg) == 'TransitionDefinition':
                    transition = parse_transition(arg)
                    if transition:
                        process.transitions.append(transition)
    return process if found else None


def parse_module(path):
    with open(path, 'rb') as source:
        tree = ast.parse(source.read())
    module_doc = ast.get_docstring(tree) or ''
    processes = []
    for item in tree.body:
        if isinstance(item, ast.ClassDef):
            process = parse_class(item, module_doc)
            if process:
                processes.append(process)
    return module_doc, processes


# --------------------------------------------------------------- emission

def node_line(node):
    ident = 'n_' + node.name
    title = esc(node.title or node.name)
    if node.kind == 'start':
        return '%s(("start"))' % ident
    if node.kind == 'end':
        icon = KIND_ICONS.get(node.event_kind, '')
        label = (icon + ' end').strip()
        return '%s((("%s")))' % (ident, label)
    if node.kind == 'xor':
        return '%s{"X"}' % ident
    if node.kind == 'and':
        return '%s{"+"}' % ident
    if node.kind == 'or':
        return '%s{"O"}' % ident
    if node.kind in ('catch', 'throw'):
        icon = KIND_ICONS.get(node.event_kind, '&#9993;')
        param = esc(node.event_param or node.name)
        return '%s(("%s %s"))' % (ident, icon, param)
    if node.kind == 'subprocess':
        sub = ' &#8594; ' + esc(node.sub_pd) if node.sub_pd else ''
        return '%s[["%s%s"]]' % (ident, title, sub)
    # activity / fallback box
    label = '<b>%s</b>' % title
    if node.contexts:
        shown = node.contexts[:3]
        more = '&#8230;' if len(node.contexts) > 3 else ''
        label += '<br/><i>%s%s</i>' % (esc(', '.join(shown)), more)
    return '%s["%s"]' % (ident, label)


def mermaid_for(process, missing):
    lines = ['flowchart TD']
    for node in process.nodes.values():
        lines.append('    ' + node_line(node))
    for src, tgt, condition, sync in process.transitions:
        for endpoint in (src, tgt):
            if endpoint not in process.nodes:
                missing.add((process.pd_id, endpoint))
        label = esc(condition) if condition else ''
        if sync and label:
            label += ' (sync)'
        elif sync:
            label = 'sync'
        arrow = '-->|"%s"|' % label if label else '-->'
        lines.append('    n_%s %s n_%s' % (src, arrow, tgt))
    return '\n'.join(lines)


HEADINGS = {
    'en': {
        'index_title': 'Business process diagrams',
        'index_intro': (
            'Generated by `tools/bpmn2mermaid.py` — do **not** edit by '
            'hand; regenerate instead. Diagrams show the graphs *as '
            'authored*: the engine normalisation may add synthetic '
            'wiring (`startpg`, `endeg`, `mergepg`, `mergeeg`).'),
        'process': 'Process',
        'unregistered': 'base class, not registered',
        'nodes': 'Nodes', 'node': 'Node', 'type': 'Type',
        'title': 'Title', 'behaviors': 'Behaviors',
        'processes': 'processes', 'transitions': 'transitions',
        'module': 'Module',
    },
    'fr': {
        'index_title': 'Diagrammes des processus métier',
        'index_intro': (
            'Généré par `tools/bpmn2mermaid.py` — ne **pas** éditer à la '
            'main ; regénérer. Les diagrammes montrent les graphes *tels '
            'qu\'écrits* : la normalisation du moteur peut ajouter un '
            'câblage synthétique (`startpg`, `endeg`, `mergepg`, '
            '`mergeeg`).'),
        'process': 'Processus',
        'unregistered': 'classe de base, non enregistrée',
        'nodes': 'Nœuds', 'node': 'Nœud', 'type': 'Type',
        'title': 'Titre', 'behaviors': 'Behaviors',
        'processes': 'processus', 'transitions': 'transitions',
        'module': 'Module',
    },
}

KIND_LABELS = {
    'start': 'start event', 'end': 'end event', 'xor': 'XOR gateway',
    'and': 'AND gateway', 'or': 'OR gateway', 'catch': 'catch event',
    'throw': 'throw event', 'subprocess': 'sub-process',
    'activity': 'activity', 'box': '?',
}


def emit_module(rel_id, module_doc, processes, lang, missing):
    text = HEADINGS[lang]
    out = ['# %s' % rel_id, '']
    if module_doc:
        out.append(rstrip_lines(module_doc.strip()))
        out.append('')
    for process in processes:
        flag = '' if process.registered else \
               ' *(%s)*' % text['unregistered']
        out.append('## %s `%s`%s' % (text['process'], process.pd_id, flag))
        out.append('')
        if process.docstring:
            out.append(rstrip_lines(process.docstring.strip()))
            out.append('')
        out.append('```mermaid')
        out.append(mermaid_for(process, missing))
        out.append('```')
        out.append('')
        activities = [n for n in process.nodes.values()
                      if n.kind in ('activity', 'subprocess', 'box')]
        if activities:
            out.append('| %s | %s | %s | %s |' % (
                text['node'], text['type'], text['title'],
                text['behaviors']))
            out.append('|---|---|---|---|')
            for node in activities:
                out.append('| `%s` | %s | %s | %s |' % (
                    node.name, KIND_LABELS[node.kind],
                    esc(node.title or ''),
                    ', '.join('`%s`' % c for c in node.contexts)))
            out.append('')
    return '\n'.join(out) + '\n'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root', help='package root to scan')
    parser.add_argument('--out', action='append', required=True,
                        metavar='DIR:LANG',
                        help='output directory and language (en|fr)')
    options = parser.parse_args()

    modules = []
    for dirpath, dirnames, filenames in os.walk(options.root):
        dirnames[:] = [d for d in dirnames
                       if d not in ('__pycache__', 'tests')]
        if 'definition.py' in filenames:
            modules.append(os.path.join(dirpath, 'definition.py'))
    modules.sort()

    parsed = []
    missing = set()
    for path in modules:
        rel = os.path.relpath(os.path.dirname(path), options.root)
        rel_id = rel.replace(os.sep, '.')
        module_doc, processes = parse_module(path)
        if processes:
            parsed.append((rel_id, module_doc, processes))

    for spec in options.out:
        directory, lang = spec.rsplit(':', 1)
        text = HEADINGS[lang]
        if not os.path.isdir(directory):
            os.makedirs(directory)
        index = ['# %s' % text['index_title'], '', text['index_intro'], '',
                 '| %s | %s | %s |' % (text['module'], text['processes'],
                                       text['transitions']),
                 '|---|---|---|']
        for rel_id, module_doc, processes in parsed:
            filename = rel_id + '.md'
            with open(os.path.join(directory, filename), 'w') as handle:
                handle.write(emit_module(rel_id, module_doc, processes,
                                         lang, missing))
            names = ', '.join('`%s`' % p.pd_id for p in processes)
            n_transitions = sum(len(p.transitions) for p in processes)
            index.append('| [%s](%s) | %s | %d |' % (
                rel_id, filename, names, n_transitions))
        with open(os.path.join(directory, 'README.md'), 'w') as handle:
            handle.write('\n'.join(index) + '\n')

    total = sum(len(p) for _, _, p in parsed)
    print('%d definition modules, %d processes -> %s' % (
        len(parsed), total, ', '.join(o.split(':')[0]
                                      for o in options.out)))
    for pd_id, endpoint in sorted(missing):
        print('WARNING: %s references unknown node %r' % (pd_id, endpoint))


if __name__ == '__main__':
    main()

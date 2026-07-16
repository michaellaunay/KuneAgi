#!/usr/bin/env python
"""Port the graphene-1-era stack to Python 3.10+ in place.

nova-ideo's GraphQL schema is written for graphene 1.x (graphql-core
1.1, graphql-relay 0.4.5 — the 2017 pins). Those releases import the
collections ABCs from ``collections``, which Python 3.10 removed. This
tool patches an *installed* copy (site-packages) mechanically:

- ``from collections import X[, ...]`` — ABC names move to a
  ``collections.abc`` import line (non-ABC names, e.g. ``OrderedDict``,
  stay);
- attribute uses ``collections.X`` become ``collections.abc.X``.

Idempotent. Run it right after installing the era pins::

    python tools/patch_graphql1_py312.py $(python -c \\
        "import graphql, os; print(os.path.dirname(graphql.__file__))") \\
        ...same for graphene, graphql_relay

Phase 3 / M4 of the porting plan. The long-term decision (port the
schema to a maintained graphene, or fork the era stack) is a post-M4
item; this keeps the golden-master behaviour byte-identical meanwhile.
"""
import re
import sys
import pathlib

ABC_NAMES = {
    'Mapping', 'MutableMapping', 'Iterable', 'Iterator', 'Sequence',
    'MutableSequence', 'Set', 'MutableSet', 'Callable', 'Hashable',
    'Container', 'Sized', 'Collection', 'Generator', 'OrderedDict_',
}
ABC_NAMES.discard('OrderedDict_')

FROM_RE = re.compile(r'^(\s*)from collections import ([^\n#]+)(#[^\n]*)?$',
                     re.M)
ATTR_RE = re.compile(r'\bcollections\.(%s)\b' % '|'.join(sorted(ABC_NAMES)))


def fix_source(source):
    """Return (new_source, changed)."""

    def split_import(match):
        indent, names, comment = match.group(1), match.group(2), match.group(3) or ''
        parts = [n.strip() for n in names.split(',') if n.strip()]
        abc = [n for n in parts if n.split(' as ')[0].strip() in ABC_NAMES]
        std = [n for n in parts if n not in abc]
        if not abc:
            return match.group(0)
        lines = []
        if std:
            lines.append('%sfrom collections import %s%s'
                         % (indent, ', '.join(std), comment))
        lines.append('%sfrom collections.abc import %s'
                     % (indent, ', '.join(abc)))
        return '\n'.join(lines)

    new = FROM_RE.sub(split_import, source)
    new = ATTR_RE.sub(r'collections.abc.\1', new)
    if 'collections.abc.' in new and \
            re.search(r'^\s*import collections\s*$', new, re.M) and \
            'import collections.abc' not in new:
        new = re.sub(r'^(\s*)import collections\s*$',
                     r'\1import collections\n\1import collections.abc',
                     new, count=1, flags=re.M)
    return new, new != source


def main(paths):
    total = 0
    for root in paths:
        for path in pathlib.Path(root).rglob('*.py'):
            source = path.read_text()
            new, changed = fix_source(source)
            if changed:
                path.write_text(new)
                total += 1
                print('patched', path)
    print('%d file(s) patched' % total)


if __name__ == '__main__':
    main(sys.argv[1:])

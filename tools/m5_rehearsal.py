#!/usr/bin/env python
"""M5 — data-migration rehearsal on a real database copy (Phase 3).

Runs the whole rehearsal, in order, on a WRITABLE copy of a
production database extracted with ``tools/decrypt_copy.py``:

0. verify   — binary check: every record must be a plain pickle
              (``.e``/``.z`` prefixes mean the copy is still
              transformed: re-extract on the server);
1. census   — structure and volumetry, then a full load sweep of every
              live object (class inventory; any broken or unloadable
              object fails the run);
2. boot     — the real ``novaideo.main`` on the copy, REACTOR-LESS
              (``dace.wosystem``: no timers, no crawler — a decade of
              expired timers would otherwise fire) and with outbound
              mail replaced by a ``DummyMailer``;
3. evolve   — list and run the unfinished evolution steps;
4. queries  — catalog queries through the era indexes;
5. reindex  — full rebuild of every catalog, then re-query: counts
              must be identical (stability check);
6. pack     — ``db.pack()``, sizes reported;
7. sweep    — final full load sweep and summary verdict.

Privacy: the tool prints AGGREGATES ONLY — counts, class names,
evolution-step identifiers, whitelisted structural service names. No
content key, title, login or address is ever printed.

Usage (inside the modern harness, see docs/modern-harness):

    .venv312/bin/python tools/m5_rehearsal.py \\
        --data /path/to/Data-plain.fs --blobs /path/to/blobstorage

The tool REFUSES to run on the originals: point it at copies.
"""
import argparse
import collections
import os
import sys

STRUCTURAL_SERVICES = {
    'catalogs', 'principals', 'runtime', 'process_definition_container',
    'relations', 'relations_container', 'locks', 'ml_file',
    'moderation_rules', 'terms_of_use',
}

INCLUDES = [
    'substanced', 'pyramid_chameleon', 'pyramid_layout',
    'pyramid_tm', 'dace.wosystem', 'pontus', 'daceui',
]


def out(*args):
    print(*args)
    sys.stdout.flush()


def phase_verify(data):
    from ZODB.FileStorage import FileStorage
    st = FileStorage(data, read_only=True)
    prefixes = collections.Counter()
    for tx in st.iterator():
        for rec in tx:
            if rec.data:
                p = rec.data[:2]
                prefixes[p if p in (b'.e', b'.z') else 'raw'] += 1
    st.close()
    out('0. verify — records:', sum(prefixes.values()),
        '| prefixes:', dict(prefixes))
    if prefixes.get(b'.e') or prefixes.get(b'.z'):
        out('   STILL TRANSFORMED: extract again with tools/decrypt_copy.py')
        sys.exit(2)


def live_oids(storage):
    current = set()
    for tx in storage.iterator():
        for rec in tx:
            if rec.data is None:
                current.discard(rec.oid)
            else:
                current.add(rec.oid)
    return current


def sweep(conn, storage, label):
    from ZODB.POSException import POSError
    classes = collections.Counter()
    broken = unloadable = 0
    for oid in live_oids(storage):
        try:
            obj = conn.get(oid)
            obj._p_activate()
            if 'broken' in type(obj).__module__:
                broken += 1
            classes[type(obj).__module__ + '.' + type(obj).__name__] += 1
            obj._p_deactivate()
        except POSError:
            unloadable += 1
        except Exception:
            unloadable += 1
    out('%s — live objects: %d | classes: %d | broken: %d | unloadable: %d'
        % (label, sum(classes.values()), len(classes), broken, unloadable))
    return classes, broken, unloadable


def counts(app_root):
    return (len(app_root['principals']['users']),
            len(app_root['runtime']),
            len(app_root['process_definition_container'].definitions))


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data', required=True)
    parser.add_argument('--blobs', required=True)
    parser.add_argument('--top', type=int, default=15,
                        help='classes shown in the census (default 15)')
    args = parser.parse_args(argv)
    data = os.path.abspath(args.data)
    blobs = os.path.abspath(args.blobs)
    for path in (data, blobs):
        if not os.path.exists(path):
            parser.error('missing: %s' % path)

    phase_verify(data)

    from pyramid import testing
    from pyramid.testing import DummyRequest

    uploads = '/tmp/m5-uploads'
    os.makedirs(uploads, exist_ok=True)
    settings = {
        'zodbconn.uri': 'file://%s?blobstorage_dir=%s' % (data, blobs),
        'tm.annotate_user': 'false',
        'sms.service': 'pyramid_sms.ovh.OvhService',
        'substanced.secret': 'rehearsal',
        'substanced.initial_login': 'admin',
        'substanced.initial_password': 'admin',
        'novaideo.secret': 'rehearsal',
        'substanced.uploads_tempdir': uploads,
        'mail.default_sender': 'rehearsal@localhost',
        'pyramid.includes': list(INCLUDES),
    }
    assert 'dace' not in settings['pyramid.includes'], 'reactor forbidden'

    testing.setUp()
    from novaideo import main as app_main
    app = app_main({}, **settings)
    from pyramid_mailer.testing import DummyMailer
    from pyramid_mailer.interfaces import IMailer
    app.registry.registerUtility(DummyMailer(), IMailer)
    out('2. boot — novaideo.main on the copy (reactor-less, mail sunk)')

    db = app.registry._zodb_databases['']
    request = DummyRequest()
    request.test = True
    testing.setUp(registry=app.registry, request=request)
    from substanced.db import root_factory
    app_root = root_factory(request)
    request.root = app_root
    zroot = app_root._p_jar.root()

    # 1. census (after boot so classes resolve through the app config)
    services = sorted(app_root.keys())
    shown = [s for s in services if s in STRUCTURAL_SERVICES]
    out('1. census — structural services:', shown,
        '(+ %d content entries)' % (len(services) - len(shown)))
    steps = zroot.get('substanced.finished_evolution_steps') or ()
    out('   finished evolution steps:', len(list(steps)))
    users, runtime, defs = counts(app_root)
    out('   users: %d | running processes: %d | definitions: %d'
        % (users, runtime, defs))
    out('   catalogs:', sorted(app_root['catalogs'].keys()))
    classes, broken, unloadable = sweep(
        app_root._p_jar, db.storage, '   sweep')
    for name, count in classes.most_common(args.top):
        out('   %6d  %s' % (count, name))
    if broken or unloadable:
        sys.exit(3)

    # 3. evolve
    from substanced.evolution import EvolutionManager
    em = EvolutionManager(app_root, app.registry)
    unfinished = [n for n, f in em.get_unfinished_steps()]
    out('3. evolve — unfinished steps on this code base:', len(unfinished))
    for name in unfinished:
        out('   -', name)
    complete = em.evolve(commit=True)
    out('   executed:', len(complete))

    # 4. queries
    import transaction
    from novaideo.content import interface as iface_mod

    def iface(*names):
        for n in names:
            obj = getattr(iface_mod, n, None)
            if obj is not None:
                return obj
        raise AttributeError(names)

    ifaces = [iface('IIdea', 'Iidea'), iface('IProposal', 'Iproposal'),
              iface('IPerson', 'Iperson')]
    op = app_root['catalogs']['dace']['object_provides']
    before = {}
    out('4. queries — era indexes through the modern stack:')
    for f in ifaces:
        before[f.__name__] = len(op.any((f.__identifier__,)).execute())
        out('   %-10s -> %d' % (f.__name__, before[f.__name__]))

    # 5. reindex + stability
    out('5. reindex —')
    for name in sorted(app_root['catalogs'].keys()):
        cat = app_root['catalogs'][name]
        cat.reindex()
        out('   %-8s : %d indexes rebuilt' % (name, len(list(cat.keys()))))
    transaction.commit()
    stable = True
    for f in ifaces:
        n = len(op.any((f.__identifier__,)).execute())
        stable = stable and n == before[f.__name__]
        out('   %-10s -> %d [%s]'
            % (f.__name__, n,
               'ok' if n == before[f.__name__] else 'DIFFERS'))
    if not stable:
        out('   INSTABILITY: rebuilt indexes disagree with era indexes')
        sys.exit(4)

    # 6. pack
    size0 = os.path.getsize(data)
    db.pack()
    size1 = os.path.getsize(data)
    out('6. pack — %.1f MB -> %.1f MB' % (size0 / 1e6, size1 / 1e6))

    # 7. final sweep
    classes, broken, unloadable = sweep(app_root._p_jar, db.storage,
                                        '7. sweep')
    users2, runtime2, defs2 = counts(app_root)
    out('   users: %d | running processes: %d | definitions: %d'
        % (users2, runtime2, defs2))
    ok = (not broken and not unloadable
          and (users, runtime, defs) == (users2, runtime2, defs2))
    out('VERDICT:', 'REHEARSAL PASSED' if ok else 'REHEARSAL FAILED')
    db.close()
    sys.exit(0 if ok else 5)


if __name__ == '__main__':
    main()

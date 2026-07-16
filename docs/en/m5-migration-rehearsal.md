# M5 — data-migration rehearsal (runbook)

*Phase 3, final milestone. French version: [`../fr/m5-migration-rehearsal.md`](../fr/m5-migration-rehearsal.md).*

The rehearsal takes a **copy of a real production database** across the
modern stack: extract → verify → census → boot (reactor-less) →
evolve → queries → reindex → pack → final sweep. It was first executed
on 2026-07-16 against a Cosmopolitical KuneAgi instance; the measured
results are at the bottom.

## Privacy rules (non-negotiable)

A production copy holds real members: names, **current email
addresses**, credential hashes, invitation tokens. Therefore:

- work on copies, on ephemeral machines; delete when done;
- aggregates only in every output, log, worklog and deliverable —
  counts, class names, step identifiers; never a key, title, login or
  address (``tools/m5_rehearsal.py`` is built that way);
- **never boot the application with the reactor on such data**: a
  decade of expired timers would re-arm and fire — behaviours would
  run, and alerts would mail *current* addresses. The tool includes
  ``dace.wosystem`` (scan + evolve steps, no reactor) and sinks the
  mailer with a ``DummyMailer`` before anything opens.

## 1. Server-side extraction

On the production host (packing first is worth it — this instance went
472 MB → 15 MB):

```bash
bin/zeopack -u ./var/zeo.sock -d 0          # live ZEO, no downtime
docker cp tools/decrypt_copy.py <container>:/app/
docker exec -w /app <container> bin/py decrypt_copy.py
tar cf kuneagi-plain-$(date +%Y%m%d).tar var/filestorage/Data-plain2.fs
```

Why ``decrypt_copy.py`` works the way it does — two lessons paid for:

- **transform storages decrypt on ``load()``, not on iteration**: the
  replication iterator (what ``copyTransactionsFrom`` uses) serves the
  at-rest bytes untouched, so a naive ZEO-client copy stays encrypted;
- the era ``cipher.encryptingstorage`` is a patched source checkout
  whose constructor differs from the modern release: the tool lets
  **ZConfig assemble the storage stack exactly as ``zeo.conf`` does**
  (same ``%import``, same section, same ``etc/encryption.conf``) — the
  keys never leave the server.

The output preserves oids and serials, so the original, never-encrypted
``var/blobstorage`` pairs with it unchanged. Undo history does not
travel (current states only): the copy arrives pre-packed.

## 2. The rehearsal

Inside the modern harness (`tools/bootstrap-modern.sh`):

```bash
.venv312/bin/python tools/m5_rehearsal.py \
    --data work/Data-plain.fs --blobs work/blobstorage
```

Phases and hard failures: still-transformed records (exit 2), any
broken or unloadable object (exit 3), rebuilt indexes disagreeing with
the era indexes (exit 4), unstable counts (exit 5). Exit 0 prints
``REHEARSAL PASSED``.

## 3. Measured results (2026-07-16, first execution)

| Check | Result |
|---|---|
| Decryption | 79,269 records, 100 % plain after extraction |
| Full load sweep | **381 classes, 0 broken, 0 unloadable** |
| Evolution steps | 73 finished in the database; **0 unfinished** on the modern code — the chain is a no-op |
| Application boot | the real ``novaideo.main`` configures against production data (reactor-less) |
| Era-index queries | idea/proposal/person counts served by hypatia 0.5 |
| Full reindex | 61 indexes rebuilt across 3 catalogs; **query counts identical** before/after |
| Pack | runs; marginal shrink (the copy arrives packed) |
| Final sweep | counts stable (users, processes, definitions) |

Ten years of pickles deserialize flawlessly on Python 3.12 / ZODB 6 —
including the engine's persistent state (``Transaction``, ``Path``,
``WorkItem``, ``Activity``). The never-move rule for persistent classes
is what this milestone cashes in.

## 4. Findings for the production side

Independent of the migration: the at-rest census showed **64,987
encrypted records against 14,282 plain ones** — the encryption
configuration drifted at some period — and blobs (attachments, avatars)
are never encrypted by this wrapper. An audit of the production
encryption setup is advisable.

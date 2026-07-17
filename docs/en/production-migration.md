# Production migration — runbook (modern stack)

*Phase 3 companion. Prerequisite: the migration rehearsal on a real
production copy must have PASSED — see
[`m5-migration-rehearsal.md`](m5-migration-rehearsal.md). French
version: [`../fr/production-migration.md`](../fr/production-migration.md).*

The supporting artifacts referenced here are in the repository:
[`etc/production-modern.ini.example`](../../etc/production-modern.ini.example)
(the target configuration template, wake-up profile included) and
`novaideo/utilities/dummy_sms.py` (the SMS sink).

## 0. Principles

- **The source instance is never modified.** Every step reads from a
  copy; the legacy container keeps running until the final switch, and
  remains the rollback until you decommission it.
- **The reactor only wakes up against sinks.** Ten years of expired
  timers WILL fire on first boot: the wake-up profile writes mails to
  disk and withholds SMS. Never boot a migrated base on a real mail
  profile first.
- **Aggregate-level observation only** (counts, states): production
  data stays out of terminals, tickets and conversations.

## 1. Freeze and extract

1. Announce the maintenance window; stop the legacy application
   processes (ZEO may stay up for the extraction).
2. Belt and braces: `repozo` backup of the live `Data.fs`.
3. Pack, then copy `Data.fs` and `blobstorage/` to the target host.
4. **Encrypted base** (`cipher.encryptingstorage`): produce the clear
   copy with `tools/decrypt_copy.py` as a read-only ZEO client on the
   live socket — the keys never leave the source host. Procedure and
   caveats: see the rehearsal runbook.

## 2. Build the target

1. Clone the quartet side by side and bootstrap:

   ```bash
   git clone git@github.com:michaellaunay/dace.git
   git clone git@github.com:michaellaunay/pontus.git
   git clone git@github.com:michaellaunay/daceui.git
   git clone git@github.com:michaellaunay/KuneAgi.git
   cd KuneAgi && tools/bootstrap-modern.sh
   ```

2. `cp etc/production-modern.ini.example etc/production.ini`, then
   edit: secrets, public URL, `mail.default_sender`, languages. Keep
   `tm.annotate_user = false` (not optional on the modern stack) and
   keep the **wake-up profile block** as shipped for now
   (`pyramid_mailer.debug` → `var/mail-out/`, `sms.service` →
   `DummySMSService`).

## 3. Drop the data in

Place the extracted (clear) `Data.fs` under `var/filestorage/` and the
blobs under `var/blobstorage/`; create `var/mail-out/` and
`var/tmp_uploads/`; check ownership and permissions.

## 4. Controlled wake-up

1. First boot on the wake-up profile. Expect the reactor to drain the
   expired timers: watch the logs and the **count** of files landing
   in `var/mail-out/` (do not read bodies), and the
   `DummySMSService` withhold lines.
2. Run the evolution steps (`sdi evolve` equivalent); the rehearsal
   showed the chain is a NO-OP on this base — anything else is a stop
   signal.
3. Optional: full reindex; the rehearsal reference is *identical
   counts on all 61 indexes*.
4. Let the instance reach quiescence (mail-out stops growing).

## 5. Verification gates

- The application boots and serves; admin login works.
- Aggregate census matches the rehearsal figures for this base
  (records, classes, zero broken).
- Catalog queries answer; key listings render.
- `var/mail-out/` volume is plausible, then stable.

Any gate failing → stop, investigate, and if needed fall back (the
legacy instance is untouched).

## 6. Switch to the real profile

1. Edit `etc/production.ini`: remove/comment the wake-up block —
   real SMTP settings replace `pyramid_mailer.debug`, the real SMS
   service replaces the sink.
2. Restart; smoke-check one outbound mail on a controlled account.
3. Flip DNS/proxy to the new instance.

## 7. Rollback

Until the switch is validated: flip DNS/proxy back to the legacy
instance — it was never written to. Keep the repozo backup and the
extracted copies until the new instance has survived its first real
production cycle.

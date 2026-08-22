# Clean server deployment

This guide replaces the historical installation (everything under
`/home/admin`, processes launched by root, a frozen Docker image)
with a legible deployment: **a dedicated service account, never
root, code separated from data and configuration, systemd in
charge**. The shipped units live in `deploy/systemd/`.

## Principles

- **One service account per application**, with no login shell. The
  name `kuneagi` is recommended (one service, one account — should
  MESHS or another Zope application join the server one day, it gets
  its own); `zope` works identically if you hold to tradition: adapt
  `User=`/`Group=` in the units.
- **root launches nothing**: it installs the units and reads the
  journals. The processes run under the service account.
- **Code ≠ data ≠ configuration**: a code upgrade never touches
  `var/`, and `etc/` (which carries secrets) does not live in git.

## Layout

    /srv/kuneagi/
      app/        git clone of KuneAgi, at the PINNED head
                  (the venv lives in app/.venv312, made by bootstrap)
      var/        THE DATA: filestorage/, blobstorage/, mail-out/,
                  tmp_uploads/, log/ — exclusive property of the service
      etc/        production.ini, production-system.ini,
                  zeo-modern.conf, zodb-modern.conf — out of git, 0640
      backups/    repozo backups

The shipped ini files reference `%(here)s/../var` and the ZODB/ZEO
confs use `$INSTANCE = .`: with `WorkingDirectory=/srv/kuneagi` in
the units, everything resolves unmodified.

## Installation

    # 1. Account and layout (root)
    useradd --system --home-dir /srv/kuneagi --create-home \
            --shell /usr/sbin/nologin kuneagi
    install -d -o kuneagi -g kuneagi -m 750 \
            /srv/kuneagi/{app,var,etc,backups}

    # 2. The code, at the pinned head (as kuneagi)
    sudo -u kuneagi git clone https://github.com/michaellaunay/KuneAgi.git \
            /srv/kuneagi/app
    sudo -u kuneagi git -C /srv/kuneagi/app reset --hard <PINNED_SHA>
    sudo -u kuneagi bash -c 'cd /srv/kuneagi/app && bash tools/bootstrap-modern.sh'

    # 3. Data and configuration (from the migration delivery
    #    kuneagi-migre-YYYYMMDD: its var/ and etc/ drop in as-is)
    tar xzf kuneagi-migre-YYYYMMDD.tar.gz
    cp -a kuneagi-migre-YYYYMMDD/var/. /srv/kuneagi/var/
    cp -a kuneagi-migre-YYYYMMDD/etc/. /srv/kuneagi/etc/
    chown -R kuneagi:kuneagi /srv/kuneagi/var /srv/kuneagi/etc
    chmod 640 /srv/kuneagi/etc/*.ini

    # 4. systemd (root)
    cp /srv/kuneagi/app/deploy/systemd/*.service /etc/systemd/system/
    systemctl daemon-reload

## Two topologies

**A. Simple (small instance, one process).** The system process also
serves the web and carries the reactor; `zodbconn.uri` stays on
`file://` (as shipped). One process at a time on a FileStorage.

    systemctl enable --now kuneagi-system

> **Troubleshooting — lock held at startup.** A looping
> `LockError` on `Data.fs.lock` means another process holds the
> base (`fuser -v var/filestorage/Data.fs` names it). A
> FileStorage admits one process only: in topology A, ZEO and the
> web must be stopped (`systemctl mask kuneagi-zeo` forbids any
> resurrection through dependencies; `unmask` on topology-B day).
> Never delete the `.lock`: it dies with its holder.

**B. Faithful to the legacy (ZEO + web + system).** Switch
`zodbconn.uri` to `zconfig://%(here)s/zodb-modern.conf#main` in
**both** ini files, then:

    systemctl enable --now kuneagi-zeo kuneagi-web kuneagi-system

The web (port 6543, several threads) does not carry the reactor; the
system process (port 5002, a single worker) does — the era's
architecture, stripped of the pass-through encryption layer.

## Cohabiting with the old stack (until switchover)

The legacy container runs on the host network: it already holds,
on the loopback, port **5002** (its system process) and the
reactor socket **12345**. As long as it lives — and it must live
until victory, it is the rollback — the modern stack takes ports
of its own:

    # waitress port of the system process: 5003
    sed -i 's/^listen = 127.0.0.1:5002/listen = 127.0.0.1:5003/' \
        etc/production-system.ini
    # reactor socket: 12346 (drop-in, survives unit upgrades)
    mkdir -p /etc/systemd/system/kuneagi-system.service.d
    printf '[Service]\nEnvironment=DACE_SOCKET_URL=tcp://127.0.0.1:12346\n' \
        > /etc/systemd/system/kuneagi-system.service.d/cohabitation.conf
    systemctl daemon-reload

(`DACE_SOCKET_URL` requires dace at the "overridable socket"
fix level.) Point the frontend at 5003. After victory, keep these
ports — they are now the house's.

## First boot and switchover

The shipped inis are in **wake-up profile** (`novaideo.mail_debug =
true`: every outbound message drops into `var/mail-out/`). Watch the
journals (`journalctl -u kuneagi-system -f` — timer re-arming shows
at INFO) and `var/mail-out/`, then run the runbook switchover
(`docs/en/production-migration.md`, §6): `novaideo.mail_debug =
false`, real SMTP, real SMS service, restart, smoke test, DNS.

In front: nginx (or varnish) carries TLS and proxies to
`127.0.0.1:6543`; waitress reads the `X-Forwarded-*` headers.

## Operations

- **Journals**: `journalctl -u kuneagi-web -u kuneagi-system`.
- **Code upgrade**:

      sudo -u kuneagi git -C /srv/kuneagi/app fetch origin
      sudo -u kuneagi git -C /srv/kuneagi/app reset --hard <NEW_SHA>
      sudo -u kuneagi bash -c 'cd /srv/kuneagi/app && bash tools/bootstrap-modern.sh'
      systemctl restart kuneagi-system kuneagi-web

- **Backups** (daily, cron or systemd timer, kuneagi account):

      /srv/kuneagi/app/.venv312/bin/repozo -B -z \
          -r /srv/kuneagi/backups \
          -f /srv/kuneagi/var/filestorage/Data.fs

- **Hardening**: the units set `NoNewPrivileges`, `PrivateTmp`,
  `ProtectSystem=strict`, `ProtectHome` and only allow writes to
  `/srv/kuneagi/var`.

## Docker note

The legacy image (`ecreall/kuneagi:master`, Python 3.6) is retired.
A modern image remains open work (phase 5); this bare-metal + systemd
deployment is today's reference path.

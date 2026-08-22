# Déploiement propre sur serveur

Ce guide remplace l'installation historique (tout dans `/home/admin`,
processus lancés par root, image Docker figée) par un déploiement
lisible : **un compte de service dédié, jamais root, le code séparé
des données et de la configuration, systemd aux commandes**. Les
unités livrées vivent dans `deploy/systemd/`.

## Principes

- **Un compte de service par application**, sans shell de connexion.
  Le nom `kuneagi` est recommandé (un service, un compte — si un jour
  MESHS ou une autre application Zope rejoint le serveur, elle aura
  le sien) ; `zope` fonctionne à l'identique si la tradition vous est
  chère : adaptez `User=`/`Group=` dans les unités.
- **root ne lance rien** : il installe les unités et regarde les
  journaux. Les processus tournent sous le compte de service.
- **Code ≠ données ≠ configuration** : une mise à jour du code ne
  touche jamais `var/`, et `etc/` (qui porte des secrets) ne vit pas
  dans git.

## Arborescence

    /srv/kuneagi/
      app/        clone git de KuneAgi, à la tête ÉPINGLÉE
                  (le venv vit dans app/.venv312, créé par bootstrap)
      var/        LES DONNÉES : filestorage/, blobstorage/, mail-out/,
                  tmp_uploads/, log/ — propriété exclusive du service
      etc/        production.ini, production-system.ini,
                  zeo-modern.conf, zodb-modern.conf — hors git, 0640
      backups/    sauvegardes repozo

Les ini livrés référencent `%(here)s/../var` et les conf ZODB/ZEO
`$INSTANCE = .` : avec `WorkingDirectory=/srv/kuneagi` dans les
unités, tout se résout sans modification.

## Installation

    # 1. Le compte et l'arborescence (root)
    useradd --system --home-dir /srv/kuneagi --create-home \
            --shell /usr/sbin/nologin kuneagi
    install -d -o kuneagi -g kuneagi -m 750 \
            /srv/kuneagi/{app,var,etc,backups}

    # 2. Le code, à la tête épinglée (en tant que kuneagi)
    sudo -u kuneagi git clone https://github.com/michaellaunay/KuneAgi.git \
            /srv/kuneagi/app
    sudo -u kuneagi git -C /srv/kuneagi/app reset --hard <SHA_ÉPINGLÉ>
    sudo -u kuneagi bash -c 'cd /srv/kuneagi/app && bash tools/bootstrap-modern.sh'

    # 3. Les données et la configuration (depuis la livraison de
    #    migration kuneagi-migre-YYYYMMDD : son var/ et son etc/
    #    se déposent tels quels)
    tar xzf kuneagi-migre-YYYYMMDD.tar.gz
    cp -a kuneagi-migre-YYYYMMDD/var/. /srv/kuneagi/var/
    cp -a kuneagi-migre-YYYYMMDD/etc/. /srv/kuneagi/etc/
    chown -R kuneagi:kuneagi /srv/kuneagi/var /srv/kuneagi/etc
    chmod 640 /srv/kuneagi/etc/*.ini

    # 4. systemd (root)
    cp /srv/kuneagi/app/deploy/systemd/*.service /etc/systemd/system/
    systemctl daemon-reload

## Deux topologies

**A. Simple (petite instance, un seul processus).** Le processus
système sert aussi le web et porte le réacteur ; `zodbconn.uri` reste
en `file://` (tel que livré). Un seul processus à la fois sur un
FileStorage.

    systemctl enable --now kuneagi-system

> **Dépannage — verrou tenu au démarrage.** `LockError` sur
> `Data.fs.lock` en boucle = un autre processus tient la base
> (`fuser -v var/filestorage/Data.fs` le nomme). Un FileStorage
> n'admet qu'un processus : en topologie A, ZEO et le web doivent
> être arrêtés (`systemctl mask kuneagi-zeo` interdit toute
> résurrection par dépendance ; `unmask` le jour de la topologie
> B). Ne supprimez jamais le `.lock` : il meurt avec son
> détenteur.

**B. Fidèle au legacy (ZEO + web + système).** Passer `zodbconn.uri`
à `zconfig://%(here)s/zodb-modern.conf#main` dans **les deux** ini,
puis :

    systemctl enable --now kuneagi-zeo kuneagi-web kuneagi-system

Le web (port 6543, plusieurs threads) ne porte pas le réacteur ; le
système (port 5002, un seul worker) le porte — c'est l'architecture
d'époque, débarrassée de la couche de chiffrement passe-plat.

## Cohabitation avec l'ancienne pile (jusqu'à la bascule)

Le conteneur legacy tourne en réseau hôte : il tient déjà, sur le
loopback, le port **5002** (son processus système) et le socket du
réacteur **12345**. Tant qu'il vit — et il doit vivre jusqu'à la
victoire, c'est le rollback — la pile moderne prend des ports à
elle :

    # port waitress du processus système : 5003
    sed -i 's/^listen = 127.0.0.1:5002/listen = 127.0.0.1:5003/' \
        etc/production-system.ini
    # socket du réacteur : 12346 (drop-in, survit aux mises à jour d'unités)
    mkdir -p /etc/systemd/system/kuneagi-system.service.d
    printf '[Service]\nEnvironment=DACE_SOCKET_URL=tcp://127.0.0.1:12346\n' \
        > /etc/systemd/system/kuneagi-system.service.d/cohabitation.conf
    systemctl daemon-reload

(`DACE_SOCKET_URL` exige dace au niveau du correctif « socket
surchargeable ».) Pointer le frontal vers 5003. Après la victoire,
gardez ces ports — ils sont désormais ceux de la maison.

## Premier démarrage et bascule

Les ini livrés sont en **profil réveil** (`novaideo.mail_debug =
true` : tout courrier sortant tombe dans `var/mail-out/`). Contrôler
les journaux (`journalctl -u kuneagi-system -f` — le réarmement des
minuteries se voit à INFO) et `var/mail-out/`, puis dérouler la
bascule du runbook (`docs/fr/production-migration.md`, §6) :
`novaideo.mail_debug = false`, SMTP réel, service SMS réel,
redémarrage, fumée, DNS.

En frontal : nginx (ou varnish) porte le TLS et proxifie vers
`127.0.0.1:6543` ; waitress lit les en-têtes `X-Forwarded-*`.

## Exploitation

- **Journaux** : `journalctl -u kuneagi-web -u kuneagi-system`.
- **Mise à jour du code** :

      sudo -u kuneagi git -C /srv/kuneagi/app fetch origin
      sudo -u kuneagi git -C /srv/kuneagi/app reset --hard <NOUVEAU_SHA>
      sudo -u kuneagi bash -c 'cd /srv/kuneagi/app && bash tools/bootstrap-modern.sh'
      systemctl restart kuneagi-system kuneagi-web

- **Sauvegardes** (quotidien, cron ou timer systemd, compte kuneagi) :

      /srv/kuneagi/app/.venv312/bin/repozo -B -z \
          -r /srv/kuneagi/backups \
          -f /srv/kuneagi/var/filestorage/Data.fs

- **Durcissement** : les unités posent `NoNewPrivileges`,
  `PrivateTmp`, `ProtectSystem=strict`, `ProtectHome` et n'autorisent
  l'écriture que sur `/srv/kuneagi/var`.

## Note Docker

L'image legacy (`ecreall/kuneagi:master`, Python 3.6) est retirée du
service. Une image moderne reste un chantier ouvert (phase 5) ; ce
déploiement bare-metal + systemd est la voie de référence
aujourd'hui.

# Fil de l'eau

Journal au fil de l'eau des travaux sur ce dépôt, du plus récent au plus ancien.
English version: [`../en/worklog.md`](../en/worklog.md).

## 2026-07-13

- Fork de `ecreall/KuneAgi` vers `michaellaunay/KuneAgi` ; reprise de la
  maintenance par Michaël Launay (Logikascium). KuneAgi est le tronc de
  référence de la modernisation de Nova-Ideo (audit de juillet 2026).
- Conversion de `README.rst` et `CHANGES.rst` en Markdown ; README rebaptisé
  de « Nova Ideo » en « KuneAgi », réécrit avec le statut du dépôt (droits :
  Cosmopolitical.coop pour les développements propres à KuneAgi, Logikascium
  pour le socle Nova-Ideo ; AGPL v3+ pour l'ensemble) et la feuille de route ;
  instructions d'exploitation obsolètes annotées (« less secure apps » de
  Google, images Docker Hub historiques).
- Mise à jour des métadonnées de build (`setup.py` : URLs du fork, champ
  mainteneur, description longue en Markdown, classifieur Python 3.6) ; ajout
  d'un `pyproject.toml` minimal (PEP 518) ; mise à jour du `MANIFEST.in`. Nom
  du paquet `novaideo` et chemins de modules inchangés (pickles ZODB).
- `sources.cfg` : `ecreall_dace`, `ecreall_pontus`, `ecreall_daceui` repointés
  vers leurs forks maintenus. Point connu pour la phase 1 : `cryptacular`
  référence encore une URL Mercurial Bitbucket (service arrêté en 2020).
- Ajout d'un workflow de CI « smoke » (`python:3.6-buster` : `compileall` sur
  `novaideo` + vérification des métadonnées de packaging) ; le build legacy
  complet est le livrable de la phase 1.
- Exclusion des artefacts de livraison (`*.patch`, `*.diff`, archives) et des
  résidus de `git apply` via `.gitignore`.
- Mise en place de la structure de documentation bilingue (`docs/en`,
  `docs/fr`) et de ce fil de l'eau.
- Restauration des changements de maintenance du fork : le commit initial
  (8883913) ne contenait que le fichier de patch de livraison, *non
  appliqué* — la commande d'application référençait
  `../kuneagi-fork-maj.patch` alors que le fichier avait été enregistré dans
  le dépôt ; la chaîne `&&` s'est arrêtée au `--check` et le fichier orphelin
  a été commité seul. Le contenu du patch est désormais appliqué et le
  fichier orphelin supprimé (et ignoré à l'avenir).


## 2026-07-14

- Lancement du « golden master » applicatif (phase 1) : un nouveau workflow
  `golden-master` reconstruit l'image Docker historique (le Dockerfile
  exécute le buildout complet pendant le `docker build`, avec les
  épinglages d'époque que le projet portait déjà : setuptools 42,
  zc.buildout 2.13.3) puis rejoue `bin/test -s novaideo`.
- Correctifs d'époque appliqués au Dockerfile : sources apt de Debian
  stretch repointées vers archive.debian.org (stretch archivée) ; dépôt
  packagecloud varnish 4.1 rendu best-effort avec le varnish de la
  distribution en repli (la suite de tests n'utilise pas varnish) ;
  `cryptacular` préinstallé depuis sa réécriture 2.x maintenue — même
  mécanisme de préinstallation pip que l'image historique pour la 1.5.5 —
  avec `bcrypt`/`cffi`/`pycparser` épinglés dans `versions.cfg` ; la source
  Mercurial Bitbucket morte remplacée par le dépôt maintenu. Chantier
  itératif attendu, comme pour les CI des bibliothèques.
- Itération 1 du golden master (build local) : apt sur la stretch archivée
  télécharge bien mais `upgrade -y` refuse les paquets — les clés de
  signature de stretch ont *expiré* (EXPKEYSIG), et Check-Valid-Until ne
  neutralise que le contrôle de date du Release, pas la vérification de
  signature. Les sources d'archive sont désormais marquées `[trusted=yes]`
  (compromis assumé et documenté pour une CI legacy figée). Montée
  préventive de pip en <22 dans l'image : le pip 19 de stretch est
  antérieur aux tags manylinux2014 des wheels bcrypt/cffi.
- Alignement complet sur Docker Compose v2 (`docker compose`) : correction
  de `run.sh`, où un remplacement global antérieur avait aussi mangé le
  *nom de fichier* (`-f docker compose-dev.yml`), cassant toutes les
  commandes enveloppées ; cible de l'attach rendue indépendante du nommage
  via `docker compose ps -q` (v2 nomme les conteneurs avec des tirets, pas
  des tirets bas) ; conversion des commandes `docker-compose` restantes du
  README ; suppression de l'attribut obsolète `version: '2'` des quatre
  fichiers compose (v2 le signale en avertissement).
- Itération 2 du golden master : `./run.sh rebuild` construit l'image avec
  `run_buildout=false` (le buildout doit tourner ensuite, hors build, avec
  le volume de cache monté), mais la ligne historique
  `RUN $run_buildout && bin/buildout` court-circuite en exit 1 quand
  l'argument vaut false — le `|| true` qui la rendait viable avait été
  commenté. Remplacée par un `if` explicite, qui garde aussi fatals les
  vrais échecs de buildout quand l'argument vaut true (le chemin du
  workflow golden-master). Correction du piège suivant dans
  `do_buildout()` : le nom d'image par défaut utilisait encore le nommage
  v1 à tiret bas (`kuneagi_novaideo`) — v2 construit `kuneagi-novaideo`.
- Itération 3 du golden master, et le jalon qui va avec : **le buildout
  complet de l'application est passé** — 194 épinglages, checkouts
  mr.developer, cryptacular 2.0 — première reconstruction intégrale depuis
  mars 2023. L'échec restant était dans l'étape de copie du cache de
  `run.sh`, un idiome docker de 2016 : `docker run -i -a stdin` (sans `-d`)
  imprimait l'id du conteneur sur stdout ; le docker moderne n'imprime rien
  dans ce mode, laissant `$id` vide (« invalid container name or ID: value
  is empty », puis l'erreur bash `test` ligne 27). Remplacé par une paire
  explicite `docker create` / `docker start -i -a`, sémantique identique
  (tar streamé vers un conteneur u1000, propriété des fichiers préservée).

- Extracteur BPMN→mermaid (`tools/bpmn2mermaid.py`, `ast` de la stdlib,
  tourne en 3.6 et 3.12) : analyse statiquement tous les
  `definition.py` (aucun import du moteur nécessaire) et génère une page
  Markdown par module de définition — flowchart mermaid par processus
  (formes façon BPMN : événements en cercles, passerelles XOR/AND en
  losanges, sous-processus en sous-routines avec leur définition cible,
  timers/conditionnels avec leur callable d'échéance/prédicat,
  conditions et `sync` en étiquettes d'arêtes) plus une table
  nœuds/behaviors. 38 modules de définition, 43 processus extraits sous
  `docs/en/processes/` et `docs/fr/processes/` (index compris). Les
  diagrammes montrent les graphes tels qu'écrits ; la normalisation du
  moteur peut ajouter un câblage synthétique. Le sous-processus de
  travail composé à l'exécution est étiqueté `(dynamic)`.

- Patch de caractérisation des cinq échecs du golden master (tous dans
  `TestIdeaManagement`). Deux causes racines, toutes deux des
  **évolutions fonctionnelles, pas des régressions** : (1) la
  modération individuelle de 2017 (un Moderator pressant
  publish_moderation/archive sur une idée 'submitted') a été remplacée
  par la *modération communautaire* — `SubmitIdea.start` tire jusqu'à
  ELECTORS_NB (3) membres actifs au hasard (auteur exclu ;
  `get_random_users` retourne *tous* les disponibles s'ils sont moins
  de 3) et ouvre un scrutin 'ideamoderation', avec un repli explicite :
  aucun électeur éligible, publication immédiate. Le bac à sable ne
  contient aucun membre hors l'auteur : le repli se déclenchait
  toujours. (2) la fusion du vocabulaire du site qu'affirmaient les
  tests create_and_publish passe par le `_tree` de l'idée
  (`root.merge_tree`) depuis que la migration keywords→tree (63a01248,
  2016-11) s'est achevée — l'argument plat `keywords=` du constructeur
  ne l'alimente plus.
- Les quatre tests de modération gardent leurs noms et photographient
  désormais le repli (paire d'états, `published_at`, absence des nœuds
  de décision, substitution 'moderationarchive') ; les ensembles
  d'actions exacts sont remplacés par des sous-ensembles
  indispensables, à resserrer une fois au vert. Un test nouveau,
  `test_submit_idea_moderation_conf_with_electors`, photographie le
  chemin nominal : trois membres ajoutés, l'idée reste 'submitted' et
  gagne une entrée `ballot_processes`.
- Note d'archéologie : le mécanisme a pris forme depuis 202a2849
  (30/11/2016, « adapt moderation ») jusqu'à l'ère KuneAgi ; les tests
  de mai 2017 décrivent le flux antérieur.

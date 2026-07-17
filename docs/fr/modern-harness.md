# Le harnais moderne (Python 3.12)

*Compagnon de la phase 3. English version: [`../en/modern-harness.md`](../en/modern-harness.md).*

Trois étages, tous versionnés :

1. **Les harnais de test** (`novaideo/testing.py` et le `testing.py` de
   chaque bibliothèque) sont bi-pile : ils empruntent d'abord le chemin
   historique, et ne se replient (mailer direct, stockage frais) que
   sur le conflit de configuration moderne. Le même arbre de travail
   sert les deux piles.
2. **Les runs isolés et reproductibles** : chaque dépôt embarque
   `tox.ini` + `constraints-modern.txt` + un workflow `py312-tests` —
   ce que la CI exécute, en installant le trio depuis ses masters git.
3. **L'environnement de développement intégré** — ce document. Pour le
   travail inter-dépôts (le quotidien de M5 et au-delà), les installs
   git de tox ne conviennent pas : il faut les checkouts frères en
   *editable*. C'est ce que reconstruit `tools/bootstrap-modern.sh` :

```bash
git clone git@github.com:michaellaunay/dace.git
git clone git@github.com:michaellaunay/pontus.git
git clone git@github.com:michaellaunay/daceui.git
git clone git@github.com:michaellaunay/KuneAgi.git
cd KuneAgi
tools/bootstrap-modern.sh
.venv312/bin/python -m zope.testrunner --test-path=. -s novaideo
```

Frères présents → installs editable ; absents → masters git. Le script
se clôt sur `tools/patch_graphql1_py312.py` (le schéma GraphQL est
d'ère graphene 1 ; l'outil porte la pile d'époque installée —
idempotent).

Le jumeau legacy est inchangé : `./run.sh test -s novaideo` lance le
conteneur certifié de 2017. Les deux doivent rester verts.

## Durcissement (réparation CI, 16/07/2026)

Un résolveur à froid sur les runners a exposé ce que les venvs au long
cours masquaient ; la discipline d'installation est désormais :

- **chaque** ligne pip tourne sous `constraints-modern.txt` (dérive
  amont muselée — ex. substanced `1.0.post1` tirant pyramid 2.1) ;
- `graphql-wsgi` se demande **par nom nu** : la contrainte porte l'URL
  source épinglée (demander l'URL directement entre en conflit avec la
  contrainte au sha) ;
- la pile graphene d'époque s'installe explicitement
  (`graphene==1.4.2 graphql-core==1.1 graphql-relay==0.4.5`, promise
  à son pin d'époque `2.0.2`), puis `tools/patch_graphql1_py312.py`
  la porte **en place — promise compris** ;
- les paquets à porter se localisent via `sysconfig` **sans les
  importer** (l'import crashe avant portage : paradoxe d'amorçage) ;
- `lxml` est un requirement déclaré de `novaideo` (parseur de bs4) ;
- côté legacy, `graphql-wsgi` figure aux requires
  **conditionnellement** (`sys.version_info < (3,7)`) : ce requirement
  est ce qui fait trouver au buildout son egg d'époque dans le cache.

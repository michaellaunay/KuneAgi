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

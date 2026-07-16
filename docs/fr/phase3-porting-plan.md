# Phase 3 — plan de portage (Python 3.12)

*Adopté le 16/07/2026, jour de la certification du golden master (29/29 sur la pile 2017 reconstruite). Chaque étape de ce plan se mesure contre cette suite. English version: [`../en/phase3-porting-plan.md`](../en/phase3-porting-plan.md).*

## 1. Objectif et non-négociables

Porter toute la pile — `dace`, `pontus`, `daceui`, `novaideo`/KuneAgi — sur **Python 3.12** avec des dépendances maintenues, à comportement identique.

Non-négociables :

1. **Parité comportementale.** La suite de 29 tests est l'arbitre : elle reste verte sur le conteneur legacy à chaque étape, et le portage est *terminé* quand la même suite est verte en 3.12 (jalon M4). Les divergences sont des faits à caractériser, jamais des opinions.
2. **Continuité ZODB.** Les bases existantes doivent continuer de se charger. Les classes persistantes gardent leurs chemins de module et leurs noms — le nom du paquet `novaideo` est déjà gelé pour cette raison précise, et la règle s'étend désormais aux bibliothèques : **une classe persistante ne bouge jamais**. Conséquence mesurée : `dace.processdefinition.core.Transaction` et `Path` dérivent de `Persistent` et sont stockées sur chaque processus (`global_transaction`) ; le renommage un temps envisagé `Transaction → PathTransaction` est donc **rejeté** — la désambiguïsation vit dans la documentation (phase 2).
3. La documentation bilingue et les fils de l'eau par dépôt continuent ; les conventions des phases 1–2 (patchs via `git apply`, code en anglais, `docker compose` v2) sont inchangées.
4. AGPL v3 ; attribution amont (Ecréall, Nova-Ideo) préservée.

## 2. L'instrument de mesure (tests bi-pile)

- **Legacy** : le conteneur certifié — `./run.sh test -s novaideo` et le workflow GitHub `golden-master`. Il ne casse jamais ; c'est le certificat.
- **Moderne** : par dépôt, un environnement tox `py312` et un job de CI, nés *autorisés à échouer* et promus *requis* à chaque jalon.
- **Une variable à la fois** : le même lanceur de tests (`zope.testrunner`) sur les deux piles jusqu'à M4 ; la migration pytest est un confort post-M4, pas un prérequis du portage.
- Point de départ, mesuré le 16/07/2026 : les quatre bases de code **compilent déjà en Python 3.12.3** (`compileall` propre ; une poignée de `SyntaxWarning: invalid escape sequence` dans des regex à passer en raw strings à M0).

## 3. Pile actuelle vs pile cible

| Composant | Pin 2017 | Cible | Notes |
|---|---|---|---|
| Python | 3.6.15 | **3.12** | la syntaxe compile déjà (voir §2) |
| pyramid | 1.9.1 | 2.0.x | authn/authz fusionnés dans la security policy ; `pyramid.compat` disparu |
| substanced | 1.0a1 (egg) | **fork `michaellaunay/substanced`** | amont dormant ; ne porter que la *surface utilisée* (annexe A) |
| ZODB / persistent / BTrees / transaction | 5.3.0 / 4.2.4 / 4.4.1 / 2.1.2 | 6.x / 6.x / 6.x / 4.x | API stable, compatible pickle |
| hypatia | 0.3 | 0.4+ | vendorer si dormant en 3.12 |
| deform / colander | 2.0a2 / 1.0 | 2.0.15 / 2.x | pontus possède ses templates de widgets (carte de la phase 2) ; passe de diff à M2 |
| Chameleon | 3.1 | 4.x | rigueur des templates vérifiée tôt (M2) |
| pyzmq / tornado | 14.4.1 / 3.2.2 | 26.x / **supprimé** | le réacteur passe à asyncio (§4) |
| venusian | 1.1.0 | 3.x | API de scan stable |
| rwproperty | 1.0 | **supprimé** | amont mort ; remplacé par des propriétés ordinaires |
| waitress | 1.1.0 | 3.x | |
| zc.buildout + mr.developer | 2.13.3 | **pip + pyproject** | `constraints-modern.txt` en miroir de `constraints-legacy.txt` ; checkouts frères via `pip install -e ../dace` |
| cryptacular | fork 2.0 | inchangé | déjà moderne (phase 1, parité octet pour octet prouvée) |

## 4. Le réacteur — l'unique changement d'architecture

Aujourd'hui (dace) : un fil `IOLoop` tornado, réveillé par une socket de commande zmq PUSH/PULL (`tcp://127.0.0.1:12345`), des timers `DelayedCallback`, et des `Job`/`EventJob` qui rétablissent site et utilisateur à chaque exécution, armés *après commit*.

Cible : **la même API publique** — `push_event_callback_after_commit`, `push_callback_after_commit`, `DelayedCallback.start/stop`, `Job`, `EventJob` — au-dessus d'un fil de boucle **asyncio**.

- **Étape A (transport conservé, incluse dans M1)** : garder la socket de commande zmq (pyzmq 26 fournit `zmq.asyncio`) ; remplacer l'IOLoop par `asyncio.new_event_loop()` dans le fil du réacteur ; `DelayedCallback` devient une fine enveloppe de `loop.call_later`.
- **Étape B (optionnelle, post-M4)** : abandonner zmq pour `asyncio.run_coroutine_threadsafe` + une file — la réalité d'aujourd'hui est mono-processus.

Spécification de parité : les docstrings de la phase 2 font office de spec — cadence du crawler (réarmement 2 s), repoll 1 s des `ConditionalEvent`, ordre d'armement après commit, unique retentative sur `ConflictError`, rétablissement site/utilisateur. M1 ajoute un petit test de timing pour les deux premiers.

## 5. Ordre de bataille (étrangleur, de bas en haut)

- **M0 — échafaudage** (tous dépôts) : extra `[modern]` + `constraints-modern.txt` ; tox `py312` ; job CI *autorisé à échouer* ; raw strings sur les avertissements d'échappement ; balayage statique (`pyupgrade --py312` **avec relecture — jamais de réécriture automatique d'une classe persistante**, triage `ruff`) produisant la liste des reliquats py2.
- **M1 — dace vert en 3.12** (88 tests) : échelle de dépendances (zope.interface → persistent/BTrees/ZODB → transaction → hypatia), fork substanced amorcé avec la surface de l'annexe A, étape A du réacteur, les trois monkey-patches de `patches.py` réévalués un à un (chacun a sa docstring de phase 2 qui dit pourquoi il existe).
- **M2 — pontus vert en 3.12** : deform 2.0.15 / colander 2 (diff des templates de widgets), `substanced.form`/`file` depuis le fork, et le reliquat py2 confirmé corrigé : `view_operation.py:724-726` indexe `dict.items()` — inatteignable par la suite (planterait sur tout Python 3), à corriger-ou-supprimer *avec un test*.
- **M3 — daceui vert en 3.12.**
- **M4 — KuneAgi 29/29 en 3.12** : balayage applicatif, buildout → pip, passe templates/statiques, `constraints-modern.txt` gelé. **Acceptation : les mêmes 29 tests, `zope.testrunner`, 0 échec 0 erreur en 3.12 — avec le conteneur legacy toujours vert.**
- **M5 — répétition de migration de données** : une copie d'un `Data.fs` d'époque ouverte sur la pile moderne — chaîne d'evolve, `zeopack`, réindexation, parcours manuel ; le mode opératoire écrit dans `docs/`.
- **Fenêtre post-M4** (changements d'API, *non persistés uniquement*, chaque candidat audité côté pickle d'abord) : `action_infomrations → action_informations` (méthode, sûre, shim gardé une version) ; noms de ressources pontus `Mutltiple*` (exposés au JS — renommage coordonné) ; paramètre `nember` ; `InclusiveGatewayDefinition` : implémenter ou supprimer (recommandation : supprimer, lever explicitement) ; boundary events : documentés comme non supportés (FIXME du runtime).

## 6. Registre des risques

1. **Dérive de périmètre du fork substanced** → liste de surface de l'annexe A ; portage à la demande, rien de spéculatif.
2. **Casse des pickles ZODB** → la règle du jamais-bouger ; essais à blanc `zodbupdate` à M5 ; renommages seulement après audit pickle.
3. **Dérive des templates deform/colander** → les templates de pontus sont inventoriés (phase 2) ; M2 fait une passe de diff visuel.
4. **Dormance d'hypatia** → repli vendoring, même licence.
5. **Reliquats py2 latents** (la famille `.items()[...]`) → balayage statique à M0 ; chaque trouvaille devient correction-plus-test ou code-mort-documenté.
6. **Parité de timing du réacteur** → spec par docstrings + test de timing à M1.
7. **Rigueur de Chameleon 4** → passe de compilation des templates à M2, pas à M4.
8. **Chaîne d'evolve inexercée** depuis les bases d'époque → répétition M5 sur une copie réelle.

## Annexe A — la surface substanced réellement utilisée (mesurée le 16/07/2026)

dace : `catalog` (`oid_from_resource`, câblage des catalogues), `content` (`content`), `db` (`root_factory`), `event` (`ObjectModified`, `RootAdded`, `subscribe_removed`), `folder` (`Folder`), `interfaces` (`IFolder`, `IRoot`, `IPrincipal`, `IService`, `IUserLocator`), `locking` (`lock_resource`), `objectmap` (`ObjectMap`, `find_objectmap`), `principal` (`DefaultUserLocator`, `User`), `property` (`PropertySheet`), `root` (`Root`), `schema` (`Schema`), `sdi` (`LEFT`, `mgmt_view`), `util` (`find_catalogs`, `find_objectmap`, `is_service`, `set_oid`, utilitaires).

pontus et daceui ajoutent : `file` (+ `file.views`), `form`, plus les partagés `content`/`db`/`schema`/`util`/`interfaces`.

À régénérer avec :

```bash
grep -rhoE "from substanced[.a-z_]* import [a-zA-Z_, ()]+" <pkg> --include="*.py" | sort -u
```

## Annexe B — liste de démarrage M0/M1

1. dace : extra `[modern]` dans `pyproject` + `constraints-modern.txt` (cibles du §3) ; tox `py312` ; job CI (autorisé à échouer).
2. Raw strings sur les avertissements d'échappement regex (trois fichiers dans novaideo, aucun dans les bibliothèques).
3. Amorcer le fork substanced : importer les modules de l'annexe A, supprimer le reste, faire résoudre la surface d'import de `dace`.
4. Échelle de dépendances jusqu'à ce que `zope.testrunner -s dace` collecte ; puis corriger en avançant, test par test.
5. Étape A du réacteur derrière la même API ; test de timing crawler/repoll.
6. Fil de l'eau à chaque session ; la CI legacy reste verte de bout en bout.

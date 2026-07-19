# Audit et plan de modernisation — Nova-Ideo, DaCE, Pontus, DaceUI

**Pour :** Logikascium EURL — **Audit initial :** 13 juillet 2026 —
**Révision 5 :** 18 juillet 2026
**Méthode :** clonage complet et analyse statique des 5 dépôts
`github.com/ecreall/{nova-ideo, KuneAgi, dace, pontus, daceui}`
(historique git, volumétrie, dépendances déclarées et figées, branches,
état des paquets amont sur PyPI). L'article de présentation (Ecréall,
éd. 57) a servi de référence fonctionnelle. Limites de l'audit
initial : pas d'exécution du code ni d'audit de données de production ;
les constats runtime restaient à confirmer en phase 1.

**Révision 5 — mise à jour d'exécution.** Entre le 13 et le 18 juillet
2026, les phases 0 à 3 et l'essentiel de la phase 5 ont été
**exécutées** ; les limites de l'audit initial sont levées (le code a
tourné, une vraie copie de production a été examinée). Chaque constat
(§4), chaque risque (§5) et chaque phase (§6) porte désormais son
**statut**, et le document entre au dépôt (`docs/fr`, `docs/en`).
Révisions antérieures : r2-r3 (préconisations frontend), r4 (glossaire
pour lecteur non informaticien, choix SolidJS, clarifications de
propriété intellectuelle).

**Lecteur non technique :** un glossaire des termes employés figure en
fin de document (§9).

---

## 1. Synthèse exécutive

L'écosystème est **cohérent, ambitieux et bien architecturé pour son
époque (2015-2019)**, mais il est aujourd'hui figé sur une pile de
2017 : Python 3.6 (EOL déc. 2021), Pyramid 1.9.1, substanced 1.0a1,
ZODB 5.3, graphene 1.4, Bootstrap 3/jQuery, buildout. **Le build ne
fonctionne plus en l'état** (les sources git utilisent le protocole
`git://`, désactivé par GitHub en 2022). La tentative React (branche
`nova-ideo-react`, arrêtée en janvier 2019) est trop datée pour être
reprise telle quelle, mais constitue une excellente spécification UX.

Les trois verrous stratégiques sont :

1. **substanced/hypatia**, socle de tout l'édifice, effectivement
   orphelin (voir §4.2) → à forker/vendoriser sous gouvernance
   Logikascium ;
2. **le moteur d'événements de DaCE** (tornado < 4 + pyzmq, code de
   2015) → à réécrire sur asyncio, c'est le chantier technique le plus
   délicat ;
3. **la perte de connaissance** (le développeur principal a quitté le
   projet en 2019, ~85 % des commits) → la phase de documentation que
   tu prévois n'est pas un luxe, c'est la mitigation du risque n° 1.

La démarche que tu proposes (audit → documentation → mise à jour) est
la bonne, avec un ajout indispensable entre les deux : **reconstruire
un build legacy reproductible** qui servira d'étalon de non-régression
avant de toucher au code.

Estimation globale pour une v2 à parité fonctionnelle sur pile 2026 :
**5 à 9 mois** de travail effectif pour un développeur expérimenté
assisté par LLM, découpables en jalons livrables indépendamment
(détail §7).

> **Mise à jour (18/07/2026).** Le diagnostic ci-dessus s'est vérifié
> point par point — et le plan a été exécuté bien au-delà des
> prévisions. État des lieux : les deux builds (legacy et moderne)
> sont reconstruits et sous CI ; le **golden master est certifié
> 29/29** sur la pile 2017 reconstruite **et** sur Python 3.12 ; la
> suite de tests est passée de 29 à **128 tests de caractérisation**
> (les cinq familles du contrat social de la plateforme et les deux
> scrutins de modération conduits jusqu'à leur verdict) ; **quatre
> bugs latents et une régression de modernisation** ont été trouvés,
> corrigés, et chaque réparation est gardée par son test retourné en
> conscience ; la documentation bilingue couvre l'écosystème (43
> processus en pages générées, harnais, runbooks) ; une **répétition
> de migration a RÉUSSI sur une vraie copie de production** (79 269
> enregistrements, 381 classes, zéro cassé) et le runbook de
> production est prêt. Les verrous n° 2 et 3 sont levés pour
> l'essentiel (réacteur : étape A asyncio faite à API constante, étape
> B — retrait de zmq — restante ; connaissance : re-documentée et
> épinglée par les tests). Le verrou n° 1 (substanced) est **contourné
> mais pas levé** : la pile moderne tient sur l'amont 1.0b1 avec
> Pyramid maintenu en 1.10.8 ; le fork élagué pour Pyramid 2 reste le
> chantier structurant à venir.

---

## 2. Inventaire des dépôts (constaté)

| Dépôt | Rôle | Dernier commit | Commits | Volumétrie Python | Tests |
|---|---|---|---|---|---|
| **nova-ideo** | Application d'innovation participative | 2020-03-28 | 2 392 | 517 fichiers / 71 675 lignes + **439 templates Chameleon (.pt)** | 9 fichiers + suite Robot Framework |
| **KuneAgi** | Variante (gouvernance coopérative : scrutins, citoyenneté, courriels) | **2023-03-02** | 2 195 | 538 fichiers / 81 519 lignes | idem nova-ideo |
| **dace** | Moteur de workflow data-centric (activités, gateways, événements BPMN-like) | 2017-12-19 | 564 | 79 fichiers / 13 792 lignes | 19 fichiers — le mieux testé |
| **pontus** | Couche vues/formulaires (Pyramid + deform) au-dessus de DaCE | 2018-01-15 | 429 | 23 fichiers / 4 317 lignes | 5 fichiers |
| **daceui** | Composants UI de DaCE (panneaux d'actions, historique de processus) | 2018-12-21 | 54 | 8 fichiers / 1 743 lignes | **0** |

Structure applicative de nova-ideo : ~30 types de contenu (`idea`,
`proposal`, `amendment`, `ballot`, `challenge`, `working_group`,
`token`…), **24 paquets de processus métier** (92 fichiers de
définitions DaCE), 286 fichiers de vues, un module GraphQL backend
(~1 200 lignes, graphene 1.4). Traductions : source en anglais + fr
(KuneAgi ajoute l'allemand, 2022).

**Contributeurs** (pertinent pour la question de propriété
intellectuelle) : Amen Souissi ~85 % des commits, puis Vincent Fretin,
Cédric Messiant, Sophie Jazwiecki, toi, et 1 commit externe (Antoine
Cezar) + Dependabot. Tous salariés/collaborateurs Ecréall à l'époque →
le rachat de la PI par Logikascium couvre l'essentiel ; la part
externe est négligeable mais reste sous AGPL v3 (sans conséquence si
tu conserves la licence, point à vérifier avec ton conseil si tu
envisages un jour une double licence).

### 2.1 nova-ideo vs KuneAgi

KuneAgi n'est **pas** un simple fork gelé : c'est la branche la plus
récente de la lignée (14 commits entre 2020 et mars 2023 : mailer/SPF,
Dockerfile, traductions, corrections de scrutins), avec un périmètre
fonctionnel élargi (processus de vote, citoyenneté). nova-ideo master
s'arrête en mars 2020 mais possède les branches d'exploration
(`nova-ideo-react`, `realtime`, `to-apollo2`) absentes de KuneAgi.

**Recommandation :** prendre **KuneAgi comme tronc fonctionnel de
référence** pour la modernisation, produire un diff systématique avec
nova-ideo master pour identifier ce qui doit être réunifié, et viser à
terme **un seul code base** avec les spécificités KuneAgi en profils
de configuration plutôt qu'en fork. Maintenir deux jumeaux de 80 000
lignes n'est pas soutenable.

> **Mise à jour (18/07/2026).** Recommandation appliquée et affinée
> par la mesure. Le travail vit sur les forks
> `github.com/michaellaunay/{dace,pontus,daceui,KuneAgi}` ; le diff
> systématique nova-ideo ↔ KuneAgi a été produit et son verdict est
> net : depuis la scission de fin 2016, les deux lignes ont co-évolué
> (1 135 fichiers touchés des deux côtés) et **neuf fichiers
> seulement** sont propres à nova-ideo 2016-2020 (catalogués pour
> arbitrage). La réunification prend donc la forme d'une **adoption** :
> nova-ideo 2.0 = le tronc modernisé, l'histoire 2010-2020 cousue en
> parent. Côté généalogie git, les têtes `ecreall` de dace/pontus/
> daceui sont des ancêtres directs des forks (merge-back = avance
> rapide pure) ; KuneAgi et nova-ideo recevront chacun une couture
> d'adoption. Les merge-backs sont planifiés au jalon v2.0.0
> (post-validation de la migration de production).

---

## 3. Architecture actuelle (telle que lue dans le code)

```
┌────────────────────────────────────────────────────────┐
│ novaideo / KuneAgi (application)                       │
│  content/ (~30 types) · content/processes/ (24 paquets)│
│  views/ (286 fichiers) · graphql/ · mail/ · connectors/│
├────────────────────────────────────────────────────────┤
│ daceui (rendu des actions/processus)                   │
│ pontus (vues composables, formulaires deform/colander) │
├────────────────────────────────────────────────────────┤
│ dace : moteur de processus                             │
│  processdefinition/ · processinstance/ · catalog/      │
│  objectofcollaboration/ · system.py (processus système)│
│  boucle d'événements : tornado<4 + pyzmq (timers,      │
│  événements conditionnels) · patches.py (monkey-patch) │
├────────────────────────────────────────────────────────┤
│ substanced 1.0a1 (arbre de ressources, catalogue       │
│ hypatia, principals, evolve) · Pyramid 1.9.1 · ZODB 5.3│
└────────────────────────────────────────────────────────┘
```

Points saillants :

- **Tout repose sur substanced** (les quatre couches l'importent).
  C'est le choix structurant de 2014 et le pivot de la migration.
- **DaCE embarque sa propre boucle d'événements** (tornado 3 + zmq)
  pour les événements temporels/conditionnels et les « processus
  système » — du code d'infrastructure de 2015 qu'aucune dépendance
  moderne ne remplacera à l'identique. `dace/patches.py` contient des
  monkey-patches non documentés : à cartographier en priorité en phase
  de documentation.
- **Frontend master** : rendu serveur Chameleon + jQuery/Bootstrap 3,
  bundlé avec gulp 3/browserify/babelify (chaîne 2015, non
  reconstructible sur un Node moderne sans effort), éditeur draft-js.
- **Branche `nova-ideo-react`** (dernier commit 29/01/2019) : vraie
  SPA de 386 fichiers JS/JSX — React 16, Redux, react-apollo 2,
  Storybook, mais avec **material-ui 0.20 et @material-ui/core 3.7
  mélangés**, ainsi que react-router 3 et 4 simultanément. C'est un
  chantier interrompu en pleine transition interne. Sept ans plus
  tard, le rattrapage coûterait plus cher qu'une réécriture ; en
  revanche les composants, les requêtes GraphQL et les flux UX qu'elle
  contient sont une **spécification exploitable**.
- **API GraphQL backend** réelle mais partielle (graphene 1.4 + fork
  `ecreall/graphql-wsgi`), pensée pour cette SPA et le temps réel
  (branche `realtime`).

> **Mise à jour (18/07/2026).** L'architecture est inchangée dans sa
> structure — c'était le but : la modernisation est **bi-pile**, le
> même arbre de travail tourne sur la pile 2017 reconstruite et sur
> Python 3.12. Deux évolutions internes : la boucle d'événements de
> DaCE tourne désormais sur **asyncio** (étape A, à API constante —
> tornado retiré, zmq encore présent jusqu'à l'étape B), et les
> monkey-patches ainsi que le protocole d'événements sont documentés
> (phase 2). Fait d'architecture consigné par les tests : **les nœuds
> de décision des scrutins de modération se terminent à l'échéance**
> (sous-processus fermés par minuterie) — à connaître pour
> l'exploitation comme pour toute future migration de moteur.

---

## 4. Constats détaillés

### 4.1 Obsolescence du socle d'exécution

Versions figées dans `versions.cfg` (194 épinglages) : pyramid 1.9.1,
substanced 1.0a1, ZODB 5.3.0, deform 2.0a2 (fork `amensouissi/deform`),
colander 1.0, hypatia 0.3, graphene 1.4, BTrees 4.4.1, waitress 1.1.0,
gunicorn 19.7.1, Babel 2.3.4. L'image Docker est épinglée par SHA sur
**python:3.6-stretch** — Python 3.6 est EOL depuis décembre 2021 et
Debian stretch depuis 2022 : plus aucun correctif de sécurité, ni
interpréteur, ni OS, ni dépendances (waitress 1.1 et gunicorn 19.7 ont
des CVE connues, entre autres). Une passe `pip-audit` chiffrée est à
faire dès que le build est reproductible, mais le verdict global est
acquis d'avance : tout l'environnement est hors support.

> **Statut : RÉSOLU pour la pile moderne.** Le même arbre tourne sur
> Python 3.12 avec des dépendances contemporaines sous contraintes ;
> la pile 2017 n'est conservée que comme golden master (conteneur
> isolé, jamais exposé).

### 4.2 Le cas substanced — décision structurante

Fait vérifié ce jour : substanced a publié une **1.0b1 sur PyPI le
28/11/2024** (et hypatia 0.5 le 27/11/2024). Attention à la fausse
bonne nouvelle : les métadonnées de cette 1.0b1 annoncent toujours
Python 2.7–3.5 et des dépendances de test `nose`, `cryptacular`,
`lingua<2.0`. Il s'agit d'une re-publication de maintenance, pas d'une
modernisation — le projet n'a ni release stable en 12 ans ni feuille
de route. Il faut le traiter comme une **dépendance orpheline dont
Logikascium devient le mainteneur de fait**.

Deux options réalistes :

- **A (recommandée) : fork interne élagué.** Vendoriser substanced +
  hypatia dans un paquet maintenu par Logikascium, réduit aux modules
  réellement utilisés (arbre de ressources/objectmap, catalogue,
  principals, evolve, folder, property sheets), porté sur Python
  3.12/Pyramid 2. Effort initial significatif mais borné (le code est
  stable et bien écrit), et tu contrôles ensuite ton destin.
- **B : re-plateformer la persistance (SQL/Postgres).** À écarter pour
  la v2 : le modèle DaCE est un graphe d'objets + catalogue,
  profondément couplé à ZODB/substanced ; ce serait une réécriture,
  pas une migration. À réévaluer éventuellement en v3 si des besoins
  d'exploitation SaaS l'exigent (l'option intermédiaire
  RelStorage/Postgres comme backend ZODB couvre déjà beaucoup de
  besoins ops sans toucher au code).

> **Statut : CONTOURNÉ, chantier restant.** La pile moderne tient sur
> l'amont git 1.0b1 avec quelques shims d'une ligne et **Pyramid
> maintenu en 1.10.8** ; une régression de l'API mot de passe entre
> générations a été découverte par la campagne de tests et corrigée en
> bi-pile. L'option A (fork élagué porté Pyramid 2) reste la décision
> recommandée et le principal chantier structurant à venir.

### 4.3 Le build est cassé (et c'est réparable en quelques heures)

`sources.cfg` référence ~20 dépôts en `git://github.com/...` : GitHub
a désactivé ce protocole en mars 2022, donc **le buildout ne peut plus
cloner ses sources aujourd'hui**. Réparation triviale (`git://` →
`https://`), mais elle révèle le vrai sujet : le projet dépend d'une
**constellation de forks Ecréall/personnels** (deform fork, velruse
fork, graphql-wsgi, keas.kmi, cipher.encryptingstorage, yampy2,
html_diff_wrapper, deform_treepy, pyramid-sms…) hébergés sur des
comptes qui ne sont plus sous ton contrôle (`amensouissi/*`,
`vincentfretin/*`) ou l'organisation ecreall. **Chaque fork non
rapatrié est un point de défaillance.** Par ailleurs les paquets PyPI
`ecreall_dace/pontus/daceui` datent de février 2017 (1.1.0/1.0.4) — le
code git a évolué après, donc PyPI ne reflète pas l'état réel.

> **Statut : RÉSOLU.** Le build legacy est reconstruit et rejoué en CI
> (golden master) ; la constellation est rapatriée : **cryptacular
> 2.0** republié (parité octet-pour-octet avec le module déployé),
> `html_diff_wrapper` forké et corrigé, `graphql-wsgi` épinglé par sha
> et rendu conditionnel à la pile. La republication PyPI des paquets
> en 2.x est calée sur le jalon v2.0.0 (§6, phase 5).

### 4.4 Dépendances mortes ou à remplacer

- `velruse` (auth sociale) : projet abandonné → remplacer par OIDC
  standard (authlib) ; noter que tu maîtrises déjà Keycloak via
  AlirPunkto, une intégration OIDC générique couvrirait
  Google/Facebook/entreprise d'un coup.
- `yampy2` (Yammer) : Microsoft a fermé Yammer/Viva Engage classic →
  supprimer le connecteur.
- `tornado < 4` + `pyzmq` dans dace : cœur de la boucle d'événements,
  API 2013 → réécriture asyncio (§6, phase 3).
- `xlrd` : ne lit plus les .xlsx depuis la 2.0 → openpyxl.
- `graphene 1.4` + fork `graphql-wsgi` : deux générations de retard →
  graphene 3 (chemin le plus court, schéma existant) ou strawberry
  (meilleur typage) ; décision en phase 3.
- `keas.kmi` + `cipher.encryptingstorage` (chiffrement at-rest de la
  ZODB) : à réévaluer selon les exigences RGPD visées ; si conservé,
  ces deux forks entrent dans le périmètre maintenu.
- Incompatibilités Python ≥ 3.12 déjà repérées dans le code :
  `import imp` (supprimé en 3.12) dans `novaideo/event.py`, `core.py`,
  `fr_lexicon.py` ; `pkg_resources` dans `novaideo/ips/hexagonit`. Le
  reste (pas d'`async` en identifiant dans le code Python, pas
  d'`asyncore`/`getargspec`) est plutôt sain — la base est du Python 3
  propre, le portage est surtout une affaire de dépendances.

> **Statut : LARGEMENT TRAITÉ, avec des écarts au plan assumés.**
> tornado est retiré (asyncio, étape A) et zmq attend l'étape B ; les
> incompatibilités 3.12 (`imp`, `pkg_resources`) sont corrigées ;
> **graphene 1 a finalement été porté sur 3.12 par outillage** plutôt
> que migré vers graphene 3 — chemin le plus court, schéma préservé,
> décision réversible en phase 4. velruse/yampy2/xlrd sont toujours
> présents (la parité du golden master l'exigeait) : leur remplacement
> ou retrait reste programmé, hors chemin critique de la migration.

### 4.5 Qualité, tests, CI

DaCE est correctement testé (19 fichiers — précieux : c'est la partie
la plus complexe), pontus modestement, novaideo peu en unitaire mais
avec une suite Robot Framework/Selenium (probablement irréparable
telle quelle, à remplacer par Playwright). daceui : zéro test. La CI
était Travis CI (service à l'abandon pour l'open source) avec un
webhook Slack chiffré — à recréer sous GitHub Actions. Les `.ini`
versionnés ne contiennent que des secrets factices (`seekri1`, `xxx`) :
hygiène correcte, à formaliser (secrets exclusivement par variables
d'environnement, rotation par précaution).

> **Statut : TRANSFORMÉ.** dace 88 tests (91 %), pontus 39 tests
> (63 → 79 %), daceui **ses 14 premiers tests de l'histoire** (81 %),
> novaideo **29 → 128 tests** de caractérisation — les cinq familles
> de processus du contrat social (question, personne, invitation,
> inscription, signalement/modération) et les **deux scrutins de
> modération conduits jusqu'au verdict**. La campagne a mis au jour
> **quatre bugs latents** (trois dans pontus, un dans novaideo — dont
> deux chemins de code qui n'avaient jamais pu s'exécuter) et **une
> régression de modernisation** (API mot de passe de substanced) :
> tous corrigés, chaque réparation gardée par son test retourné en
> conscience. Deux étages de CI GitHub Actions (golden master legacy
> et py312) sont verts à chaque push ; la suite complète se certifie
> en deux moitiés (voir `modern-harness.md`). La migration vers
> pytest reste au programme, hors chemin critique.

### 4.6 Documentation existante

READMEs squelettiques (celui de KuneAgi s'intitule encore « Nova
Ideo » et renvoie au site), aucune doc d'architecture, monkey-patches
et protocole d'événements non documentés, pas de glossaire du modèle
(Idée/Proposition/Groupe de travail/Amendement/Jeton/Jugement
majoritaire — ton article de 2021 est aujourd'hui la meilleure doc
fonctionnelle du produit). Ton intuition de faire de la documentation
une phase à part entière est validée par l'audit.

> **Statut : RÉSOLU (relecture humaine restante).** Documentation
> bilingue `docs/en` + `docs/fr` sur les quatre dépôts : READMEs
> complets, architectures, catalogue auto-généré des **43 processus**
> (extracteur BPMN → mermaid), docstrings (dace 67,7 %, pontus
> 88,3 %, daceui 88,8 %), harnais moderne et ses idiomes de test,
> runbooks (répétition M5, migration de production, réveil contrôlé),
> registre des problèmes connus (résolus, conservé en mémoire
> historique), fils de l'eau. La relecture humaine des documents
> générés en phase 2 reste à planifier.

### 4.7 Données de production (constat nouveau — révision 5)

L'audit initial n'avait pas accès aux données. La répétition de
migration (M5) a examiné une **vraie copie de production
déchiffrée** (client ZEO en lecture seule, clés jamais sorties du
serveur, règles strictes de non-divulgation : agrégats seulement) :
**79 269 enregistrements, 381 classes, zéro objet cassé**, étapes
`evolve` sans opération, 61 index reconstruits à comptes identiques.
Deux faits d'audit en ressortent : (a) une **dérive du chiffrement
at-rest** — 64 987 enregistrements chiffrés contre 14 282 en clair, et
les blobs jamais chiffrés — à auditer et trancher (politique keas.kmi/
cipher.encryptingstorage) avant ou pendant la migration ; (b) dix ans
de minuteries expirées dorment dans la base — d'où le **profil de
réveil contrôlé** du runbook (courriels détournés vers
`var/mail-out/`, SMS factices) qui interdit tout envoi réel au
redémarrage.

---

## 5. Registre des risques

| # | Risque | Impact | Prob. | Mitigation | **Statut (18/07/2026)** |
|---|---|---|---|---|---|
| 1 | Perte de connaissance (développeur principal parti en 2019, code non documenté, monkey-patches) | Élevé | Acquis | Phase 2 documentation + tests de caractérisation avant toute refonte | **Mitigé** : docs bilingues + 128 tests épinglant les contrats |
| 2 | substanced/hypatia orphelins | Élevé | Acquis | Fork interne élagué, porté 3.12 (§4.2 option A) | **Ouvert** : contourné (amont + shims, Pyramid 1.10.8) ; fork Pyramid 2 à faire |
| 3 | Réécriture asyncio du moteur d'événements DaCE (timers, événements conditionnels, processus système) | Élevé | Moyenne | Doc du protocole d'abord, tests de caractérisation, réécriture isolée derrière l'API existante | **Partiel** : étape A faite (asyncio, API constante) ; étape B (retrait zmq) restante |
| 4 | Forks satellites hors de contrôle (comptes tiers, protocole git:// mort) | Moyen | Acquis | Rapatriement immédiat dans l'organisation Logikascium (phase 0) | **Résolu** : constellation rapatriée ; merge-backs ecreall planifiés (v2.0.0) |
| 5 | Renommage des paquets → **pickles ZODB cassés** (les chemins de classes sont sérialisés dans Data.fs) | Élevé si données à migrer | Moyenne | Conserver les dotted names (`novaideo`, `dace`…) ou table de renommage zodbupdate ; décision phase 0 | **Maîtrisé** : noms de modules gelés ; seuls des noms non persistés ont été renommés (vérifié), avec alias |
| 6 | Double base nova-ideo/KuneAgi (2 × 80 k lignes) | Moyen | Acquis | Réunification sur un tronc + profils de configuration | **En cours** : stratégie d'adoption nova-ideo 2.0 ; 9 fichiers exclusifs catalogués |
| 7 | Volumétrie UI (439 templates, 286 vues) sous-estimée | Moyen | Moyenne | Périmétrer la v2 UI par parcours (challenge → idée → groupe → proposition → vote), le reste suit | **Inchangé** (phase 4 non entamée) |
| 8 | Effet tunnel | Moyen | Moyenne | Jalons livrables par phase, golden master permanent | **Conjuré** : chaque lot livré et poussé, CI vertes en continu |
| 9 | *(nouveau)* Dérive du chiffrement at-rest en production (mélange chiffré/clair, blobs en clair) | Moyen | Acquis | Audit dédié + politique tranchée avant/pendant la migration (§4.7) | **Ouvert** |

---

## 6. Plan de modernisation

Principe directeur : **ne jamais moderniser ce qu'on ne sait pas
reconstruire ni tester**. D'où l'insertion d'une phase 1 « build
legacy reproductible » entre ton audit et ta phase de documentation.

### Phase 0 — Reprise de contrôle (1 à 2 semaines) — **EXÉCUTÉE**

Rapatrier les 5 dépôts **et tous les forks satellites** dans
l'organisation GitHub Logikascium (fork ou transfert), taguer
`legacy-final` partout, archiver les originaux avec un pointeur.
Réparer `sources.cfg` (`git://` → `https://`, URLs re-pointées vers
Logikascium). Trancher trois décisions structurantes : (a) tronc de
référence = KuneAgi (recommandé) ; (b) **conservation des noms de
modules Python** pour préserver les pickles ZODB — on peut renommer
les dépôts et la marque sans renommer les paquets ; (c) licence :
AGPL v3 conservée (cohérente avec un modèle SaaS, et tu détiens la PI
pour toute évolution future). Inventorier les éventuelles Data.fs de
production à migrer.

> **Réalisé.** Les trois décisions sont actées et appliquées ; les
> forks vivent sous `michaellaunay/*` (tags `legacy-golden-master`
> posés), en attendant les merge-backs vers `ecreall` au jalon
> v2.0.0.

### Phase 1 — Build legacy reproductible = étalon de non-régression (2 à 4 semaines) — **EXÉCUTÉE**

Reconstruire l'image Docker figée (l'épinglage par SHA de python:3.6
est une chance : l'image existe encore), faire tourner buildout
jusqu'au bout, relancer les suites de tests existantes (dace,
novaideo, pontus, html_diff_wrapper, deform_treepy — le `.travis.yml`
documente exactement quoi lancer), obtenir une instance qui démarre
avec des données de démonstration. Mettre cette exécution sous GitHub
Actions. Livrable : le « golden master » — toute étape ultérieure se
mesure contre lui. C'est aussi le moment de la passe
`pip-audit`/inventaire CVE chiffré.

> **Réalisé.** Golden master **certifié 29/29** sur la pile 2017
> reconstruite, rejoué en CI à chaque push — puis re-certifié 29/29
> sur la pile moderne (M4), devenant l'étalon bi-pile permanent.

### Phase 2 — Documentation exhaustive (3 à 6 semaines) — **EXÉCUTÉE** (relecture humaine restante)

C'est ta phase 2, outillée :

- **README complet par dépôt** : rôle, positionnement dans la pile,
  installation, exemples. Glossaire du domaine (reprendre ton article
  comme base fonctionnelle).
- **Doc d'architecture transverse** : le diagramme en couches du §3,
  le cycle de vie d'une proposition, le protocole d'événements de
  DaCE, le contenu de `dace/patches.py` patch par patch.
- **Catalogue des 24 paquets de processus métier** : les définitions
  DaCE sont déclaratives — écrire un petit extracteur qui génère
  automatiquement les diagrammes mermaid/BPMN depuis le code. Rapport
  effort/valeur imbattable, et le livrable sert ensuite de doc
  vivante.
- **Docstrings** : passe systématique dans l'ordre dace → pontus →
  daceui → novaideo/content/processes, génération assistée par LLM
  avec revue humaine, couverture mesurée en CI.
- **ADR** (architecture decision records) pour tracer chaque décision
  de migration à partir de maintenant.

> **Réalisé.** 43 processus en pages bilingues auto-générées
> (`bpmn2mermaid`), docstrings dace 67,7 % / pontus 88,3 % / daceui
> 88,8 %, architectures et READMEs bilingues partout. S'y sont
> ajoutés, au fil de l'exécution : le document du **harnais moderne**
> et ses idiomes de tests, les **runbooks** (répétition, production,
> réveil contrôlé) et le **registre des problèmes connus** (désormais
> mémoire historique des bugs résolus). Reste : la relecture humaine
> des documents générés.

### Phase 3 — Socle Python moderne (6 à 10 semaines) — **EXÉCUTÉE** (jalons M0 → M5)

Cible : **Python 3.12**. Ordre de portage ascendant, chaque paquet
vert avant le suivant :

1. **Fork substanced/hypatia élagué** porté 3.12/Pyramid 2.0.x,
   ZODB 6, deform 2.0.15/colander 2.
2. **dace** : corrections mécaniques, puis le morceau sérieux —
   remplacer tornado 3 + pyzmq par **asyncio** derrière l'API
   existante.
3. **pontus**, puis **daceui** (écrire enfin ses premiers tests).
4. **novaideo/KuneAgi réunifiés** : `imp` → importlib,
   `pkg_resources` → importlib.metadata, modernisation des
   dépendances applicatives.

> **Réalisé, avec des écarts assumés (consignés dans
> `phase3-porting-plan.md`).** M1 dace 88/88 sur 3.12 (réacteur
> asyncio étape A à API constante) ; M2 pontus (deform 3/colander
> 2/Chameleon 4) ; M3 daceui (première suite de son histoire) ; M4
> golden master 29/29 sur 3.12 (pile graphene 1 **portée par
> outillage** plutôt que migrée) ; M5 répétition de migration réussie
> sur vraie copie de production. Écarts : substanced consommé en
> amont + shims (Pyramid tenu en 1.10.8) au lieu du fork élagué —
> reporté ; buildout conservé côté legacy (la pile moderne est en
> pip/constraints) ; pytest reporté. La campagne de caractérisation
> qui a suivi (29 → 128 tests) a durci ce socle bien au-delà du
> critère de sortie initial.

### Phase 4 — Frontend (8 à 16 semaines selon le périmètre) — **NON ENTAMÉE**

Décision recommandée : **ne pas ressusciter la branche
`nova-ideo-react`** mais la traiter comme spécification. Depuis la
révision 4, le choix retenu est **SolidJS** (+ TypeScript), client
GraphQL moderne, en complétant l'API au fil des écrans. Stratégie
strangler : l'UI serveur Chameleon reste en place, la SPA prend les
parcours un par un (challenges/idées d'abord, puis groupes de
travail/amendements/votes). Option B frugale si le budget se tend :
conserver le rendu serveur et le rafraîchir (Bootstrap 5 + htmx) —
environ un tiers du coût ; à chiffrer avant la phase 4.

### Phase 5 — Données, déploiement, exploitation (2 à 4 semaines) — **PARTIELLE**

Outillage de migration des Data.fs existants : étapes evolve
substanced, banc de migration à blanc rejouable. Docker moderne,
docker compose v2, Dependabot/Renovate, publication des paquets sur
PyPI sous les versions 2.x pour matérialiser la reprise.

> **Réalisé / restant.** Le banc de migration à blanc est fait et
> **réussi sur une vraie copie de production** (M5) ; le **runbook de
> production** est prêt (cible épinglée, réveil contrôlé, portes de
> vérification, rollback, jalon de version). Restent : l'exécution de
> la migration réelle, puis au jalon v2.0.0 les tags, les merge-backs
> `ecreall` (dont l'adoption nova-ideo 2.0) et la republication PyPI
> 2.x.

### Phase 6 — Évolutions produit (continu, après la v2) — inchangée

Reprise du bilan 2021 de ton article, réévaluée à l'aune de 2026 :
l'anonymisation des participations et la simplification UX du
jugement majoritaire deviennent des lots applicatifs classiques une
fois le socle sain. La fusion idée/proposition prévue avec CamemBERT
se traite aujourd'hui bien mieux par LLM via API (détection d'idées
similaires, liage idées↔propositions, synthèse des fils de
discussion, aide à la rédaction d'amendements) — et c'est aligné avec
le positionnement de Logikascium. Quant à la **réécriture Rust du
moteur** envisagée en 2021 : à requalifier — aucun goulot de
performance n'est documenté ; à garder comme option v3, jamais avant
que documentation et tests n'existent (condition désormais remplie
pour l'essentiel, ce qui rend l'évaluation possible le jour venu).

---

## 7. Calendrier et charges indicatives

Hypothèse initiale : un développeur senior connaissant l'écosystème
Zope/Pyramid (toi), assisté LLM, hors gestion de projet.

| Phase | Livrable clé | Charge estimée | **Statut** |
|---|---|---|---|
| 0 — Reprise de contrôle | Dépôts + forks sous contrôle, build réparé, décisions actées | 5–10 j | **Exécutée** |
| 1 — Golden master | Instance legacy qui tourne + CI qui rejoue les tests | 10–20 j | **Exécutée** |
| 2 — Documentation | Docs publiées, catalogue BPMN auto-généré, docstrings | 15–30 j | **Exécutée** (relecture restante) |
| 3 — Socle 3.12 | 4 paquets verts sur pile 2026, UI serveur iso | 30–50 j | **Exécutée** |
| 4 — Frontend | SPA SolidJS sur les parcours cœur (ou option B htmx : 10–20 j) | 40–80 j | Non entamée |
| 5 — Données/ops | Migration Data.fs outillée, déploiement moderne | 10–20 j | **Partielle** (répétition réussie ; migration réelle restante) |

> **Réalisé vs estimé.** Le périmètre « v2 backend » (phases 0-3 + 5
> hors migration réelle), estimé à **70-130 jours**, a été exécuté
> **entre le 13 et le 18 juillet 2026** — un travail continu assisté
> par LLM sous revue et pilotage humains, qui a de surcroît livré
> au-delà du périmètre (campagne de 128 tests, quatre bugs latents
> corrigés, runbooks). L'estimation de la phase 4, qui obéit à
> d'autres contraintes (design, itérations d'usage), reste valable
> comme ordre de grandeur.

## 8. Actions de la première semaine

Forker/transférer les dépôts et les satellites, corriger `git://` →
`https://` dans les `sources.cfg`, taguer `legacy-final`, poser une CI
squelette, relancer le build Docker legacy, et écrire le premier ADR
(« KuneAgi devient le tronc, en co-gouvernance avec
Cosmopolitical.coop ; tout reste sous AGPL v3 ; les noms de modules
Python sont gelés pour préserver les pickles ZODB »). Tout le reste
découle de là.

> **Statut : toutes exécutées.** Prochaines actions (18/07/2026), dans
> l'ordre : exécuter la **migration de production** (runbook
> `production-migration.md` — cible épinglée, réveil contrôlé) ; au
> premier vrai cycle survécu, poser les tags **v2.0.0** et dérouler
> les **merge-backs `ecreall`** (bibliothèques en avance rapide,
> coutures d'adoption KuneAgi et nova-ideo 2.0) ; puis, hors chemin
> critique : étape B du réacteur (retrait de zmq), fork substanced
> élagué pour Pyramid 2, migration pytest, audit du chiffrement
> at-rest (§4.7), relecture humaine des documents de phase 2.

---

## 9. Glossaire (à l'usage du lecteur non informaticien)

Définitions volontairement vulgarisées, dans le contexte de ce
document ; le praticien y trouvera des raccourcis assumés.

**ADR (Architecture Decision Record)** — courte note qui consigne une
décision technique, ses raisons et les alternatives écartées, afin que
l'on sache encore « pourquoi » des années plus tard.

**AGPL v3, copyleft** — licence de logiciel libre. Le « copyleft » est
sa clause centrale : quiconque modifie le logiciel — y compris pour le
proposer comme service en ligne — doit publier ses modifications sous
la même licence. C'est ce qui garantit que le code reste un bien
commun.

**Amont (upstream), droit de merge** — l'« amont » est le dépôt de
référence d'un projet, celui dont dérivent les copies et vers lequel
remontent les contributions ; le « droit de merge » désigne qui a
autorité pour accepter l'intégration de ces contributions.

**API, GraphQL** — une API est la porte d'entrée normalisée par
laquelle un programme dialogue avec un autre. GraphQL est un type
d'API où le demandeur décrit précisément les données qu'il souhaite
recevoir, ni plus ni moins.

**Backend, frontend** — le backend est la partie du logiciel qui
s'exécute sur le serveur (données, règles métier) ; le frontend est ce
qui s'exécute dans le navigateur de l'utilisateur (l'interface).

**Bibliothèque, framework** — une bibliothèque est un ensemble de
fonctions réutilisables qu'un programme appelle ; un framework est un
socle plus structurant, qui impose une manière d'organiser
l'application (Pyramid côté serveur, SolidJS côté navigateur).

**Branche, commit, tag (git)** — git est l'outil qui conserve
l'historique du code. Un « commit » est un enregistrement daté d'une
modification ; une « branche » est une ligne de développement
parallèle (comme la branche React de 2019, jamais fusionnée) ; un
« tag » est une étiquette posée sur un état précis du code pour
pouvoir y revenir à coup sûr (ex. `legacy-final`).

**Breaking change** — évolution d'un composant qui rompt la
compatibilité : les programmes qui l'utilisaient doivent être adaptés.

**Build, buildout** — le « build » est l'opération qui assemble le
code source et toutes ses dépendances en un logiciel exécutable ; dire
que « le build est cassé » signifie qu'on ne peut plus fabriquer le
logiciel à partir de ses sources. Buildout est l'outil d'assemblage
historique de l'écosystème Zope, utilisé par le projet, aujourd'hui
supplanté par des standards plus répandus.

**CI (intégration continue)** — automate qui, à chaque modification du
code, reconstruit le logiciel et exécute les tests, afin de détecter
immédiatement toute régression. GitHub Actions est le service de CI de
GitHub.

**Codegen (génération de code)** — outillage qui produit
automatiquement le code répétitif (ici, le code TypeScript
correspondant aux requêtes GraphQL) — autant d'erreurs humaines en
moins.

**CVE** — identifiant public d'une faille de sécurité documentée. Des
« dépendances avec CVE » sont des composants dont les failles sont
connues de tous, et exploitables tant qu'on ne les met pas à jour.

**Dépendance, épinglage (pin)** — une dépendance est une brique
logicielle tierce nécessaire au projet ; il y en a des dizaines, et
chacune vieillit. « Épingler » une version, c'est la figer précisément
pour garantir un assemblage reproductible — au prix du vieillissement
de l'ensemble si personne ne remet les épingles à jour.

**Dépôt (repository)** — espace où sont conservés le code source d'un
projet et tout son historique (ici, sur GitHub).

**Docker, conteneur, image** — technologie qui emballe un logiciel
avec tout son environnement dans une « boîte » standardisée (l'image),
exécutable à l'identique sur n'importe quel serveur (le conteneur).

**EOL (end of life)** — date après laquelle un logiciel ne reçoit plus
aucun correctif, même de sécurité. Python 3.6, socle historique du
projet, est EOL depuis décembre 2021.

**Fork** — copie indépendante d'un projet, qui vit ensuite sa propre
vie. KuneAgi est un fork de Nova-Ideo ; « forker substanced » signifie
en prendre une copie que Logikascium maintiendra elle-même.

**Golden master** — version de référence de l'existant, remise en état
de marche puis figée, contre laquelle chaque étape de modernisation
est comparée pour vérifier que rien n'a régressé.

**Headless (composants)** — composants d'interface livrés « sans
habillage » : ils fournissent le comportement (menus, fenêtres,
accessibilité au clavier), l'apparence restant à définir soi-même.

**htmx** — petite bibliothèque qui rend interactives des pages
fabriquées par le serveur ; alternative économique à une application
JavaScript complète.

**Îlots (architecture en)** — technique consistant à ne placer des
composants interactifs modernes qu'aux endroits de la page qui en ont
besoin, le reste demeurant des pages classiques rendues par le
serveur.

**JSX** — syntaxe mêlant balises d'interface et code JavaScript,
commune à React et à SolidJS — c'est elle qui rend l'ancien code React
de 2019 encore lisible comme spécification.

**LLM (grand modèle de langage)** — programme d'intelligence
artificielle entraîné sur de vastes corpus de textes, utilisé ici
comme assistant pour documenter et écrire du code, toujours sous revue
humaine.

**Monkey-patch** — modification « à chaud » du comportement d'une
bibliothèque tierce, sans toucher à son code source. Efficace mais
invisible et fragile : d'où l'importance de les recenser.

**Moteur de processus, BPMN** — logiciel qui exécute des processus
métier décrits comme des enchaînements d'étapes, de décisions et
d'échéances ; BPMN est la notation graphique standard de ces
processus. DaCE est le moteur de processus sur lequel repose
Nova-Ideo.

**OIDC (OpenID Connect)** — standard d'authentification permettant le
« se connecter avec » un compte existant (Google, compte
d'entreprise…) ; il remplace les connecteurs sociaux devenus
obsolètes.

**Orphelin (projet)** — projet libre sans mainteneur actif : il
continue de fonctionner, mais plus personne ne corrige ses failles ni
ne l'adapte aux évolutions. C'est le cas de substanced, socle du
projet.

**PyPI, npm** — les « magasins » publics de bibliothèques : PyPI pour
Python, npm pour JavaScript. Les projets y téléchargent leurs
dépendances.

**Régression** — réapparition d'un défaut, ou perte d'une
fonctionnalité, à l'occasion d'une modification. Les tests et le
golden master servent précisément à la détecter.

**Rendu serveur, SPA** — deux façons de construire une interface web.
Dans le rendu serveur, chaque page est fabriquée sur le serveur puis
envoyée au navigateur (c'est l'interface actuelle, 439 gabarits) ;
dans une SPA (Single Page Application), l'application se charge une
fois dans le navigateur puis dialogue avec le serveur par API, sans
rechargement de pages.

**Runtime** — part d'un framework d'interface que le navigateur doit
télécharger et exécuter. Un runtime « minuscule » (SolidJS) signifie
des pages plus légères et plus rapides.

**Signals (réactivité fine)** — technique d'interface où chaque donnée
sait exactement quels éléments de l'écran dépendent d'elle, et ne met
à jour que ceux-là. C'est le cœur de SolidJS, et le modèle vers lequel
l'industrie a convergé.

**Spike** — mini-prototype jetable, borné dans le temps (ici 3 à 5
jours), réalisé dans le seul but de lever une incertitude technique
avant d'engager un chantier. On en garde la connaissance, pas le code.

**Stratégie strangler (du figuier étrangleur)** — modernisation
progressive dans laquelle le nouveau système enveloppe l'ancien et le
remplace écran par écran, jusqu'à pouvoir débrancher l'ancien — par
opposition au remplacement brutal en une seule bascule, bien plus
risqué.

**Template (gabarit), Chameleon** — fichier décrivant la structure
d'une page HTML, que le serveur remplit avec les données au moment de
la servir. Chameleon est le système de gabarits utilisé (439
fichiers).

**Tests unitaires, de caractérisation, de bout en bout** — programmes
qui vérifient automatiquement le comportement du logiciel. Les tests
unitaires contrôlent chaque brique isolément ; les tests « de
caractérisation » photographient le comportement actuel de l'existant
pour détecter tout changement involontaire pendant la modernisation ;
les tests de bout en bout (Playwright) pilotent un vrai navigateur
comme le ferait un utilisateur.

**TypeScript, typage** — pratique consistant à déclarer la nature de
chaque donnée (nombre, texte, idée, proposition…), ce qui permet de
détecter des erreurs avant même d'exécuter le programme. TypeScript
l'apporte à JavaScript.

**VDOM (Virtual DOM)** — technique de React consistant à reconstruire
en mémoire une maquette de la page à chaque changement, puis à la
comparer à l'écran pour n'appliquer que les différences. SolidJS s'en
passe, d'où ses performances.

**Vendoriser** — intégrer le code d'une dépendance directement dans
son propre projet afin de ne plus dépendre de son auteur d'origine ;
utile quand celle-ci est à l'abandon.

**Wrapper, bindings** — fines couches de code qui adaptent une
bibliothèque à un environnement pour lequel elle n'était pas prévue
(ex. adapter l'éditeur ProseMirror à SolidJS).

**ZODB, Data.fs, pickles** — ZODB est la base de données orientée
objets de l'écosystème Zope : elle enregistre directement les objets
du programme (idées, propositions, votes) dans un fichier unique, le
Data.fs, sous un format appelé « pickle ». Ces enregistrements
mémorisent le nom exact des modules Python : renommer les modules
rendrait les données existantes illisibles — d'où la règle de gel des
noms.

### Termes ajoutés en révision 5

**Bi-pile (dual-stack)** — état d'un même code capable de tourner sur
deux environnements : la pile historique de 2017 (le golden master) et
la pile moderne Python 3.12. C'est ce qui permet de comparer les deux
comportements à l'identique pendant toute la modernisation.

**Avance rapide (fast-forward)** — fusion git triviale possible quand
une ligne de code est le simple prolongement d'une autre : rien à
réconcilier, l'histoire avance d'un bloc.

**Couture (fusion d'adoption)** — fusion git particulière qui relie
deux histoires jusque-là indépendantes en faisant de l'ancienne un
« parent » de la nouvelle, sans changer une ligne du code adopté :
l'histoire ancienne reste consultable, le présent est celui de la
ligne modernisée.

**Répétition de migration (rehearsal)** — exécution complète de la
migration sur une copie des données réelles, dans un environnement
isolé et sans aucun envoi vers l'extérieur, pour prouver la procédure
avant le grand soir.

**Test retourné en conscience** — un test de caractérisation qui
épinglait un défaut (il passait en affirmant le comportement cassé)
et qui, une fois le défaut corrigé, est réécrit pour garder la
réparation : le même test change de camp, délibérément et
traçablement.

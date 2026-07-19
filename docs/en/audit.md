# Audit and modernisation plan — Nova-Ideo, DaCE, Pontus, DaceUI

**For:** Logikascium EURL — **Initial audit:** 13 July 2026 —
**Revision 5:** 18 July 2026
**Method:** full cloning and static analysis of the 5 repositories
`github.com/ecreall/{nova-ideo, KuneAgi, dace, pontus, daceui}` (git
history, volumetrics, declared and pinned dependencies, branches,
state of the upstream packages on PyPI). The presentation article
(Ecréall, ed. 57) served as the functional reference. Limits of the
initial audit: no code execution and no production-data audit; the
runtime findings remained to be confirmed in phase 1.

**Revision 5 — execution update.** Between 13 and 18 July 2026,
phases 0 to 3 and most of phase 5 were **executed**; the limits of the
initial audit are lifted (the code has run, a real production copy has
been examined). Every finding (§4), every risk (§5) and every phase
(§6) now carries its **status**, and the document enters the
repository (`docs/fr`, `docs/en`). Earlier revisions: r2-r3 (frontend
recommendations), r4 (glossary for the non-technical reader, SolidJS
choice, intellectual-property clarifications).

**Non-technical reader:** a glossary of the terms used is provided at
the end of the document (§9).

---

## 1. Executive summary

The ecosystem is **coherent, ambitious and well architected for its
era (2015-2019)**, but it is frozen today on a 2017 stack: Python 3.6
(EOL Dec. 2021), Pyramid 1.9.1, substanced 1.0a1, ZODB 5.3, graphene
1.4, Bootstrap 3/jQuery, buildout. **The build no longer works as
is** (the git sources use the `git://` protocol, disabled by GitHub in
2022). The React attempt (branch `nova-ideo-react`, stopped in January
2019) is too dated to be resumed as such, but constitutes an excellent
UX specification.

The three strategic locks are:

1. **substanced/hypatia**, the foundation of the whole edifice,
   effectively orphaned (see §4.2) → to be forked/vendored under
   Logikascium governance;
2. **DaCE's event engine** (tornado < 4 + pyzmq, 2015 code) → to be
   rewritten on asyncio, the most delicate technical work;
3. **knowledge loss** (the main developer left the project in 2019,
   ~85 % of the commits) → the documentation phase you plan is not a
   luxury, it is the mitigation of risk #1.

The approach you propose (audit → documentation → update) is the right
one, with one indispensable addition in between: **rebuilding a
reproducible legacy build** that will serve as the non-regression
yardstick before any code is touched.

Overall estimate for a v2 at functional parity on a 2026 stack: **5 to
9 months** of effective work for an experienced developer assisted by
an LLM, sliceable into independently deliverable milestones (detail
§7).

> **Update (2026-07-18).** The diagnosis above was confirmed point by
> point — and the plan was executed well beyond expectations. State of
> play: both builds (legacy and modern) are rebuilt and under CI; the
> **golden master is certified 29/29** on the rebuilt 2017 stack
> **and** on Python 3.12; the test suite grew from 29 to **128
> characterisation tests** (the five process families of the
> platform's social contract and both moderation ballots conducted to
> their verdicts); **four latent bugs and one modernisation
> regression** were found and fixed, each repair guarded by its
> consciously flipped pinning test; the bilingual documentation covers
> the ecosystem (43 processes as generated pages, harness, runbooks);
> a **migration rehearsal PASSED on a real production copy** (79,269
> records, 381 classes, zero broken) and the production runbook is
> ready. Locks #2 and #3 are essentially lifted (reactor: asyncio
> step A done at constant API, step B — removing zmq — remaining;
> knowledge: re-documented and pinned by the tests). Lock #1
> (substanced) is **bypassed but not lifted**: the modern stack rests
> on upstream 1.0b1 with Pyramid held at 1.10.8; the pruned fork for
> Pyramid 2 remains the structuring work ahead.

---

## 2. Repository inventory (observed)

| Repository | Role | Last commit | Commits | Python volumetrics | Tests |
|---|---|---|---|---|---|
| **nova-ideo** | Participatory-innovation application | 2020-03-28 | 2,392 | 517 files / 71,675 lines + **439 Chameleon templates (.pt)** | 9 files + Robot Framework suite |
| **KuneAgi** | Variant (cooperative governance: ballots, citizenship, mails) | **2023-03-02** | 2,195 | 538 files / 81,519 lines | same as nova-ideo |
| **dace** | Data-centric workflow engine (activities, gateways, BPMN-like events) | 2017-12-19 | 564 | 79 files / 13,792 lines | 19 files — the best tested |
| **pontus** | Views/forms layer (Pyramid + deform) on top of DaCE | 2018-01-15 | 429 | 23 files / 4,317 lines | 5 files |
| **daceui** | DaCE UI components (action panels, process history) | 2018-12-21 | 54 | 8 files / 1,743 lines | **0** |

Application structure of nova-ideo: ~30 content types (`idea`,
`proposal`, `amendment`, `ballot`, `challenge`, `working_group`,
`token`…), **24 business-process packages** (92 DaCE definition
files), 286 view files, a backend GraphQL module (~1,200 lines,
graphene 1.4). Translations: English source + fr (KuneAgi adds German,
2022).

**Contributors** (relevant to the intellectual-property question):
Amen Souissi ~85 % of the commits, then Vincent Fretin, Cédric
Messiant, Sophie Jazwiecki, you, and 1 external commit (Antoine Cezar)
+ Dependabot. All Ecréall employees/collaborators at the time → the IP
acquisition by Logikascium covers the essential; the external share is
negligible but remains under AGPL v3 (without consequence if you keep
the licence — a point to check with your counsel should you one day
consider dual licensing).

### 2.1 nova-ideo vs KuneAgi

KuneAgi is **not** a frozen fork: it is the most recent branch of the
lineage (14 commits between 2020 and March 2023: mailer/SPF,
Dockerfile, translations, ballot fixes), with a broader functional
scope (voting processes, citizenship). nova-ideo master stops in March
2020 but holds the exploration branches (`nova-ideo-react`,
`realtime`, `to-apollo2`) absent from KuneAgi.

**Recommendation:** take **KuneAgi as the functional reference trunk**
for the modernisation, produce a systematic diff against nova-ideo
master to identify what must be reunified, and aim in time for **a
single codebase** with the KuneAgi specifics as configuration profiles
rather than a fork. Maintaining two 80,000-line twins is not
sustainable.

> **Update (2026-07-18).** Recommendation applied and refined by
> measurement. The work lives on the
> `github.com/michaellaunay/{dace,pontus,daceui,KuneAgi}` forks; the
> systematic nova-ideo ↔ KuneAgi diff was produced and its verdict is
> clear: since the late-2016 split the two lines co-evolved (1,135
> files touched on both sides) and **only nine files** are specific to
> nova-ideo 2016-2020 (catalogued for arbitration). Reunification
> therefore takes the form of an **adoption**: nova-ideo 2.0 = the
> modernised trunk, with the 2010-2020 history stitched in as a
> parent. On the git-genealogy side, the `ecreall` tips of
> dace/pontus/daceui are direct ancestors of the forks (merge-back =
> pure fast-forward); KuneAgi and nova-ideo will each receive an
> adoption merge. The merge-backs are planned at the v2.0.0 milestone
> (after the production migration is validated).

---

## 3. Current architecture (as read in the code)

```
┌────────────────────────────────────────────────────────┐
│ novaideo / KuneAgi (application)                       │
│  content/ (~30 types) · content/processes/ (24 pkgs)   │
│  views/ (286 files) · graphql/ · mail/ · connectors/   │
├────────────────────────────────────────────────────────┤
│ daceui (rendering of actions/processes)                │
│ pontus (composable views, deform/colander forms)       │
├────────────────────────────────────────────────────────┤
│ dace: process engine                                   │
│  processdefinition/ · processinstance/ · catalog/      │
│  objectofcollaboration/ · system.py (system processes) │
│  event loop: tornado<4 + pyzmq (timers, conditional    │
│  events) · patches.py (monkey-patches)                 │
├────────────────────────────────────────────────────────┤
│ substanced 1.0a1 (resource tree, hypatia catalog,      │
│ principals, evolve) · Pyramid 1.9.1 · ZODB 5.3         │
└────────────────────────────────────────────────────────┘
```

Salient points:

- **Everything rests on substanced** (all four layers import it). It
  is the structuring choice of 2014 and the pivot of the migration.
- **DaCE embeds its own event loop** (tornado 3 + zmq) for
  temporal/conditional events and the "system processes" — 2015
  infrastructure code that no modern dependency will replace
  identically. `dace/patches.py` contains undocumented monkey-patches:
  to be mapped as a priority in the documentation phase.
- **Master frontend**: Chameleon server rendering + jQuery/Bootstrap
  3, bundled with gulp 3/browserify/babelify (a 2015 chain, not
  rebuildable on a modern Node without effort), draft-js editor.
- **Branch `nova-ideo-react`** (last commit 2019-01-29): a real SPA of
  386 JS/JSX files — React 16, Redux, react-apollo 2, Storybook, but
  with **material-ui 0.20 and @material-ui/core 3.7 mixed**, plus
  react-router 3 and 4 simultaneously. A worksite interrupted
  mid-transition. Seven years later, catching up would cost more than
  a rewrite; on the other hand the components, GraphQL queries and UX
  flows it contains are an **exploitable specification**.
- **Backend GraphQL API** real but partial (graphene 1.4 +
  `ecreall/graphql-wsgi` fork), designed for that SPA and for realtime
  (branch `realtime`).

> **Update (2026-07-18).** The architecture is unchanged in structure
> — that was the point: the modernisation is **dual-stack**, the same
> working tree runs on the rebuilt 2017 stack and on Python 3.12. Two
> internal evolutions: DaCE's event loop now runs on **asyncio**
> (step A, at constant API — tornado removed, zmq still present until
> step B), and the monkey-patches and event protocol are documented
> (phase 2). One architecture fact recorded by the tests: **the
> decision nodes of the moderation ballots complete at the
> DEADLINE** (timer-closed sub-processes) — to be known for
> operations as well as for any future engine migration.

---

## 4. Detailed findings

### 4.1 Obsolescence of the execution base

Versions pinned in `versions.cfg` (194 pins): pyramid 1.9.1,
substanced 1.0a1, ZODB 5.3.0, deform 2.0a2 (`amensouissi/deform`
fork), colander 1.0, hypatia 0.3, graphene 1.4, BTrees 4.4.1, waitress
1.1.0, gunicorn 19.7.1, Babel 2.3.4. The Docker image is pinned by SHA
on **python:3.6-stretch** — Python 3.6 has been EOL since December
2021 and Debian stretch since 2022: no more security fixes for the
interpreter, the OS or the dependencies (waitress 1.1 and gunicorn
19.7 have known CVEs, among others). A quantified `pip-audit` pass is
due as soon as the build is reproducible, but the global verdict is a
foregone conclusion: the entire environment is out of support.

> **Status: RESOLVED for the modern stack.** The same tree runs on
> Python 3.12 with contemporary dependencies under constraints; the
> 2017 stack is kept only as the golden master (isolated container,
> never exposed).

### 4.2 The substanced case — a structuring decision

Fact verified today: substanced published a **1.0b1 on PyPI on
2024-11-28** (and hypatia 0.5 on 2024-11-27). Beware the false good
news: the metadata of that 1.0b1 still announces Python 2.7–3.5 and
test dependencies `nose`, `cryptacular`, `lingua<2.0`. It is a
maintenance re-publication, not a modernisation — the project has had
neither a stable release in 12 years nor a roadmap. It must be treated
as an **orphaned dependency whose de-facto maintainer Logikascium
becomes**.

Two realistic options:

- **A (recommended): a pruned internal fork.** Vendor substanced +
  hypatia into a Logikascium-maintained package, reduced to the
  modules actually used (resource tree/objectmap, catalog, principals,
  evolve, folder, property sheets), ported to Python 3.12/Pyramid 2.
  Significant but bounded initial effort (the code is stable and well
  written), and you then control your destiny.
- **B: re-platform persistence (SQL/Postgres).** To be set aside for
  v2: the DaCE model is an object graph + catalog, deeply coupled to
  ZODB/substanced; it would be a rewrite, not a migration. To be
  re-evaluated possibly in v3 if SaaS-operation needs demand it (the
  intermediate option of RelStorage/Postgres as a ZODB backend already
  covers many ops needs without touching the code).

> **Status: BYPASSED, work remaining.** The modern stack rests on the
> upstream git 1.0b1 with a few one-line shims and **Pyramid held at
> 1.10.8**; a password-API regression between the two generations was
> uncovered by the test campaign and fixed dual-stack. Option A (the
> pruned fork ported to Pyramid 2) remains the recommended decision
> and the main structuring work ahead.

### 4.3 The build is broken (and repairable in a few hours)

`sources.cfg` references ~20 repositories as `git://github.com/...`:
GitHub disabled that protocol in March 2022, so **buildout can no
longer clone its sources today**. The repair is trivial (`git://` →
`https://`), but it reveals the real subject: the project depends on a
**constellation of Ecréall/personal forks** (deform fork, velruse
fork, graphql-wsgi, keas.kmi, cipher.encryptingstorage, yampy2,
html_diff_wrapper, deform_treepy, pyramid-sms…) hosted on accounts no
longer under your control (`amensouissi/*`, `vincentfretin/*`) or the
ecreall organisation. **Every unrepatriated fork is a point of
failure.** Besides, the PyPI packages `ecreall_dace/pontus/daceui`
date from February 2017 (1.1.0/1.0.4) — the git code evolved
afterwards, so PyPI does not reflect the real state.

> **Status: RESOLVED.** The legacy build is rebuilt and replayed in CI
> (golden master); the constellation is repatriated: **cryptacular
> 2.0** republished (byte-for-byte parity with the deployed module),
> `html_diff_wrapper` forked and fixed, `graphql-wsgi` pinned by sha
> and made conditional on the stack. The PyPI 2.x republication is
> scheduled at the v2.0.0 milestone (§6, phase 5).

### 4.4 Dead or to-be-replaced dependencies

- `velruse` (social auth): abandoned project → replace with standard
  OIDC (authlib); note that you already master Keycloak via
  AlirPunkto, a generic OIDC integration would cover
  Google/Facebook/enterprise at once.
- `yampy2` (Yammer): Microsoft closed Yammer/Viva Engage classic →
  remove the connector.
- `tornado < 4` + `pyzmq` in dace: heart of the event loop, a 2013
  API → asyncio rewrite (§6, phase 3).
- `xlrd`: no longer reads .xlsx since 2.0 → openpyxl.
- `graphene 1.4` + `graphql-wsgi` fork: two generations behind →
  graphene 3 (shortest path, existing schema) or strawberry (better
  typing); decision in phase 3.
- `keas.kmi` + `cipher.encryptingstorage` (at-rest ZODB encryption):
  to be re-evaluated against the targeted GDPR requirements; if kept,
  these two forks enter the maintained perimeter.
- Python ≥ 3.12 incompatibilities already spotted in the code:
  `import imp` (removed in 3.12) in `novaideo/event.py`, `core.py`,
  `fr_lexicon.py`; `pkg_resources` in `novaideo/ips/hexagonit`. The
  rest (no `async` as an identifier in the Python code, no
  `asyncore`/`getargspec`) is rather healthy — the base is clean
  Python 3, the port is mostly a dependency affair.

> **Status: LARGELY ADDRESSED, with assumed deviations from the
> plan.** tornado is removed (asyncio, step A) and zmq awaits step B;
> the 3.12 incompatibilities (`imp`, `pkg_resources`) are fixed;
> **graphene 1 was in the end PORTED to 3.12 by tooling** rather than
> migrated to graphene 3 — the shortest path, schema preserved, a
> decision reversible in phase 4. velruse/yampy2/xlrd are still
> present (golden-master parity required it): their replacement or
> removal remains scheduled, off the migration's critical path.

### 4.5 Quality, tests, CI

DaCE is properly tested (19 files — precious: it is the most complex
part), pontus modestly, novaideo little in unit terms but with a Robot
Framework/Selenium suite (probably unrepairable as such, to be
replaced by Playwright). daceui: zero tests. CI was Travis CI (a
service abandoned for open source) with an encrypted Slack webhook —
to be recreated under GitHub Actions. The versioned `.ini` files only
contain dummy secrets (`seekri1`, `xxx`): decent hygiene, to be
formalised (secrets exclusively via environment variables, rotation as
a precaution).

> **Status: TRANSFORMED.** dace 88 tests (91 %), pontus 39 tests
> (63 → 79 %), daceui **its first 14 tests ever** (81 %), novaideo
> **29 → 128 characterisation tests** — the five process families of
> the social contract (question, person, invitation, registration,
> report/moderation) and **both moderation ballots conducted to their
> verdicts**. The campaign surfaced **four latent bugs** (three in
> pontus, one in novaideo — including two code paths that had never
> been able to run) and **one modernisation regression** (substanced's
> password API): all fixed, each repair guarded by its consciously
> flipped pinning test. Two GitHub Actions CI floors (legacy golden
> master and py312) are green on every push; the full suite is
> certified in two halves (see `modern-harness.md`). The pytest
> migration remains scheduled, off the critical path.

### 4.6 Existing documentation

Skeletal READMEs (KuneAgi's is still titled "Nova Ideo" and points to
the website), no architecture documentation, undocumented
monkey-patches and event protocol, no domain glossary
(Idea/Proposal/Working group/Amendment/Token/Majority judgment — your
2021 article is today the product's best functional documentation).
Your intuition to make documentation a phase in its own right is
validated by the audit.

> **Status: RESOLVED (human review remaining).** Bilingual
> documentation `docs/en` + `docs/fr` across the four repositories:
> complete READMEs, architectures, the auto-generated catalogue of the
> **43 processes** (BPMN → mermaid extractor), docstrings (dace
> 67.7 %, pontus 88.3 %, daceui 88.8 %), the modern harness and its
> test idioms, the runbooks (M5 rehearsal, production migration,
> controlled wake-up), the known-issues register (resolved, kept as
> the historical record), worklogs. The human review of the
> phase-2-generated documents remains to be planned.

### 4.7 Production data (new finding — revision 5)

The initial audit had no access to the data. The migration rehearsal
(M5) examined a **real decrypted production copy** (read-only ZEO
client, keys never leaving the server, strict non-disclosure rules:
aggregates only): **79,269 records, 381 classes, zero broken object**,
`evolve` steps no-op, 61 indexes rebuilt with identical counts. Two
audit facts emerge: (a) an **at-rest encryption drift** — 64,987
encrypted records versus 14,282 in clear, and blobs never encrypted —
to audit and decide (keas.kmi/cipher.encryptingstorage policy) before
or during the migration; (b) ten years of expired timers sleep in the
base — hence the runbook's **controlled wake-up profile** (mails
diverted to `var/mail-out/`, dummy SMS) which forbids any real sending
at restart.

---

## 5. Risk register

| # | Risk | Impact | Prob. | Mitigation | **Status (2026-07-18)** |
|---|---|---|---|---|---|
| 1 | Knowledge loss (main developer gone in 2019, undocumented code, monkey-patches) | High | Certain | Phase 2 documentation + characterisation tests before any overhaul | **Mitigated**: bilingual docs + 128 tests pinning the contracts |
| 2 | substanced/hypatia orphaned | High | Certain | Pruned internal fork, ported to 3.12 (§4.2 option A) | **Open**: bypassed (upstream + shims, Pyramid 1.10.8); Pyramid-2 fork to do |
| 3 | asyncio rewrite of DaCE's event engine (timers, conditional events, system processes) | High | Medium | Protocol documentation first, characterisation tests, isolated rewrite behind the existing API | **Partial**: step A done (asyncio, constant API); step B (zmq removal) remaining |
| 4 | Satellite forks out of control (third-party accounts, dead git:// protocol) | Medium | Certain | Immediate repatriation (phase 0) | **Resolved**: constellation repatriated; ecreall merge-backs planned (v2.0.0) |
| 5 | Package renaming → **broken ZODB pickles** (class paths are serialised in Data.fs) | High if data to migrate | Medium | Keep the dotted names (`novaideo`, `dace`…) or a zodbupdate rename table; decision in phase 0 | **Under control**: module names frozen; only non-persisted names were renamed (verified), with aliases |
| 6 | Double codebase nova-ideo/KuneAgi (2 × 80 k lines) | Medium | Certain | Reunification on one trunk + configuration profiles | **In progress**: nova-ideo 2.0 adoption strategy; 9 exclusive files catalogued |
| 7 | UI volumetrics (439 templates, 286 views) underestimated | Medium | Medium | Scope the v2 UI by journeys (challenge → idea → group → proposal → vote), the rest follows | **Unchanged** (phase 4 not started) |
| 8 | Tunnel effect | Medium | Medium | Deliverable milestones per phase, permanent golden master | **Averted**: every batch delivered and pushed, CI continuously green |
| 9 | *(new)* At-rest encryption drift in production (encrypted/clear mix, blobs in clear) | Medium | Certain | Dedicated audit + policy decided before/during the migration (§4.7) | **Open** |

---

## 6. Modernisation plan

Guiding principle: **never modernise what you cannot rebuild or
test**. Hence the insertion of a phase 1 "reproducible legacy build"
between your audit and your documentation phase.

### Phase 0 — Taking back control (1 to 2 weeks) — **EXECUTED**

Repatriate the 5 repositories **and all satellite forks** (fork or
transfer), tag `legacy-final` everywhere, archive the originals with a
pointer. Repair `sources.cfg` (`git://` → `https://`, URLs re-pointed).
Settle three structuring decisions: (a) reference trunk = KuneAgi
(recommended); (b) **keep the Python module names** to preserve the
ZODB pickles — repositories and brand can be renamed without renaming
the packages; (c) licence: AGPL v3 kept (coherent with a SaaS model,
and you hold the IP for any future evolution). Inventory any
production Data.fs to migrate.

> **Done.** The three decisions are settled and applied; the forks
> live under `michaellaunay/*` (`legacy-golden-master` tags posed),
> pending the merge-backs to `ecreall` at the v2.0.0 milestone.

### Phase 1 — Reproducible legacy build = non-regression yardstick (2 to 4 weeks) — **EXECUTED**

Rebuild the frozen Docker image (the SHA pin on python:3.6 is a
stroke of luck: the image still exists), run buildout to the end,
re-run the existing test suites, obtain an instance that starts with
demo data. Put that execution under GitHub Actions. Deliverable: the
"golden master" — every later step is measured against it. It is also
the moment for the quantified `pip-audit`/CVE inventory.

> **Done.** Golden master **certified 29/29** on the rebuilt 2017
> stack, replayed in CI on every push — then re-certified 29/29 on the
> modern stack (M4), becoming the permanent dual-stack yardstick.

### Phase 2 — Exhaustive documentation (3 to 6 weeks) — **EXECUTED** (human review remaining)

Your phase 2, tooled:

- **A complete README per repository**: role, position in the stack,
  installation, examples. A domain glossary.
- **Cross-cutting architecture documentation**: the §3 layer diagram,
  the life of a proposal, DaCE's event protocol, the content of
  `dace/patches.py` patch by patch.
- **Catalogue of the 24 business-process packages**: the DaCE
  definitions are declarative — write a small extractor generating the
  mermaid/BPMN diagrams from the code. Unbeatable effort/value ratio,
  and the deliverable then serves as living documentation.
- **Docstrings**: a systematic pass in the order dace → pontus →
  daceui → novaideo/content/processes, LLM-assisted generation with
  human review, coverage measured in CI.
- **ADRs** to trace every migration decision from now on.

> **Done.** 43 processes as auto-generated bilingual pages
> (`bpmn2mermaid`), docstrings dace 67.7 % / pontus 88.3 % / daceui
> 88.8 %, bilingual architectures and READMEs everywhere. Added along
> the way: the **modern harness** document and its test idioms, the
> **runbooks** (rehearsal, production, controlled wake-up) and the
> **known-issues register** (now the historical record of the
> resolved bugs). Remaining: the human review of the generated
> documents.

### Phase 3 — Modern Python base (6 to 10 weeks) — **EXECUTED** (milestones M0 → M5)

Target: **Python 3.12**. Ascending port order, each package green
before the next:

1. **Pruned substanced/hypatia fork** ported to 3.12/Pyramid 2.0.x,
   ZODB 6, deform 2.0.15/colander 2.
2. **dace**: mechanical fixes, then the serious piece — replace
   tornado 3 + pyzmq with **asyncio** behind the existing API.
3. **pontus**, then **daceui** (finally write its first tests).
4. **novaideo/KuneAgi reunified**: `imp` → importlib,
   `pkg_resources` → importlib.metadata, modernisation of the
   application dependencies.

> **Done, with assumed deviations (recorded in
> `phase3-porting-plan.md`).** M1 dace 88/88 on 3.12 (asyncio reactor,
> step A at constant API); M2 pontus (deform 3/colander 2/Chameleon
> 4); M3 daceui (the first suite of its history); M4 golden master
> 29/29 on 3.12 (the graphene 1 stack **ported by tooling** rather
> than migrated); M5 migration rehearsal passed on a real production
> copy. Deviations: substanced consumed upstream + shims (Pyramid held
> at 1.10.8) instead of the pruned fork — deferred; buildout kept on
> the legacy side (the modern stack is pip/constraints); pytest
> deferred. The characterisation campaign that followed (29 → 128
> tests) hardened this base far beyond the initial exit criterion.

### Phase 4 — Frontend (8 to 16 weeks depending on scope) — **NOT STARTED**

Recommended decision: **do not resurrect the `nova-ideo-react`
branch** but treat it as a specification. Since revision 4 the
retained choice is **SolidJS** (+ TypeScript), a modern GraphQL
client, completing the API screen by screen. Strangler strategy: the
Chameleon server UI stays in place, the SPA takes the journeys one by
one (challenges/ideas first, then working groups/amendments/votes).
Frugal option B if the budget tightens: keep the server rendering and
refresh it (Bootstrap 5 + htmx) — about a third of the cost; to be
priced before phase 4.

### Phase 5 — Data, deployment, operations (2 to 4 weeks) — **PARTIAL**

Migration tooling for the existing Data.fs: substanced evolve steps, a
replayable blank-migration bench. Modern Docker, docker compose v2,
Dependabot/Renovate, PyPI publication of the packages as 2.x versions
to materialise the takeover.

> **Done / remaining.** The blank-migration bench is done and
> **passed on a real production copy** (M5); the **production
> runbook** is ready (pinned target, controlled wake-up, verification
> gates, rollback, release milestone). Remaining: executing the real
> migration, then at the v2.0.0 milestone the tags, the `ecreall`
> merge-backs (including the nova-ideo 2.0 adoption) and the PyPI 2.x
> republication.

### Phase 6 — Product evolutions (continuous, after v2) — unchanged

Resumption of your article's 2021 assessment, re-evaluated in 2026
light: anonymised participation and majority-judgment UX
simplification become classic application batches once the base is
sound. The idea/proposal merging planned with CamemBERT is handled far
better today by LLMs via API (similar-idea detection,
idea↔proposal linking, discussion-thread synthesis, amendment-drafting
help) — aligned with Logikascium's positioning. As for the **Rust
rewrite of the engine** considered in 2021: to be requalified — no
performance bottleneck is documented; keep it as a v3 option, never
before documentation and tests exist (a condition now essentially
met, which makes the evaluation possible when the day comes).

---

## 7. Calendar and indicative workloads

Initial hypothesis: a senior developer who knows the Zope/Pyramid
ecosystem (you), LLM-assisted, excluding project management.

| Phase | Key deliverable | Estimated load | **Status** |
|---|---|---|---|
| 0 — Taking back control | Repositories + forks under control, build repaired, decisions settled | 5–10 d | **Executed** |
| 1 — Golden master | Running legacy instance + CI replaying the tests | 10–20 d | **Executed** |
| 2 — Documentation | Published docs, auto-generated BPMN catalogue, docstrings | 15–30 d | **Executed** (review remaining) |
| 3 — 3.12 base | 4 packages green on a 2026 stack, server UI iso | 30–50 d | **Executed** |
| 4 — Frontend | SolidJS SPA on the core journeys (or option B htmx: 10–20 d) | 40–80 d | Not started |
| 5 — Data/ops | Tooled Data.fs migration, modern deployment | 10–20 d | **Partial** (rehearsal passed; real migration remaining) |

> **Achieved vs estimated.** The "v2 backend" perimeter (phases 0-3 +
> 5 minus the real migration), estimated at **70-130 days**, was
> executed **between 13 and 18 July 2026** — continuous LLM-assisted
> work under human review and steering, which moreover delivered
> beyond the perimeter (a 128-test campaign, four latent bugs fixed,
> the runbooks). The phase-4 estimate, which obeys other constraints
> (design, usage iterations), stands as an order of magnitude.

## 8. First-week actions

Fork/transfer the repositories and satellites, fix `git://` →
`https://` in the `sources.cfg`, tag `legacy-final`, lay a skeleton
CI, re-run the legacy Docker build, and write the first ADR ("KuneAgi
becomes the trunk, in co-governance with Cosmopolitical.coop;
everything stays under AGPL v3; the Python module names are frozen to
preserve the ZODB pickles"). Everything else flows from there.

> **Status: all executed.** Next actions (2026-07-18), in order:
> execute the **production migration** (`production-migration.md`
> runbook — pinned target, controlled wake-up); once the first real
> cycle is survived, pose the **v2.0.0** tags and roll the **`ecreall`
> merge-backs** (libraries fast-forward, KuneAgi and nova-ideo 2.0
> adoption merges); then, off the critical path: reactor step B (zmq
> removal), the pruned substanced fork for Pyramid 2, the pytest
> migration, the at-rest encryption audit (§4.7), the human review of
> the phase-2 documents.

---

## 9. Glossary (for the non-technical reader)

Deliberately simplified definitions, in the context of this document;
the practitioner will find assumed shortcuts.

**ADR (Architecture Decision Record)** — a short note recording a
technical decision, its reasons and the discarded alternatives, so
that the "why" is still known years later.

**AGPL v3, copyleft** — a free-software licence. "Copyleft" is its
central clause: whoever modifies the software — including to offer it
as an online service — must publish the modifications under the same
licence. This is what keeps the code a common good.

**Upstream, merge rights** — the "upstream" is a project's reference
repository, from which the copies derive and towards which
contributions flow back; "merge rights" designate who has authority to
accept the integration of those contributions.

**API, GraphQL** — an API is the standardised doorway through which
one program talks to another. GraphQL is a kind of API where the
requester describes precisely the data it wishes to receive, no more,
no less.

**Backend, frontend** — the backend is the part of the software
running on the server (data, business rules); the frontend is what
runs in the user's browser (the interface).

**Library, framework** — a library is a set of reusable functions a
program calls; a framework is a more structuring base that imposes a
way of organising the application (Pyramid on the server, SolidJS in
the browser).

**Branch, commit, tag (git)** — git is the tool that keeps the code's
history. A "commit" is a dated record of a modification; a "branch" is
a parallel development line (like the 2019 React branch, never
merged); a "tag" is a label posed on a precise state of the code so
one can return to it reliably (e.g. `legacy-final`).

**Breaking change** — an evolution of a component that breaks
compatibility: the programs using it must be adapted.

**Build, buildout** — the "build" is the operation that assembles the
source code and all its dependencies into an executable piece of
software; saying "the build is broken" means the software can no
longer be made from its sources. Buildout is the historical assembly
tool of the Zope ecosystem, used by the project, today superseded by
more common standards.

**CI (continuous integration)** — an automaton that, on every code
change, rebuilds the software and runs the tests, so that any
regression is detected immediately. GitHub Actions is GitHub's CI
service.

**Codegen (code generation)** — tooling that automatically produces
repetitive code (here, the TypeScript code matching the GraphQL
queries) — that many fewer human errors.

**CVE** — the public identifier of a documented security flaw.
"Dependencies with CVEs" are components whose flaws are known to all,
and exploitable as long as they are not updated.

**Dependency, pin** — a dependency is a third-party software brick the
project needs; there are dozens, and each one ages. To "pin" a version
is to freeze it precisely to guarantee a reproducible assembly — at
the price of the whole ageing if nobody refreshes the pins.

**Repository** — the space where a project's source code and its
entire history are kept (here, on GitHub).

**Docker, container, image** — technology that packs a piece of
software with its whole environment into a standardised "box" (the
image), executable identically on any server (the container).

**EOL (end of life)** — the date after which a piece of software
receives no fix at all, even for security. Python 3.6, the project's
historical base, has been EOL since December 2021.

**Fork** — an independent copy of a project, which then lives its own
life. KuneAgi is a fork of Nova-Ideo; "forking substanced" means
taking a copy that Logikascium will maintain itself.

**Golden master** — a reference version of the existing system, put
back in working order then frozen, against which every modernisation
step is compared to verify nothing regressed.

**Headless (components)** — interface components delivered "without
clothing": they provide the behaviour (menus, windows, keyboard
accessibility), the appearance remaining to be defined oneself.

**htmx** — a small library that makes server-produced pages
interactive; an economical alternative to a full JavaScript
application.

**Islands (architecture)** — the technique of placing modern
interactive components only where the page needs them, the rest
remaining classic server-rendered pages.

**JSX** — a syntax mixing interface markup and JavaScript code, common
to React and SolidJS — it is what keeps the old 2019 React code
readable as a specification.

**LLM (large language model)** — an artificial-intelligence program
trained on vast text corpora, used here as an assistant to document
and write code, always under human review.

**Monkey-patch** — an "on-the-fly" modification of a third-party
library's behaviour, without touching its source code. Effective but
invisible and fragile: hence the importance of inventorying them.

**Process engine, BPMN** — software that executes business processes
described as chains of steps, decisions and deadlines; BPMN is the
standard graphical notation of those processes. DaCE is the process
engine Nova-Ideo rests on.

**OIDC (OpenID Connect)** — the authentication standard enabling
"sign in with" an existing account (Google, a company account…); it
replaces the obsolete social connectors.

**Orphaned (project)** — a free-software project without an active
maintainer: it keeps working, but nobody fixes its flaws or adapts it
to change anymore. This is the case of substanced, the project's
foundation.

**PyPI, npm** — the public library "stores": PyPI for Python, npm for
JavaScript. Projects download their dependencies from them.

**Regression** — the reappearance of a defect, or the loss of a
feature, on the occasion of a change. Tests and the golden master
exist precisely to detect it.

**Server rendering, SPA** — two ways of building a web interface. In
server rendering, each page is made on the server then sent to the
browser (the current interface, 439 templates); in an SPA (Single
Page Application), the application loads once in the browser then
talks to the server through an API, without page reloads.

**Runtime** — the part of an interface framework the browser must
download and execute. A "tiny" runtime (SolidJS) means lighter, faster
pages.

**Signals (fine-grained reactivity)** — an interface technique where
each piece of data knows exactly which screen elements depend on it,
and updates only those. It is the heart of SolidJS, and the model the
industry converged on.

**Spike** — a disposable mini-prototype, time-boxed (here 3 to 5
days), made for the sole purpose of lifting a technical uncertainty
before committing to a worksite. One keeps the knowledge, not the
code.

**Strangler strategy (strangler fig)** — progressive modernisation in
which the new system wraps the old one and replaces it screen by
screen, until the old one can be unplugged — as opposed to the far
riskier brutal replacement in a single switch.

**Template, Chameleon** — a file describing the structure of an HTML
page, which the server fills with data when serving it. Chameleon is
the template system used (439 files).

**Unit, characterisation, end-to-end tests** — programs that
automatically verify the software's behaviour. Unit tests check each
brick in isolation; "characterisation" tests photograph the current
behaviour of the existing system to detect any involuntary change
during the modernisation; end-to-end tests (Playwright) drive a real
browser as a user would.

**TypeScript, typing** — the practice of declaring the nature of every
piece of data (number, text, idea, proposal…), which allows errors to
be detected before the program even runs. TypeScript brings it to
JavaScript.

**VDOM (Virtual DOM)** — React's technique of rebuilding an in-memory
model of the page on every change, then comparing it with the screen
to apply only the differences. SolidJS does without it, hence its
performance.

**Vendoring** — integrating a dependency's code directly into one's
own project so as to no longer depend on its original author; useful
when it is abandoned.

**Wrapper, bindings** — thin layers of code adapting a library to an
environment it was not designed for (e.g. adapting the ProseMirror
editor to SolidJS).

**ZODB, Data.fs, pickles** — ZODB is the object database of the Zope
ecosystem: it records the program's objects (ideas, proposals, votes)
directly into a single file, the Data.fs, in a format called "pickle".
Those records memorise the exact names of the Python modules: renaming
the modules would make the existing data unreadable — hence the
name-freeze rule.

### Terms added in revision 5

**Dual-stack** — the state of a single codebase able to run on two
environments: the historical 2017 stack (the golden master) and the
modern Python 3.12 stack. This is what allows the two behaviours to be
compared identically throughout the modernisation.

**Fast-forward** — the trivial git merge possible when one code line
is the simple continuation of another: nothing to reconcile, history
advances in one block.

**Adoption merge (stitch)** — a particular git merge that ties two
hitherto independent histories by making the old one a "parent" of the
new, without changing a line of the adopted code: the old history
stays consultable, the present is that of the modernised line.

**Migration rehearsal** — a full execution of the migration on a copy
of the real data, in an isolated environment with no outbound sending,
to prove the procedure before the big night.

**Consciously flipped test** — a characterisation test that pinned a
defect (it passed by asserting the broken behaviour) and which, once
the defect is fixed, is rewritten to guard the repair: the same test
changes sides, deliberately and traceably.

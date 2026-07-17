# Changelog

## Unreleased
### Fix — 2026-07-17
- **Modernisation regression** (caught by the Registration-arc tests):
  substanced's password API drifted across the stacks — the era class
  exposed ``pwd_manager``, the modern one a ``hash_new_password``
  staticmethod — which crashed the ``Preregistration`` constructor on
  Python 3.12. ``person.py`` now honours whichever is present; the
  encode → store → verify chain is proven end to end by the new tests.

### Unit-test campaign, first batches — 2026-07-16
- The suite grows from 29 to 78 tests, all green on BOTH stacks:
  T1 pins the 2006 French dates parser (16 tests — including the
  sharpened header bug: both boundary days escape the « sauf le … »
  filter); T1b pins the pure vein of `utilities/util` (18 tests) and
  the two pure `pseudo_react` helpers; T2a pins the `pseudo_react`
  metadata composers functionally (13 tests — dispatch registries,
  payload families, exact role-dependent action sets).
- Coverage: french_dates_parser 16 % → 57 %, ical_date_utility
  18 % → 41 %, utilities/util 22 % → 32 %, pseudo_react 16 % → 26 %.

### CI repair — 2026-07-16
- golden-master (red since M4): `graphql-wsgi` returns to the requires
  **conditionally** (`sys.version_info < (3,7)`) so the legacy
  buildout finds its era egg again; the modern stack keeps installing
  it from source.
- py312-tests (never green before): every pip line now runs under
  `constraints-modern.txt` (upstream drift caged — substanced
  1.0.post1 pulling pyramid 2.1); the era graphene stack is installed
  explicitly (promise stays on the era pin 2.0.2 and
  `tools/patch_graphql1_py312.py` ports it too); `graphql-wsgi` is
  requested by bare name (the constraint carries the pinned URL); the
  porting tool is located via `sysconfig` without importing the
  not-yet-ported packages; `lxml` becomes a declared requirement.


### Phase 3 / M4 — 2026-07-16 (Python 3.12)

- **The golden-master suite is green on Python 3.12: the same 29
  tests, 0 failures, 0 errors** — on dace/pontus/daceui 2.0.0.dev0,
  substanced 1.0b1, deform 3, Chameleon 4 (`constraints-modern.txt`).
  The legacy container keeps running the same working tree: the test
  harness is dual-stack (it first takes the historical path, and only
  falls back — mailer override, fresh storage — on the modern
  configuration conflict).
- Application changes are two one-line shims (``deform.compat`` in
  ``data_manager``, ``hypatia._compat`` in ``dateindex``); everything
  else is dependency archaeology: ``graphql-wsgi`` was withdrawn from
  PyPI (installed from its source, faassen/graphql-wsgi);
  ``html_diff_wrapper`` needs the maintained fork (py3.11 regex-flags
  fix); the GraphQL schema is graphene-1-era and the era stack
  (graphene 1.4.2, graphql-core 1.1, graphql-relay 0.4.5, promise 2.3
  override) is ported in place by ``tools/patch_graphql1_py312.py``.
- Version bumped to 2.0.0.dev0; a ``py312-tests`` workflow runs the
  suite on the modern stack alongside the golden-master workflow.


### Fork maintenance — 2026-07-13 (`michaellaunay/KuneAgi`)

- Repository forked from `ecreall/KuneAgi`; maintenance resumed by Michaël Launay (Logikascium), with KuneAgi as the reference trunk of the Nova-Ideo modernisation. Intellectual property: KuneAgi-specific developments are copyright Cosmopolitical.coop (rights transferred by Laurent Zibell); the underlying Nova-Ideo base is copyright Logikascium (Ecréall's IP, acquired in 2024). License unchanged (AGPL v3+).
- `README.rst` and `CHANGES.rst` converted to Markdown (`README.md`, `CHANGES.md`); README retitled from "Nova Ideo" to "KuneAgi" and rewritten with the repository status, converted operating instructions (annotated where outdated: Google "less secure apps" removed, historical Docker Hub release images unmaintained) and the modernisation roadmap.
- Build metadata updated: fork URLs, maintainer field, Markdown `long_description`, Python 3.6 classifier; minimal `pyproject.toml` added (PEP 518 `[build-system]` only — metadata stays in `setup.py` until the Phase 3 packaging migration); `MANIFEST.in` updated for Markdown files. The Python package name (`novaideo`) and all module paths are unchanged, to keep existing ZODB databases loadable.
- Buildout `sources.cfg`: `ecreall_dace`, `ecreall_pontus` and `ecreall_daceui` repointed to their maintained forks (`michaellaunay/{dace,pontus,daceui}`). Known remaining issue for Phase 1: the `cryptacular` source still references a Mercurial Bitbucket URL (service discontinued in 2020).
- Added a GitHub Actions **smoke** workflow (`python:3.6-buster` container: `compileall` over the `novaideo` package plus a packaging metadata check). The full legacy build (buildout + ZEO + test suite) is the Phase 1 "golden master" deliverable and will get its own workflow then.
- `.gitignore` extended to exclude delivery artifacts (patches, diffs, archives) and `git apply` leftovers.
- Bilingual documentation structure added (`docs/en/`, `docs/fr/`), including the worklog / fil de l'eau and the documentation policy (`docs/README.md`).

### Planned (modernisation roadmap → 2.0.0)

- Phase 1: reproducible legacy build + green CI (golden master).
- Phase 2: exhaustive documentation (architecture, auto-generated BPMN catalogue of the business processes, docstrings, glossary).
- Phase 3: Python 3.12, Pyramid 2.x, ZODB 6, maintained substanced fork; removal of dead dependencies (velruse → OIDC, yampy2 removed, xlrd → openpyxl, graphene 3); pytest; PEP 621 packaging with `uv`; ruff; gradual typing.
- Phase 4: frontend rebuilt on SolidJS + TypeScript + Vite over the GraphQL API (strangler-fig strategy).
- Phase 5: ZODB data-migration tooling, modern Docker images and CI/CD. Module dotted names (including the `novaideo` package) frozen to preserve ZODB pickles.
- Reunification with the nova-ideo lineage into a single trunk (KuneAgi specifics as configuration profiles), in coordination with Cosmopolitical.coop.

### Inherited unreleased changes (upstream `1.4.dev`, 2017–2023)

- No entries were recorded upstream for this version; the repository nevertheless contains the whole 2017–2019 Nova-Ideo development plus the KuneAgi-specific work up to 2023-03-02 — notably the cooperative-governance features (ballots, citizenship), German translations, mailer/SPF work and Docker updates.

## 1.3 — 2017-02-25

- When anonymous, use the browser language for the language of the user interface.
- Add Challenges feature.
- Add Questions feature.

## 1.2 — 2017-01-06

- Remove runtime pyramid_robot dependency, this avoids a dependency on robotsuite that depends on lxml. Add optional lxml dependency in `buildout:eggs`.

## 1.1 — 2016-09-15

- Improved ergonomics and fix some issues.

## 1.0 — 2016-06-28

- Initial version.

# Changelog

## Unreleased

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

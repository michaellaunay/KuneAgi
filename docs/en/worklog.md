# Worklog

Running log of the work on this repository, newest first.
Version française : [`../fr/worklog.md`](../fr/worklog.md).

## 2026-07-13

- Forked `ecreall/KuneAgi` to `michaellaunay/KuneAgi`; maintenance resumed by
  Michaël Launay (Logikascium). KuneAgi is the reference trunk of the
  Nova-Ideo modernisation (audit of July 2026).
- Converted `README.rst` and `CHANGES.rst` to Markdown; README retitled from
  "Nova Ideo" to "KuneAgi", rewritten with the repository status (copyright:
  Cosmopolitical.coop for the KuneAgi-specific work, Logikascium for the
  Nova-Ideo base; AGPL v3+ for the whole) and the modernisation roadmap;
  outdated operating instructions annotated (Google "less secure apps",
  historical Docker Hub images).
- Updated build metadata (`setup.py`: fork URLs, maintainer field, Markdown
  long description, Python 3.6 classifier); added a minimal PEP 518
  `pyproject.toml`; updated `MANIFEST.in`. Package name `novaideo` and module
  paths unchanged (ZODB pickles).
- `sources.cfg`: `ecreall_dace`, `ecreall_pontus`, `ecreall_daceui` repointed
  to their maintained forks. Known Phase 1 issue: `cryptacular` still points
  to a Mercurial Bitbucket URL (service discontinued in 2020).
- Added a smoke CI workflow (`python:3.6-buster`: `compileall` on `novaideo`
  + packaging metadata check); the full legacy build is the Phase 1
  deliverable.
- Ignored delivery artifacts (`*.patch`, `*.diff`, archives) and `git apply`
  leftovers in `.gitignore`.
- Established the bilingual documentation structure (`docs/en`, `docs/fr`)
  and this worklog.
- Restored the fork-maintenance changes: the initial commit (8883913)
  contained only the *unapplied* delivery patch file — the apply command
  referenced `../kuneagi-fork-maj.patch` while the file had been saved inside
  the repository, so the `&&` chain stopped at `--check` and the stray file
  was committed alone. The patch content is now applied and the stray file
  removed (and ignored from now on).


## 2026-07-14

- Started the Phase 1 "golden master" of the application: a new
  `golden-master` workflow rebuilds the historical Docker image (the
  Dockerfile runs the full buildout inside `docker build`, with the era pins
  the project already carried: setuptools 42, zc.buildout 2.13.3) and
  replays `bin/test -s novaideo`.
- Era fixes applied to the Dockerfile: Debian stretch apt sources repointed
  to archive.debian.org (stretch archived); the varnish 4.1 packagecloud
  repository made best-effort with the distro varnish as fallback (the test
  suite does not use varnish); `cryptacular` preinstalled from its
  maintained 2.x rewrite — same pip-preinstall mechanism the historical
  image used for 1.5.5 — with `bcrypt`/`cffi`/`pycparser` pinned in
  `versions.cfg`; the dead Mercurial Bitbucket source replaced by the
  maintained repository. Expected to be iterative, like the library CIs.
- Golden-master iteration 1 (local build): apt on the archived stretch
  fetched fine but `upgrade -y` refused the packages — the stretch signing
  keys have *expired* (EXPKEYSIG), and Check-Valid-Until only bypasses the
  Release date check, not signature verification. Archive sources are now
  marked `[trusted=yes]` (accepted, documented trade-off for a frozen
  legacy CI). Preemptively upgraded pip to <22 inside the image: stretch's
  pip 19 predates the manylinux2014 tags of the bcrypt/cffi wheels.
- Aligned everything on Docker Compose v2 (`docker compose`): fixed
  `run.sh`, where an earlier global replace had also mangled the *file
  name* (`-f docker compose-dev.yml`), breaking every wrapped command;
  made the attach target naming-agnostic via `docker compose ps -q`
  (v2 names containers with dashes, not underscores); converted the
  remaining `docker-compose` commands in the README; removed the obsolete
  `version: '2'` attribute from the four compose files (v2 warns on it).

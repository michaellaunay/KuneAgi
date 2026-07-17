# The modern harness (Python 3.12)

*Phase 3 companion. French version: [`../fr/modern-harness.md`](../fr/modern-harness.md).*

Three layers, all versioned:

1. **The test harnesses** (`novaideo/testing.py` and each library's
   `testing.py`) are dual-stack: they first take the historical path,
   and only fall back (mailer override, fresh storage) on the modern
   configuration conflict. The same working tree serves both stacks.
2. **Isolated, reproducible runs**: each repo ships `tox.ini` +
   `constraints-modern.txt` + a `py312-tests` workflow — what the CI
   executes, installing the trio from their git masters.
3. **The integrated development environment** — this document. For
   cross-repo work (the M5+ daily routine), tox's git-master installs
   are wrong: you want the sibling checkouts *editable*. That is what
   `tools/bootstrap-modern.sh` rebuilds:

```bash
git clone git@github.com:michaellaunay/dace.git
git clone git@github.com:michaellaunay/pontus.git
git clone git@github.com:michaellaunay/daceui.git
git clone git@github.com:michaellaunay/KuneAgi.git
cd KuneAgi
tools/bootstrap-modern.sh
.venv312/bin/python -m zope.testrunner --test-path=. -s novaideo
```

Siblings present → editable installs; absent → git masters. The script
ends by running `tools/patch_graphql1_py312.py` (the GraphQL schema is
graphene-1-era; the tool ports the installed era stack — idempotent).

The legacy twin is unchanged: `./run.sh test -s novaideo` runs the
certified 2017 container. Both must stay green.

## Hardening (CI repair, 2026-07-16)

A cold resolver on the runners exposed what long-lived venvs masked;
the install discipline is now:

- **every** pip line runs under `constraints-modern.txt` (upstream
  drift caged — e.g. substanced `1.0.post1` pulling pyramid 2.1);
- `graphql-wsgi` is requested **by bare name**: the constraint carries
  the pinned source URL (requesting the URL directly conflicts with
  the sha-pinned constraint);
- the era graphene stack is installed explicitly
  (`graphene==1.4.2 graphql-core==1.1 graphql-relay==0.4.5`,
  promise on its era pin `2.0.2`), then
  `tools/patch_graphql1_py312.py` ports it **in place — promise
  included**;
- the packages to port are located through `sysconfig` **without
  importing them** (importing crashes before the port: the bootstrap
  paradox);
- `lxml` is a declared requirement of `novaideo` (bs4's parser);
- on the legacy side, `graphql-wsgi` sits in the requires
  **conditionally** (`sys.version_info < (3,7)`): that requirement is
  how the buildout finds the era egg in its cache.

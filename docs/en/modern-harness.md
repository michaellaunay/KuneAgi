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

## Writing behaviour-level tests (campaign idioms)

The 2026-07 characterisation campaign settled these idioms — use them
when pinning new process families:

- **Drive actions by node id** through `getAllBusinessAction`, and
  FILTER by `process_id` when the node name is common (`creat` exists
  on several families at the root).
- **Content-creating actions** take
  `{'_object_data': <content instance>}`; required extra keys surface
  as `KeyError` — pin them (`explanation`, `roles`, the nested
  `change_password` mapping, `password`).
- **Pin action sets exactly** (set equality of
  `process_id + '.' + node_id`) per role and per state — the gates ARE
  the security model. Remember the dace-level SiteAdmin override: the
  admin sees every action, so negative pins need a plain member or the
  anonymous user.
- **Authors must be real Persons**: alert flows read `user_locale`,
  which the raw substanced admin lacks.
- **Substanced's audit subscriber** (LoggedIn) reads
  `request.context` — set it (the root) on the test request.
- **Importing a behaviours module** from a test primes the historical
  import cycle: `import novaideo.views` first.
- **Coverage**: measure with `--source=novaideo` (module form) on the
  single test module — pointing coverage at a process sub-package
  breaks collection; run the full suite bare, in its own invocation.

### Conducting a ballot in a test

The decision node of a moderation ballot completes at the BALLOT
DEADLINE in production (the vote sub-process is timer-closed). After
the last vote, invoke the node's completion directly — the very code
path the deadline runs:

    action = subject.ballot_processes[0].get_actions('start_ballot')[0]
    action.after_execution(subject, request)

Read the REAL electors from the ballot report (the draw is random and
every member is in the urn — including freshly created ones).

### Running the suite (two halves)

The full run has outgrown one invocation; certify in two passes whose
counts must sum:

    zope.testrunner ... -m '!novaideo.tests.test_(question_lifecycle|user_lifecycle|invitation_lifecycle|registration_lifecycle|reports_lifecycle|ballot_conduct|moderate_registration)'
    zope.testrunner ... -m 'novaideo.tests.test_(question_lifecycle|user_lifecycle|invitation_lifecycle|registration_lifecycle|reports_lifecycle|ballot_conduct|moderate_registration)'

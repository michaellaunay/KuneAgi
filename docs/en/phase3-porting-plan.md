# Phase 3 — porting plan (Python 3.12)

*Adopted 2026-07-16, the day the golden master was certified (29/29 on the rebuilt 2017 stack). Every step of this plan is measured against that suite. French version: [`../fr/phase3-porting-plan.md`](../fr/phase3-porting-plan.md).*

## 1. Goal and non-negotiables

Bring the whole stack — `dace`, `pontus`, `daceui`, `novaideo`/KuneAgi — to **Python 3.12** on maintained dependencies, with the same behaviour.

Non-negotiables:

1. **Behavioural parity.** The 29-test suite is the arbiter: it stays green on the legacy container at every step, and the port is *done* when the same suite is green on 3.12 (milestone M4). Divergences are facts to characterise, never opinions.
2. **ZODB continuity.** Existing databases must keep loading. Persistent classes keep their module paths and class names — the `novaideo` package name is already frozen for this very reason, and the rule now extends to the libraries: **a persistent class never moves**. Measured consequence: `dace.processdefinition.core.Transaction` and `Path` derive from `Persistent` and are stored on every process (`global_transaction`); the once-considered `Transaction → PathTransaction` rename is therefore **rejected** — the disambiguation lives in the docs (Phase 2) instead.
3. Bilingual documentation and per-repo worklogs continue; the working agreements of Phase 1–2 (patches via `git apply`, English code, `docker compose` v2) are unchanged.
4. AGPL v3; upstream attribution (Ecréall, Nova-Ideo) preserved.

## 2. The measuring instrument (dual-stack testing)

- **Legacy**: the certified container — `./run.sh test -s novaideo` and the `golden-master` GitHub workflow. It never breaks; it is the certificate.
- **Modern**: per repo, a `py312` tox environment and a CI job, born *allowed-to-fail* and promoted to *required* at each milestone.
- **One variable at a time**: the same test runner (`zope.testrunner`) on both stacks until M4; a pytest migration is post-M4 comfort, not a port prerequisite.
- Starting point, measured 2026-07-16: the four code bases already **compile on Python 3.12.3** (`compileall` clean; a handful of `SyntaxWarning: invalid escape sequence` in regexes to raw-string at M0).

## 3. Current vs target stack

| Component | 2017 pin | Target | Notes |
|---|---|---|---|
| Python | 3.6.15 | **3.12** | syntax already compiles (see §2) |
| pyramid | 1.9.1 | 2.0.x | authn/authz merged into the security policy; `pyramid.compat` gone |
| substanced | 1.0a1 (egg) | **fork `michaellaunay/substanced`** | upstream dormant; port the *used surface only* (Appendix A) |
| ZODB / persistent / BTrees / transaction | 5.3.0 / 4.2.4 / 4.4.1 / 2.1.2 | 6.x / 6.x / 6.x / 4.x | API stable, pickle-compatible |
| hypatia | 0.3 | 0.4+ | vendor if dormant on 3.12 |
| deform / colander | 2.0a2 / 1.0 | 2.0.15 / 2.x | pontus owns its widget templates (Phase-2 map); diff pass at M2 |
| Chameleon | 3.1 | 4.x | template strictness checked early (M2) |
| pyzmq / tornado | 14.4.1 / 3.2.2 | 26.x / **dropped** | reactor goes asyncio (§4) |
| venusian | 1.1.0 | 3.x | scan API stable |
| rwproperty | 1.0 | **removed** | dead upstream; replaced by plain properties |
| waitress | 1.1.0 | 3.x | |
| zc.buildout + mr.developer | 2.13.3 | **pip + pyproject** | `constraints-modern.txt` mirrors `constraints-legacy.txt`; sibling checkouts via `pip install -e ../dace` |
| cryptacular | fork 2.0 | unchanged | already modern (Phase 1, byte-for-byte parity proven) |

## 4. The reactor — the one architectural change

Today (dace): a tornado `IOLoop` thread, woken through a zmq PUSH/PULL command socket (`tcp://127.0.0.1:12345`), `DelayedCallback` timers, and `Job`/`EventJob` re-establishing site and user per run, armed *after commit*.

Target: **the same public API** — `push_event_callback_after_commit`, `push_callback_after_commit`, `DelayedCallback.start/stop`, `Job`, `EventJob` — over an **asyncio** loop thread.

- **Step A (transport-preserving, part of M1)**: keep the zmq command socket (pyzmq 26 ships `zmq.asyncio`); replace the IOLoop with `asyncio.new_event_loop()` in the reactor thread; `DelayedCallback` becomes a thin `loop.call_later` wrapper.
- **Step B (optional, post-M4)**: drop zmq for `asyncio.run_coroutine_threadsafe` + a queue — today's reality is single-process.

Parity specification: the Phase-2 docstrings double as the spec — crawler cadence (2 s re-arm), `ConditionalEvent` 1 s repoll, after-commit arming order, `ConflictError` retry-once, user/site re-establishment. M1 adds a small timing test for the first two.

## 5. Order of battle (bottom-up strangler)

- **M0 — scaffolding** (all repos): `[modern]` extra + `constraints-modern.txt`; tox `py312`; CI job *allowed-to-fail*; raw-string the escape-sequence warnings; static sweep (`pyupgrade --py312` **with review — never auto-rewrite a persistent class**, `ruff` triage) producing the py2-remnant fix list.
- **M1 — dace green on 3.12** (88 tests): dependency ladder (zope.interface → persistent/BTrees/ZODB → transaction → hypatia), substanced fork bootstrapped with the Appendix-A surface, reactor Step A, the three monkey-patches of `patches.py` re-evaluated one by one (each has its Phase-2 docstring stating why it exists).
- **M2 — pontus green on 3.12**: deform 2.0.15 / colander 2 (widget-template diff), `substanced.form`/`file` from the fork, and the confirmed py2 remnant fixed: `view_operation.py:724-726` subscripts `dict.items()` — unreachable by the suite (it would crash on any Python 3), to fix-or-delete *with a test*.
- **M3 — daceui green on 3.12.**
- **M4 — KuneAgi 29/29 on 3.12**: application sweep, buildout → pip, template/static pass, `constraints-modern.txt` frozen. **Acceptance: the same 29 tests, `zope.testrunner`, 0 failures 0 errors on 3.12 — with the legacy container still green.**
- **M5 — data-migration rehearsal**: a copy of a real-era `Data.fs` opened on the modern stack — evolve chain, `zeopack`, reindex, click-through; the runbook written into `docs/`.
- **Post-M4 window** (API changes, *non-persisted only*, each candidate pickle-audited first): `action_infomrations → action_informations` (method, safe, shim kept one release); pontus `Mutltiple*` resource names (JS-facing — coordinated rename); `nember` parameter; `InclusiveGatewayDefinition`: implement or remove (recommendation: remove, raise explicitly); boundary events: documented as unsupported (runtime FIXME).

## 6. Risk register

1. **substanced fork scope creep** → Appendix-A surface list; port on demand, nothing speculative.
2. **ZODB pickle breakage** → the never-move rule; `zodbupdate` dry-runs at M5; renames only after a pickle audit.
3. **deform/colander template drift** → pontus's templates are inventoried (Phase 2); M2 does a visual diff pass.
4. **hypatia dormancy** → vendor fallback, same license.
5. **Latent py2 remnants** (the `.items()[...]` class) → M0 static sweep; every finding becomes fix-plus-test or documented-dead.
6. **Reactor timing parity** → docstring spec + M1 timing test.
7. **Chameleon 4 strictness** → template compile pass at M2, not M4.
8. **Unexercised evolve chain** from era databases → M5 rehearsal on a real copy.

## Appendix A — the substanced surface actually used (measured 2026-07-16)

dace: `catalog` (`oid_from_resource`, catalog wiring), `content` (`content`), `db` (`root_factory`), `event` (`ObjectModified`, `RootAdded`, `subscribe_removed`), `folder` (`Folder`), `interfaces` (`IFolder`, `IRoot`, `IPrincipal`, `IService`, `IUserLocator`), `locking` (`lock_resource`), `objectmap` (`ObjectMap`, `find_objectmap`), `principal` (`DefaultUserLocator`, `User`), `property` (`PropertySheet`), `root` (`Root`), `schema` (`Schema`), `sdi` (`LEFT`, `mgmt_view`), `util` (`find_catalogs`, `find_objectmap`, `is_service`, `set_oid`, helpers).

pontus and daceui add: `file` (+ `file.views`), `form`, plus the shared `content`/`db`/`schema`/`util`/`interfaces`.

Regenerate with:

```bash
grep -rhoE "from substanced[.a-z_]* import [a-zA-Z_, ()]+" <pkg> --include="*.py" | sort -u
```

## Appendix B — M0/M1 kickoff checklist

1. dace: add `pyproject` `[modern]` extra + `constraints-modern.txt` (targets of §3); tox `py312`; CI job (allowed-to-fail).
2. Raw-string the regex escape warnings (three files in novaideo, none in the libraries).
3. Bootstrap the substanced fork: import the Appendix-A modules, delete the rest, make `dace`'s import surface resolve.
4. Dependency ladder until `zope.testrunner -s dace` collects; then fix forward, test by test.
5. Reactor Step A behind the same API; timing test for crawler/repoll.
6. Worklog every session; legacy CI stays green throughout.

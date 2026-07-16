#!/usr/bin/env bash
# Recreate the Phase-3 "modern harness": the integrated Python 3.12
# development environment the milestones M1-M4 were certified in.
#
# Sibling checkouts (../dace, ../pontus, ../daceui) are installed
# *editable* when present — the cross-repo workflow — and fall back to
# their git masters otherwise. Idempotent; safe to re-run.
#
# Usage:
#   tools/bootstrap-modern.sh            # creates .venv312
#   VENV=/path/to/venv tools/bootstrap-modern.sh
#   .venv312/bin/python -m zope.testrunner --test-path=. -s novaideo
set -euo pipefail
cd "$(dirname "$0")/.."

VENV="${VENV:-.venv312}"
PYTHON="${PYTHON:-python3.12}"
command -v "$PYTHON" >/dev/null || PYTHON=python3

"$PYTHON" -m venv "$VENV"
PIP="$VENV/bin/pip"
PY="$VENV/bin/python"
"$PIP" -q install --upgrade pip

# --- the ecreall trio: editable siblings first, git masters otherwise
for name in dace pontus daceui; do
    if [ -d "../$name" ]; then
        echo "== $name: editable sibling (../$name)"
        "$PIP" -q install -c constraints-modern.txt -e "../$name"
    else
        echo "== $name: git master"
        "$PIP" -q install -c constraints-modern.txt "ecreall_$name @ git+https://github.com/michaellaunay/$name.git"
    fi
done

# --- git-sourced dependencies (see constraints-modern.txt header)
"$PIP" -q install -c constraints-modern.txt \
    "deform_treepy @ git+https://github.com/ecreall/deform_treepy.git" \
    "html_diff_wrapper @ git+https://github.com/michaellaunay/html_diff_wrapper.git" \
    "graphql-wsgi"   # pinned by URL in constraints-modern.txt

# --- the application, under the certified pins
"$PIP" -q install -c constraints-modern.txt \
    "graphene==1.4.2" "graphql-core==1.1" "graphql-relay==0.4.5"
"$PIP" -q install -c constraints-modern.txt zope.testrunner -e .

# --- port the graphene-1 era stack in place (idempotent)
# locate WITHOUT importing: the era stack crashes on import until
# this very tool has patched it (bootstrap paradox)
SP=$("$PY" -c "import sysconfig; print(sysconfig.get_paths()['purelib'])")
"$PY" tools/patch_graphql1_py312.py \
    "$SP/graphql" "$SP/graphene" "$SP/graphql_relay" "$SP/promise"

echo
echo "Modern harness ready: $VENV"
echo "  $VENV/bin/python -m zope.testrunner --test-path=. -s novaideo"

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
        "$PIP" -q install -e "../$name"
    else
        echo "== $name: git master"
        "$PIP" -q install "ecreall_$name @ git+https://github.com/michaellaunay/$name.git"
    fi
done

# --- git-sourced dependencies (see constraints-modern.txt header)
"$PIP" -q install \
    "deform_treepy @ git+https://github.com/ecreall/deform_treepy.git" \
    "html_diff_wrapper @ git+https://github.com/michaellaunay/html_diff_wrapper.git" \
    "graphql_wsgi @ git+https://github.com/faassen/graphql-wsgi.git"

# --- the application, under the certified pins
"$PIP" -q install -c constraints-modern.txt zope.testrunner -e .

# --- port the graphene-1 era stack in place (idempotent)
"$PY" tools/patch_graphql1_py312.py \
    "$("$PY" -c 'import graphql, os; print(os.path.dirname(graphql.__file__))')" \
    "$("$PY" -c 'import graphene, os; print(os.path.dirname(graphene.__file__))')" \
    "$("$PY" -c 'import graphql_relay, os; print(os.path.dirname(graphql_relay.__file__))')"

echo
echo "Modern harness ready: $VENV"
echo "  $VENV/bin/python -m zope.testrunner --test-path=. -s novaideo"

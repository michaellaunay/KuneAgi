#!/usr/bin/env python3
# Copyright (c) 2026 by Logikascium under licence AGPL terms
# available on http://www.gnu.org/licenses/agpl.html

# licence: AGPL
# author: Michaël Launay

"""Regenerate the presentation screenshots (docs/images/presentation).

A deliberately readable Playwright scaffold. Each figure of
``docs/{en,fr}/presentation.md`` carries a stable semantic name; this
script logs into a running instance, walks the documented journeys and
rewrites each figure under that same name — the documents update
without a single text edit.

Configuration through environment variables:

    DOCSHOTS_BASE_URL   e.g. https://my-instance   (required)
    DOCSHOTS_LOGIN      login of a member account  (required)
    DOCSHOTS_PASSWORD   its password               (required)
    DOCSHOTS_VIEWPORT   WIDTHxHEIGHT, default 1280x800

Usage:

    python tools/docshots.py              # every figure
    python tools/docshots.py fig-02 fig-03  # a selection (prefix match)

The SHOTS table below is the contract: one entry per figure, with the
path to open and the optional gestures (clicks, fills) bringing the
subject on screen. Entries marked ``'todo': True`` still need their
gestures refined on the first run against the modernised instance —
the script skips them with a notice instead of failing.
"""
import os
import sys

VIEWPORT = os.environ.get('DOCSHOTS_VIEWPORT', '1280x800')

# --- the contract -----------------------------------------------------
# name          -> the figure's file stem in docs/images/presentation
# path          -> URL path to open (joined to DOCSHOTS_BASE_URL)
# actions       -> optional list of (verb, selector[, value]) executed
#                  in order before the capture: ('click', sel),
#                  ('fill', sel, value), ('wait', sel)
# full_page     -> capture the whole page (default: viewport only)
# todo          -> gestures still to refine on a live instance
SHOTS = [
    {'name': 'fig-01-idea-form', 'path': '/',
     'actions': [('click', 'text=Ajouter une idée')], 'todo': True},
    {'name': 'fig-02-home-list', 'path': '/'},
    {'name': 'fig-03-home-blocks', 'path': '/',
     'actions': [('click', '.blocs-view, [data-view="blocs"]')],
     'todo': True},
    {'name': 'fig-04-idea-fork', 'path': '/ideas', 'todo': True},
    {'name': 'fig-05-dependency-graph', 'path': '/ideas', 'todo': True},
    {'name': 'fig-06-challenge-create', 'path': '/challenges',
     'todo': True},
    {'name': 'fig-07-challenge-published', 'path': '/'},
    {'name': 'fig-08-proposal-from-idea', 'path': '/ideas',
     'todo': True},
    {'name': 'fig-09-group-join', 'path': '/proposals', 'todo': True},
    {'name': 'fig-10-iteration-state', 'path': '/proposals',
     'todo': True},
    {'name': 'fig-11-iteration-vote', 'path': '/proposals',
     'todo': True},
    {'name': 'fig-12-iteration-vote-result', 'path': '/proposals',
     'todo': True},
    {'name': 'fig-13-work-mode-choice', 'path': '/proposals',
     'todo': True},
    {'name': 'fig-14-change-validation', 'path': '/proposals',
     'todo': True},
    {'name': 'fig-15-amendments-creation', 'path': '/proposals',
     'todo': True},
    {'name': 'fig-16-majority-judgment', 'path': '/proposals',
     'todo': True},
    {'name': 'fig-17-new-version', 'path': '/proposals', 'todo': True},
    {'name': 'fig-18-discussions', 'path': '/', 'todo': True},
    {'name': 'fig-19-notifications', 'path': '/', 'todo': True},
    {'name': 'fig-20-steering-opinion', 'path': '/ideas',
     'todo': True},
]

OUTPUT_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    'docs', 'images', 'presentation')


def _require(name):
    value = os.environ.get(name)
    if not value:
        sys.exit('missing environment variable: ' + name)
    return value


def _login(page, base_url, login, password):
    page.goto(base_url + '/login')
    page.fill('input[name="email"], input[name="login"]', login)
    page.fill('input[name="password"]', password)
    page.click('button[type="submit"], input[type="submit"]')
    page.wait_for_load_state('networkidle')


def _capture(page, base_url, shot):
    page.goto(base_url + shot['path'])
    page.wait_for_load_state('networkidle')
    for action in shot.get('actions', []):
        verb, selector = action[0], action[1]
        if verb == 'click':
            page.click(selector)
        elif verb == 'fill':
            page.fill(selector, action[2])
        elif verb == 'wait':
            page.wait_for_selector(selector)
        page.wait_for_load_state('networkidle')
    # the historical figures are jpg or png: keep each stem's
    # existing extension so the markdown references stay valid
    existing = [f for f in os.listdir(OUTPUT_DIR)
                if f.startswith(shot['name'] + '.')]
    filename = existing[0] if existing else shot['name'] + '.png'
    target = os.path.join(OUTPUT_DIR, filename)
    page.screenshot(path=target,
                    full_page=shot.get('full_page', False))
    return target


def main(argv):
    from playwright.sync_api import sync_playwright

    base_url = _require('DOCSHOTS_BASE_URL').rstrip('/')
    login = _require('DOCSHOTS_LOGIN')
    password = _require('DOCSHOTS_PASSWORD')
    width, height = (int(part) for part in VIEWPORT.split('x'))
    wanted = argv[1:]

    selected = [shot for shot in SHOTS
                if not wanted or any(shot['name'].startswith(w)
                                     for w in wanted)]
    done, skipped = 0, 0
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(
            viewport={'width': width, 'height': height})
        _login(page, base_url, login, password)
        for shot in selected:
            if shot.get('todo'):
                print('SKIP (gestures to refine): ' + shot['name'])
                skipped += 1
                continue
            target = _capture(page, base_url, shot)
            print('OK  ' + target)
            done += 1
        browser.close()
    print('%d captured, %d to refine' % (done, skipped))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))

# Copyright (c) 2026 by Logikascium under licence AGPL terms
# available on http://www.gnu.org/licenses/agpl.html

# licence: AGPL
# author: Michaël Launay

"""Keycloak single sign-on for KuneAgi (OpenID Connect).

Members managed elsewhere — typically created by AlirPunkto and
federated by Keycloak — sign in to KuneAgi through the standard OpenID
Connect authorization-code flow, and are auto-provisioned as Persons
on first login (mirroring, line for line, what ``ConfirmRegistration``
does for the local registration path).

The plugin is inert unless configured. Add to the ``[app:main]``
section of the deployment ``.ini``::

    oidc_sso.issuer = https://keycloak.example.org/realms/myrealm
    oidc_sso.client_id = kuneagi
    oidc_sso.client_secret = ...
    # optional:
    oidc_sso.button_title = Keycloak
    oidc_sso.scope = openid profile email
    oidc_sso.provision = true
    oidc_sso.verify_tls = true
    oidc_sso.timeout = 10

Two anonymous routes are then registered:

``/oidcsso/login``
    stores ``state``/``nonce`` in the session and redirects to the
    Keycloak authorization endpoint (discovered through
    ``<issuer>/.well-known/openid-configuration``);

``/oidcsso/callback``
    the ``redirect_uri`` to declare in the Keycloak client — exchanges
    the code at the token endpoint, validates the ID token claims
    (``iss``, ``aud``, ``exp``, ``nonce``), cross-checks ``sub``
    against the UserInfo endpoint, then finds the Person by e-mail or
    provisions one, and logs it in exactly as the login form does.

Security notes. The ID token is received straight from the token
endpoint over server-validated TLS with client authentication, the
one flow where OpenID Connect Core (§3.1.3.7.6) allows the TLS channel
to stand in for a local signature check; its claims are still fully
validated and the ``sub`` is confirmed against UserInfo. The identity
claims of record are taken from UserInfo. Keycloak's
``preferred_username`` — the AlirPunkto pseudonym when Keycloak
federates the cooperative's LDAP — becomes the Person's pseudonym,
so members keep the same public name across applications.
"""
import base64
import json
import secrets
import time

try:  # tolerate exotic deployments; the plugin then refuses to start
    import requests
except ImportError:  # pragma: no cover
    requests = None

from pyramid.httpexceptions import HTTPFound
from pyramid.security import remember, NO_PERMISSION_REQUIRED

from substanced.util import get_oid, find_service
from substanced.event import LoggedIn

from dace.util import find_catalog, getSite, name_chooser
from dace.objectofcollaboration.principal.util import (
    grant_roles,
    has_role)

from novaideo import log, my_locale_negotiator
from novaideo.content.interface import IPerson
from novaideo.content.person import Person


SETTINGS_PREFIX = 'oidc_sso.'
SESSION_STATE = 'oidc_sso.state'
SESSION_NONCE = 'oidc_sso.nonce'
SESSION_CAME_FROM = 'oidc_sso.came_from'
DISCOVERY_ATTR = '_oidc_sso_discovery'


def get_settings(registry):
    """Return the plugin settings as a plain dict (empty if unset)."""
    settings = getattr(registry, 'settings', None) or {}
    result = {}
    for key, value in settings.items():
        if key.startswith(SETTINGS_PREFIX):
            result[key[len(SETTINGS_PREFIX):]] = value
    return result


def is_configured(registry):
    conf = get_settings(registry)
    return bool(conf.get('issuer') and conf.get('client_id')
                and conf.get('client_secret'))


def _bool(value, default=True):
    if value is None:
        return default
    return str(value).strip().lower() in ('true', 'yes', 'on', '1')


def _http_get_json(url, **kw):
    """GET a JSON document. Isolated for the tests to substitute."""
    response = requests.get(url, **kw)
    response.raise_for_status()
    return response.json()


def _http_post_json(url, data, **kw):
    """POST a form and read JSON back. Isolated for the tests."""
    response = requests.post(url, data=data, **kw)
    response.raise_for_status()
    return response.json()


def discover(registry):
    """Fetch and cache the issuer's OpenID Connect discovery document."""
    cached = getattr(registry, DISCOVERY_ATTR, None)
    if cached is not None:
        return cached
    conf = get_settings(registry)
    issuer = conf['issuer'].rstrip('/')
    url = issuer + '/.well-known/openid-configuration'
    document = _http_get_json(
        url,
        timeout=float(conf.get('timeout', 10)),
        verify=_bool(conf.get('verify_tls')))
    setattr(registry, DISCOVERY_ATTR, document)
    return document


def _login_url(request):
    return request.resource_url(request.root, '@@login')


def _callback_url(request):
    try:
        return request.route_url('oidc_sso_callback')
    except Exception:  # harness requests carry no route mapper
        return request.application_url.rstrip('/') + '/oidcsso/callback'


def login_button(request):
    """What the login page needs to offer SSO — or None when inert."""
    if not is_configured(request.registry):
        return None
    conf = get_settings(request.registry)
    try:
        url = request.route_url('oidc_sso_login')
    except Exception:
        url = request.application_url.rstrip('/') + '/oidcsso/login'
    return {'url': url,
            'title': conf.get('button_title', 'Keycloak')}


def _fail(request, message):
    """Flash (when the toolbar is there) and return to the login page."""
    log.warning('oidc_sso: %s', message)
    sdiapi = getattr(request, 'sdiapi', None)
    if sdiapi is not None:
        try:
            sdiapi.flash(message, 'danger')
        except Exception:  # pragma: no cover
            pass
    return HTTPFound(location=_login_url(request))


def begin_login(request):
    """Route ``oidc_sso_login``: send the browser to Keycloak."""
    if not is_configured(request.registry):
        return _fail(request, 'SSO is not configured')
    conf = get_settings(request.registry)
    document = discover(request.registry)
    state = secrets.token_urlsafe(24)
    nonce = secrets.token_urlsafe(24)
    request.session[SESSION_STATE] = state
    request.session[SESSION_NONCE] = nonce
    came_from = request.params.get('came_from')
    if not came_from:
        came_from = request.resource_url(request.root)
    request.session[SESSION_CAME_FROM] = came_from
    query = [
        ('response_type', 'code'),
        ('client_id', conf['client_id']),
        ('redirect_uri', _callback_url(request)),
        ('scope', conf.get('scope', 'openid profile email')),
        ('state', state),
        ('nonce', nonce),
    ]
    try:  # py3
        from urllib.parse import urlencode
    except ImportError:  # pragma: no cover
        from urllib import urlencode
    location = document['authorization_endpoint'] + '?' + urlencode(query)
    return HTTPFound(location=location)


def _decode_id_token(id_token):
    """Read the claims of a compact JWT (payload only, no signature).

    Acceptable here because the token comes straight from the token
    endpoint over verified TLS with client authentication (OpenID
    Connect Core §3.1.3.7.6); the claims themselves are then checked.
    """
    parts = id_token.split('.')
    if len(parts) != 3:
        raise ValueError('malformed ID token')
    payload = parts[1]
    padding = '=' * (-len(payload) % 4)
    decoded = base64.urlsafe_b64decode(payload + padding)
    return json.loads(decoded.decode('utf-8'))


def _validate_claims(claims, conf, nonce):
    issuer = conf['issuer'].rstrip('/')
    if str(claims.get('iss', '')).rstrip('/') != issuer:
        return 'issuer mismatch'
    audience = claims.get('aud')
    if isinstance(audience, (list, tuple)):
        if conf['client_id'] not in audience:
            return 'audience mismatch'
    elif audience != conf['client_id']:
        return 'audience mismatch'
    expires = claims.get('exp')
    if not expires or float(expires) < time.time() - 60:
        return 'expired ID token'
    if not nonce or claims.get('nonce') != nonce:
        return 'nonce mismatch'
    return None


def _exchange_code(request, code):
    """Trade the authorization code for tokens at the token endpoint."""
    conf = get_settings(request.registry)
    document = discover(request.registry)
    return _http_post_json(
        document['token_endpoint'],
        data={
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': _callback_url(request),
            'client_id': conf['client_id'],
            'client_secret': conf['client_secret'],
        },
        timeout=float(conf.get('timeout', 10)),
        verify=_bool(conf.get('verify_tls')))


def _fetch_userinfo(request, access_token):
    conf = get_settings(request.registry)
    document = discover(request.registry)
    return _http_get_json(
        document['userinfo_endpoint'],
        headers={'Authorization': 'Bearer ' + access_token},
        timeout=float(conf.get('timeout', 10)),
        verify=_bool(conf.get('verify_tls')))


def find_person_by_email(email):
    """The very lookup the login form performs (identifier + IPerson)."""
    novaideo_catalog = find_catalog('novaideo')
    dace_catalog = find_catalog('dace')
    identifier_index = novaideo_catalog['identifier']
    object_provides_index = dace_catalog['object_provides']
    query = object_provides_index.any([IPerson.__identifier__]) & \
        identifier_index.any([email])
    users = list(query.execute().all())
    return users[0] if users else None


def provision_person(request, claims):
    """Create the Person for a first SSO login.

    Mirrors ``ConfirmRegistration.start``: same container, same
    ``name_chooser`` naming (pseudonym first), same roles, same state.
    The local password is set to an unguessable random value — the
    account authenticates through Keycloak.
    """
    root = getSite()
    data = {
        'first_name': claims.get('given_name') or '',
        'last_name': claims.get('family_name') or '',
        'email': claims['email'],
        'pseudonym': claims.get('preferred_username') or '',
        'locale': claims.get('locale') or my_locale_negotiator(request),
    }
    person = Person(**data)
    # Person.password stores the *hash* (ConfirmRegistration pours an
    # already-encoded initial_password into it); hash through the
    # proper channel so the account has an unguessable local secret.
    person.set_password(secrets.token_urlsafe(32))
    principals = find_service(root, 'principals')
    name = data['pseudonym'] if data['pseudonym'] else \
        (data['first_name'] + ' ' + data['last_name']).strip()
    if not name:
        name = claims['email'].split('@', 1)[0]
    users = principals['users']
    name = name_chooser(users, name=name)
    users[name] = person
    grant_roles(person, roles=('Member',))
    grant_roles(person, (('Owner', person),))
    person.state.append('active')
    person.init_annotations()
    person.reindex()
    log.info('oidc_sso: provisioned member for a first SSO login')
    return person


def finish_login(request):
    """Route ``oidc_sso_callback``: validate, find or provision, log in."""
    if not is_configured(request.registry):
        return _fail(request, 'SSO is not configured')
    if request.params.get('error'):
        return _fail(request, 'SSO refused: '
                     + str(request.params.get('error')))
    conf = get_settings(request.registry)
    state = request.session.pop(SESSION_STATE, None)
    nonce = request.session.pop(SESSION_NONCE, None)
    if not state or request.params.get('state') != state:
        return _fail(request, 'SSO state mismatch')
    code = request.params.get('code')
    if not code:
        return _fail(request, 'SSO code missing')
    try:
        tokens = _exchange_code(request, code)
        claims = _decode_id_token(tokens['id_token'])
    except Exception as error:
        return _fail(request, 'SSO token exchange failed: ' + str(error))
    problem = _validate_claims(claims, conf, nonce)
    if problem:
        return _fail(request, 'SSO ' + problem)
    try:
        userinfo = _fetch_userinfo(request, tokens.get('access_token', ''))
    except Exception as error:
        return _fail(request, 'SSO userinfo failed: ' + str(error))
    if userinfo.get('sub') != claims.get('sub'):
        return _fail(request, 'SSO subject mismatch')
    merged = dict(claims)
    merged.update(userinfo)
    email = (merged.get('email') or '').strip().lower()
    if not email:
        return _fail(request, 'SSO account has no e-mail address')
    person = find_person_by_email(email)
    if person is None:
        if not _bool(get_settings(request.registry).get('provision')):
            return _fail(request, 'SSO account is not a member here')
        merged['email'] = email
        person = provision_person(request, merged)
    if not (has_role(user=person, role=('SiteAdmin',))
            or 'active' in getattr(person, 'state', [])):
        return _fail(
            request,
            'Disabled account! Contact the site administrator '
            'to activate your account.')
    came_from = request.session.pop(
        SESSION_CAME_FROM, request.resource_url(request.root))
    headers = remember(request, get_oid(person))
    request.registry.notify(
        LoggedIn(email, person, request.root, request))
    return HTTPFound(location=came_from, headers=headers)


def includeme(config):
    """Register the SSO routes — only when the plugin is configured."""
    if not is_configured(config.registry):
        log.info('oidc_sso: not configured, plugin inert')
        return
    if requests is None:  # pragma: no cover
        log.error('oidc_sso: the requests library is missing')
        return
    config.add_route('oidc_sso_login', '/oidcsso/login')
    config.add_route('oidc_sso_callback', '/oidcsso/callback')
    config.add_view(
        begin_login, route_name='oidc_sso_login',
        permission=NO_PERMISSION_REQUIRED)
    config.add_view(
        finish_login, route_name='oidc_sso_callback',
        permission=NO_PERMISSION_REQUIRED)
    log.info('oidc_sso: routes registered for issuer %s',
             get_settings(config.registry).get('issuer'))

# Copyright (c) 2026 by Logikascium under licence AGPL terms
# available on http://www.gnu.org/licenses/agpl.html

# licence: AGPL
# author: Michaël Launay

"""Characterisation of the Keycloak / OpenID Connect SSO plugin.

The network is never touched: discovery, the token exchange and the
UserInfo call are substituted at module level, exactly where
``novaideo.oidc_sso`` isolates them. What is pinned here is the
contract of the plugin itself: an inert module when unconfigured, the
authorization redirect carrying ``state``/``nonce``, the callback
refusing a forged ``state``, a wrong ``nonce`` or an account without
e-mail, first-login provisioning that mirrors ``ConfirmRegistration``
(container, pseudonym-first naming, Member+Owner roles, active state),
the login of an existing member, and the refusal of a deactivated one.
"""
import base64
import json

from pyramid.httpexceptions import HTTPFound

from dace.objectofcollaboration.principal.util import (
    grant_roles,
    has_role)
from substanced.util import find_service
from dace.util import name_chooser

from novaideo.testing import FunctionalTests
from novaideo.content.person import Person
from novaideo import oidc_sso

ISSUER = 'https://keycloak.example.org/realms/coop'
DISCOVERY = {
    'authorization_endpoint': ISSUER + '/protocol/openid-connect/auth',
    'token_endpoint': ISSUER + '/protocol/openid-connect/token',
    'userinfo_endpoint': ISSUER + '/protocol/openid-connect/userinfo',
}


def _jwt(payload):
    """A compact, unsigned JWT — the plugin reads the payload only."""
    def _part(data):
        raw = json.dumps(data).encode('utf-8')
        return base64.urlsafe_b64encode(raw).rstrip(b'=').decode('ascii')
    return _part({'alg': 'none'}) + '.' + _part(payload) + '.sig'


class TestOidcSso(FunctionalTests):

    def setUp(self):
        super(TestOidcSso, self).setUp()
        self.default_novaideo_config()
        self.root = self.request.root
        self.admin = self.request.user
        # substanced's audit subscriber (LoggedIn) reads request.context
        self.request.context = self.root
        self._saved = (oidc_sso.discover, oidc_sso._exchange_code,
                       oidc_sso._fetch_userinfo)

    def tearDown(self):
        (oidc_sso.discover, oidc_sso._exchange_code,
         oidc_sso._fetch_userinfo) = self._saved
        settings = self.request.registry.settings
        for key in list(settings):
            if key.startswith(oidc_sso.SETTINGS_PREFIX):
                del settings[key]
        super(TestOidcSso, self).tearDown()

    def _configure(self, **extra):
        settings = self.request.registry.settings
        settings['oidc_sso.issuer'] = ISSUER
        settings['oidc_sso.client_id'] = 'kuneagi'
        settings['oidc_sso.client_secret'] = 'sekrit'
        for key, value in extra.items():
            settings['oidc_sso.' + key] = value
        oidc_sso.discover = lambda registry: DISCOVERY

    def _wire_provider(self, claims, userinfo=None):
        """Substitute the two network legs of the callback."""
        tokens = {'access_token': 'at-123', 'id_token': _jwt(claims)}
        oidc_sso._exchange_code = lambda request, code: tokens
        if userinfo is None:
            userinfo = {'sub': claims.get('sub'),
                        'email': claims.get('email')}
        oidc_sso._fetch_userinfo = lambda request, token: userinfo

    def _prime_session(self, state='st-1', nonce='no-1',
                       came_from='http://example.com/after'):
        self.request.session[oidc_sso.SESSION_STATE] = state
        self.request.session[oidc_sso.SESSION_NONCE] = nonce
        self.request.session[oidc_sso.SESSION_CAME_FROM] = came_from

    def _claims(self, email, nonce='no-1', **extra):
        claims = {
            'iss': ISSUER,
            'aud': 'kuneagi',
            'exp': 4102444800,  # 2100-01-01: never expires in tests
            'nonce': nonce,
            'sub': 'sub-' + email,
            'email': email,
        }
        claims.update(extra)
        return claims

    def _callback(self, state='st-1', code='code-1'):
        self.request.GET.clear()
        self.request.GET['state'] = state
        self.request.GET['code'] = code
        return oidc_sso.finish_login(self.request)

    def _make_member(self, email, pseudonym=''):
        """A member built with the very primitives provisioning uses."""
        person = Person(first_name='Ada', last_name='L',
                        email=email, pseudonym=pseudonym)
        person.set_password('adapass')
        principals = find_service(self.root, 'principals')
        users = principals['users']
        name = name_chooser(users, name=pseudonym or 'Ada L')
        users[name] = person
        grant_roles(person, roles=('Member',))
        grant_roles(person, (('Owner', person),))
        person.state.append('active')
        person.init_annotations()
        person.reindex()
        return person

    def test_unconfigured_plugin_is_inert(self):
        self.assertFalse(oidc_sso.is_configured(self.request.registry))
        self.assertIsNone(oidc_sso.login_button(self.request))
        response = oidc_sso.begin_login(self.request)
        self.assertIsInstance(response, HTTPFound)
        self.assertIn('@@login', response.location)

    def test_begin_login_redirects_to_keycloak_with_state_and_nonce(self):
        self._configure()
        self.request.GET['came_from'] = 'http://example.com/idea'
        response = oidc_sso.begin_login(self.request)
        self.assertIsInstance(response, HTTPFound)
        self.assertTrue(response.location.startswith(
            DISCOVERY['authorization_endpoint'] + '?'))
        session = self.request.session
        state = session[oidc_sso.SESSION_STATE]
        nonce = session[oidc_sso.SESSION_NONCE]
        self.assertIn('state=' + state, response.location)
        self.assertIn('nonce=' + nonce, response.location)
        self.assertIn('client_id=kuneagi', response.location)
        self.assertIn('response_type=code', response.location)
        self.assertEqual(session[oidc_sso.SESSION_CAME_FROM],
                         'http://example.com/idea')
        button = oidc_sso.login_button(self.request)
        self.assertTrue(button['url'].endswith('/oidcsso/login'))
        self.assertEqual(button['title'], 'Keycloak')

    def test_callback_rejects_a_forged_state(self):
        self._configure()
        self._prime_session(state='st-good')
        self._wire_provider(self._claims('mallory@example.com'))
        response = self._callback(state='st-forged')
        self.assertIn('@@login', response.location)
        # the one-shot state is consumed either way
        self.assertNotIn(oidc_sso.SESSION_STATE, self.request.session)

    def test_callback_rejects_a_wrong_nonce(self):
        self._configure()
        self._prime_session(nonce='no-expected')
        self._wire_provider(self._claims('eve@example.com',
                                         nonce='no-other'))
        response = self._callback()
        self.assertIn('@@login', response.location)

    def test_callback_logs_in_an_existing_member(self):
        self._configure()
        person = self._make_member('ada@example.com')
        self._prime_session()
        self._wire_provider(self._claims('ada@example.com'))
        response = self._callback()
        self.assertIsInstance(response, HTTPFound)
        self.assertEqual(response.location, 'http://example.com/after')
        self.assertNotIn(oidc_sso.SESSION_CAME_FROM, self.request.session)
        self.assertIs(
            oidc_sso.find_person_by_email('ada@example.com'), person)

    def test_callback_provisions_a_first_login(self):
        self._configure()
        claims = self._claims('zora@example.com',
                              given_name='Zora',
                              family_name='Neale',
                              preferred_username='zora')
        self._prime_session()
        self._wire_provider(claims)
        response = self._callback()
        self.assertIsInstance(response, HTTPFound)
        self.assertEqual(response.location, 'http://example.com/after')
        person = oidc_sso.find_person_by_email('zora@example.com')
        self.assertIsNotNone(person)
        self.assertEqual(person.pseudonym, 'zora')
        self.assertIn('active', person.state)
        self.assertTrue(has_role(user=person, role=('Member',)))
        users = find_service(self.root, 'principals')['users']
        self.assertIn(person, list(users.values()))
        # the local password is unusable: SSO is the way in
        self.assertFalse(person.check_password('zora'))

    def test_provisioning_can_be_disabled(self):
        self._configure(provision='false')
        self._prime_session()
        self._wire_provider(self._claims('ghost@example.com'))
        response = self._callback()
        self.assertIn('@@login', response.location)
        self.assertIsNone(
            oidc_sso.find_person_by_email('ghost@example.com'))

    def test_callback_requires_an_email(self):
        self._configure()
        claims = self._claims('noone@example.com')
        del claims['email']
        self._prime_session()
        self._wire_provider(claims, userinfo={'sub': claims['sub']})
        response = self._callback()
        self.assertIn('@@login', response.location)
        self.assertIsNone(
            oidc_sso.find_person_by_email('noone@example.com'))

    def test_a_deactivated_member_is_refused(self):
        self._configure()
        person = self._make_member('dora@example.com')
        person.state = ['deactivated']
        person.reindex()
        self._prime_session()
        self._wire_provider(self._claims('dora@example.com'))
        response = self._callback()
        self.assertIn('@@login', response.location)
        self.assertNotEqual(response.location, 'http://example.com/after')

# Keycloak single sign-on (SSO)

KuneAgi can delegate authentication to a Keycloak server through
standard OpenID Connect — the natural companion of an AlirPunkto
deployment, where AlirPunkto creates the cooperative's members,
Keycloak federates them (usually over the same LDAP), and KuneAgi
welcomes them without a second account.

## Keycloak side

In the realm that holds the members, create a client:

- **Client ID**: `kuneagi` (or your choice — mirror it in the ini)
- **Client authentication**: on (confidential client); note the secret
- **Flow**: *Standard flow* only (authorization code)
- **Valid redirect URI**: `https://<your-kuneagi>/oidcsso/callback`
- **Scopes**: the defaults suffice; `email` and `profile` must stay

With AlirPunkto members federated from LDAP, Keycloak's
`preferred_username` is the member's **pseudonym** (the LDAP `cn`
AlirPunkto writes): KuneAgi picks it up so the member keeps the same
public name across both applications. An e-mail address is required —
accounts without one are refused.

## KuneAgi side

Add to the `[app:main]` section of the deployment ini:

    oidc_sso.issuer = https://keycloak.example.org/realms/myrealm
    oidc_sso.client_id = kuneagi
    oidc_sso.client_secret = %(KEYCLOAK_CLIENT_SECRET)s
    # optional:
    oidc_sso.button_title = Keycloak
    oidc_sso.scope = openid profile email
    oidc_sso.provision = true
    oidc_sso.verify_tls = true
    oidc_sso.timeout = 10

Unset, the plugin is inert: no route, no button, nothing changes.
Configured, the login page grows a "Log in with Keycloak" button and
the two anonymous routes `/oidcsso/login` and `/oidcsso/callback`
come alive.

## What a first login does

When an authenticated Keycloak account has no matching Person (lookup
by e-mail, the same catalog query the login form runs), the plugin
provisions one exactly as `ConfirmRegistration` would: stored under
`principals['users']` with pseudonym-first naming through
`name_chooser`, granted `Member` and `Owner` of itself, state
`active`, indexed. Its local password is set to an unguessable random
secret — Keycloak is the way in. Set `oidc_sso.provision = false` to
refuse unknown accounts instead (members must then pre-exist).

Deactivated members stay deactivated: SSO respects the same gate as
the login form (`active` state or `SiteAdmin`).

## Security notes

The flow carries a per-attempt `state` (CSRF) and `nonce` (replay),
both single-use. ID-token claims are validated (`iss`, `aud`, `exp`,
`nonce`) and the subject is cross-checked against the UserInfo
endpoint; the token itself arrives straight from the token endpoint
over verified TLS with client authentication — the one flow where
OpenID Connect Core (§3.1.3.7.6) lets the TLS channel stand in for a
local signature check. Keep the client secret out of version control
(environment substitution in the ini, as above).

## Current limits

Logout stays local (no RP-initiated logout at Keycloak yet); all SSO
members arrive as `Member` (no Keycloak-role mapping); the button is
a plain link on the login page rather than a citizen of the historic
connectors framework. Each is a reasonable evolution once the need
shows.

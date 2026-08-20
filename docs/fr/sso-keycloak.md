# Authentification unique Keycloak (SSO)

KuneAgi peut déléguer l'authentification à un serveur Keycloak via
OpenID Connect standard — le compagnon naturel d'un déploiement
AlirPunkto : AlirPunkto crée les membres de la coopérative, Keycloak
les fédère (généralement sur le même LDAP), et KuneAgi les accueille
sans second compte.

## Côté Keycloak

Dans le realm qui porte les membres, créer un client :

- **Client ID** : `kuneagi` (ou autre — refléter dans le ini)
- **Client authentication** : activée (client confidentiel) ; noter
  le secret
- **Flux** : *Standard flow* seul (code d'autorisation)
- **Valid redirect URI** : `https://<votre-kuneagi>/oidcsso/callback`
- **Scopes** : les défauts suffisent ; garder `email` et `profile`

Avec des membres AlirPunkto fédérés depuis LDAP, le
`preferred_username` de Keycloak est le **pseudonyme** du membre (le
`cn` LDAP écrit par AlirPunkto) : KuneAgi le reprend, et le membre
garde le même nom public dans les deux applications. Une adresse de
courriel est requise — les comptes qui n'en ont pas sont refusés.

## Côté KuneAgi

Ajouter à la section `[app:main]` du ini de déploiement :

    oidc_sso.issuer = https://keycloak.example.org/realms/monrealm
    oidc_sso.client_id = kuneagi
    oidc_sso.client_secret = %(KEYCLOAK_CLIENT_SECRET)s
    # optionnel :
    oidc_sso.button_title = Keycloak
    oidc_sso.scope = openid profile email
    oidc_sso.provision = true
    oidc_sso.verify_tls = true
    oidc_sso.timeout = 10

Non configuré, le plugin est inerte : aucune route, aucun bouton,
rien ne change. Configuré, la page de connexion gagne un bouton
« Log in with Keycloak » et les deux routes anonymes
`/oidcsso/login` et `/oidcsso/callback` s'éveillent.

## Ce que fait une première connexion

Quand un compte Keycloak authentifié n'a pas de Personne
correspondante (recherche par courriel, la requête catalogue même du
formulaire de connexion), le plugin la provisionne exactement comme
le ferait `ConfirmRegistration` : rangée sous `principals['users']`
avec le nommage pseudonyme-d'abord de `name_chooser`, rôles `Member`
et `Owner` d'elle-même, état `active`, indexée. Son mot de passe
local est un secret aléatoire indevinable — Keycloak est la porte
d'entrée. Poser `oidc_sso.provision = false` pour refuser les comptes
inconnus (les membres doivent alors préexister).

Les membres désactivés le restent : le SSO respecte la même porte que
le formulaire (état `active` ou `SiteAdmin`).

## Notes de sécurité

Le flux porte un `state` (anti-CSRF) et un `nonce` (anti-rejeu) à
usage unique par tentative. Les claims du jeton d'identité sont
validés (`iss`, `aud`, `exp`, `nonce`) et le sujet est recoupé avec
le point UserInfo ; le jeton lui-même arrive en direct du point
token sur TLS vérifié avec authentification du client — le seul flux
où OpenID Connect Core (§3.1.3.7.6) permet au canal TLS de tenir lieu
de vérification locale de signature. Garder le secret client hors du
dépôt (substitution d'environnement dans le ini, comme ci-dessus).

## Limites actuelles

La déconnexion reste locale (pas encore de déconnexion initiée côté
Keycloak) ; tous les membres SSO arrivent `Member` (pas de
correspondance des rôles Keycloak) ; le bouton est un lien simple sur
la page de connexion plutôt qu'un citoyen du cadre historique des
connecteurs. Autant d'évolutions raisonnables quand le besoin se
présentera.

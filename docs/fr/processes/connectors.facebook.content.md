# connectors.facebook.content

## Processus `facebookprocess`

```mermaid
flowchart TD
    n_start(("start"))
    n_login["<b>Login with Facebook</b><br/><i>LogIn</i>"]
    n_create["<b>Add a Facebook connector</b><br/><i>CreateConnector</i>"]
    n_configure["<b>Configure</b><br/><i>Configure</i>"]
    n_remove["<b>Remove</b><br/><i>Remove</i>"]
    n_pg{"+"}
    n_eg{"X"}
    n_end((("end")))
    n_start --> n_pg
    n_pg --> n_login
    n_login --> n_eg
    n_pg --> n_create
    n_create --> n_eg
    n_pg --> n_configure
    n_configure --> n_eg
    n_pg --> n_remove
    n_remove --> n_eg
    n_eg --> n_end
```

| Nœud | Type | Titre | Behaviors |
|---|---|---|---|
| `login` | activity | Login with Facebook | `LogIn` |
| `create` | activity | Add a Facebook connector | `CreateConnector` |
| `configure` | activity | Configure | `Configure` |
| `remove` | activity | Remove | `Remove` |


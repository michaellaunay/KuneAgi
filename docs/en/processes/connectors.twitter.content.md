# connectors.twitter.content

## Process `twitterprocess`

```mermaid
flowchart TD
    n_start(("start"))
    n_login["<b>Login with Twitter</b><br/><i>LogIn</i>"]
    n_create["<b>Add a Twitter connector</b><br/><i>CreateConnector</i>"]
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

| Node | Type | Title | Behaviors |
|---|---|---|---|
| `login` | activity | Login with Twitter | `LogIn` |
| `create` | activity | Add a Twitter connector | `CreateConnector` |
| `configure` | activity | Configure | `Configure` |
| `remove` | activity | Remove | `Remove` |


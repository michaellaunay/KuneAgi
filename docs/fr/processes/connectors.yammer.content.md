# connectors.yammer.content

## Processus `yammerprocess`

```mermaid
flowchart TD
    n_start(("start"))
    n_login["<b>Login with Yammer</b><br/><i>LogIn</i>"]
    n_create["<b>Add a Yammer connector</b><br/><i>CreateConnector</i>"]
    n_configure["<b>Configure</b><br/><i>Configure</i>"]
    n_remove["<b>Remove</b><br/><i>Remove</i>"]
    n_import_messages["<b>Import</b><br/><i>Import</i>"]
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
    n_pg --> n_import_messages
    n_import_messages --> n_eg
    n_eg --> n_end
```

| Nœud | Type | Titre | Behaviors |
|---|---|---|---|
| `login` | activity | Login with Yammer | `LogIn` |
| `create` | activity | Add a Yammer connector | `CreateConnector` |
| `configure` | activity | Configure | `Configure` |
| `remove` | activity | Remove | `Remove` |
| `import_messages` | activity | Import | `Import` |


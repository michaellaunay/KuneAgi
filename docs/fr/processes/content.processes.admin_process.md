# content.processes.admin_process

## Processus `adminprocess`

```mermaid
flowchart TD
    n_start(("start"))
    n_pg{"+"}
    n_configure_site["<b>Configure</b><br/><i>ConfigureSite</i>"]
    n_managekeywords["<b>Manage keywords</b><br/><i>ManageKeywords</i>"]
    n_extract["<b>Extract</b><br/><i>Extract</i>"]
    n_eg{"X"}
    n_end((("end")))
    n_start --> n_pg
    n_pg --> n_configure_site
    n_configure_site --> n_eg
    n_pg --> n_extract
    n_extract --> n_eg
    n_pg --> n_managekeywords
    n_managekeywords --> n_eg
    n_eg --> n_end
```

| Nœud | Type | Titre | Behaviors |
|---|---|---|---|
| `configure_site` | activity | Configure | `ConfigureSite` |
| `managekeywords` | activity | Manage keywords | `ManageKeywords` |
| `extract` | activity | Extract | `Extract` |


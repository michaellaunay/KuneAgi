# connectors.core.content

## Process `connectorsmanagement`

```mermaid
flowchart TD
    n_start(("start"))
    n_see["<b>Connectors</b><br/><i>SeeConnectors</i>"]
    n_add["<b>Connectors</b><br/><i>AddConnectors</i>"]
    n_pg{"+"}
    n_eg{"X"}
    n_end((("end")))
    n_start --> n_pg
    n_pg --> n_see
    n_see --> n_eg
    n_pg --> n_add
    n_add --> n_eg
    n_eg --> n_end
```

| Node | Type | Title | Behaviors |
|---|---|---|---|
| `see` | activity | Connectors | `SeeConnectors` |
| `add` | activity | Connectors | `AddConnectors` |


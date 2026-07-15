# content.processes.novaideo_process_management

## Processus `novaideoprocessmanagement`

```mermaid
flowchart TD
    n_start(("start"))
    n_pg{"+"}
    n_update["<b>Update processes</b><br/><i>Update</i>"]
    n_eg{"X"}
    n_end((("end")))
    n_start --> n_pg
    n_pg --> n_update
    n_update --> n_eg
    n_eg --> n_end
```

| Nœud | Type | Titre | Behaviors |
|---|---|---|---|
| `update` | activity | Update processes | `Update` |


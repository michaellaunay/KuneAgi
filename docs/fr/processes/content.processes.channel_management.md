# content.processes.channel_management

This module represent the Channel management process definition
powered by the dace engine. This process is unique, which means that
this process is instantiated only once.

## Processus `channelmanagement`

```mermaid
flowchart TD
    n_start(("start"))
    n_pg{"+"}
    n_subscribe["<b>Subscribe</b><br/><i>Subscribe</i>"]
    n_unsubscribe["<b>Unsubscribe</b><br/><i>Unsubscribe</i>"]
    n_eg{"X"}
    n_end((("end")))
    n_start --> n_pg
    n_pg --> n_subscribe
    n_subscribe --> n_eg
    n_pg --> n_unsubscribe
    n_unsubscribe --> n_eg
    n_eg --> n_end
```

| Nœud | Type | Titre | Behaviors |
|---|---|---|---|
| `subscribe` | activity | Subscribe | `Subscribe` |
| `unsubscribe` | activity | Unsubscribe | `Unsubscribe` |


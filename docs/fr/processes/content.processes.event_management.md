# content.processes.event_management

This module represent the Event management process definition
powered by the dace engine. This process is unique, which means that
this process is instantiated only once.

## Processus `eventmanagement`

```mermaid
flowchart TD
    n_start(("start"))
    n_pg{"+"}
    n_create["<b>Organise a discussion event</b><br/><i>Create</i>"]
    n_edit["<b>Edit</b><br/><i>Edit</i>"]
    n_remove["<b>Remove</b><br/><i>Remove</i>"]
    n_see_events["<b>The organised discussion events</b><br/><i>SeeRelatedEvents</i>"]
    n_see["<b>Details</b><br/><i>SeeEvent</i>"]
    n_eg{"X"}
    n_end((("end")))
    n_start --> n_pg
    n_pg --> n_create
    n_create --> n_eg
    n_pg --> n_edit
    n_edit --> n_eg
    n_pg --> n_remove
    n_remove --> n_eg
    n_pg --> n_see_events
    n_see_events --> n_eg
    n_pg --> n_see
    n_see --> n_eg
    n_eg --> n_end
```

| Nœud | Type | Titre | Behaviors |
|---|---|---|---|
| `create` | activity | Organise a discussion event | `Create` |
| `edit` | activity | Edit | `Edit` |
| `remove` | activity | Remove | `Remove` |
| `see_events` | activity | The organised discussion events | `SeeRelatedEvents` |
| `see` | activity | Details | `SeeEvent` |


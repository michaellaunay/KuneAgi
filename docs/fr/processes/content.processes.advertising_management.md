# content.processes.advertising_management

## Processus `advertisingmanagement`

```mermaid
flowchart TD
    n_start(("start"))
    n_pg{"+"}
    n_creat["<b>Create an announcement</b><br/><i>CreateWebAdvertising</i>"]
    n_edit["<b>Edit the announcement</b><br/><i>EditWebAdvertising</i>"]
    n_see["<b>Details</b><br/><i>SeeWebAdvertising</i>"]
    n_see_all["<b>The announcements</b><br/><i>SeeAdvertisings</i>"]
    n_publish["<b>Publish</b><br/><i>PublishAdvertising</i>"]
    n_archive["<b>Archive</b><br/><i>ArchiveAdvertising</i>"]
    n_remove["<b>Remove</b><br/><i>RemoveAdvertising</i>"]
    n_eg{"X"}
    n_end((("end")))
    n_start --> n_pg
    n_pg --> n_creat
    n_creat --> n_eg
    n_pg --> n_see
    n_see --> n_eg
    n_pg --> n_see_all
    n_see_all --> n_eg
    n_pg --> n_edit
    n_edit --> n_eg
    n_pg --> n_publish
    n_publish --> n_eg
    n_pg --> n_archive
    n_archive --> n_eg
    n_pg --> n_remove
    n_remove --> n_eg
    n_eg --> n_end
```

| Nœud | Type | Titre | Behaviors |
|---|---|---|---|
| `creat` | activity | Create an announcement | `CreateWebAdvertising` |
| `edit` | activity | Edit the announcement | `EditWebAdvertising` |
| `see` | activity | Details | `SeeWebAdvertising` |
| `see_all` | activity | The announcements | `SeeAdvertisings` |
| `publish` | activity | Publish | `PublishAdvertising` |
| `archive` | activity | Archive | `ArchiveAdvertising` |
| `remove` | activity | Remove | `RemoveAdvertising` |


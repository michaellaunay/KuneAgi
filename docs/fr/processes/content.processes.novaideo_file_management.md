# content.processes.novaideo_file_management

## Processus `novaideofilemanagement`

```mermaid
flowchart TD
    n_start(("start"))
    n_pg{"+"}
    n_creat["<b>Create a document</b><br/><i>CreateFile</i>"]
    n_editfile["<b>Edit the file</b><br/><i>EditFile</i>"]
    n_seefile["<b>Details</b><br/><i>SeeFile</i>"]
    n_publish["<b>Publish</b><br/><i>Publish</i>"]
    n_private["<b>Privatise</b><br/><i>Private</i>"]
    n_seefiles["<b>See files</b><br/><i>SeeFiles</i>"]
    n_eg{"X"}
    n_end((("end")))
    n_start --> n_pg
    n_pg --> n_creat
    n_creat --> n_eg
    n_pg --> n_seefile
    n_seefile --> n_eg
    n_pg --> n_publish
    n_publish --> n_eg
    n_pg --> n_private
    n_private --> n_eg
    n_pg --> n_editfile
    n_editfile --> n_eg
    n_pg --> n_seefiles
    n_seefiles --> n_eg
    n_eg --> n_end
```

| Nœud | Type | Titre | Behaviors |
|---|---|---|---|
| `creat` | activity | Create a document | `CreateFile` |
| `editfile` | activity | Edit the file | `EditFile` |
| `seefile` | activity | Details | `SeeFile` |
| `publish` | activity | Publish | `Publish` |
| `private` | activity | Privatise | `Private` |
| `seefiles` | activity | See files | `SeeFiles` |


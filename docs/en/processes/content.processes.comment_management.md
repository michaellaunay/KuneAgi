# content.processes.comment_management

This module represent the Comment management process definition
powered by the dace engine. This process is unique, which means that
this process is instantiated only once.

## Process `commentmanagement`

```mermaid
flowchart TD
    n_start(("start"))
    n_pg{"+"}
    n_respond["<b>Answer</b><br/><i>Respond</i>"]
    n_edit["<b>Edit</b><br/><i>Edit</i>"]
    n_remove["<b>Remove</b><br/><i>Remove</i>"]
    n_pin["<b>Pin</b><br/><i>Pin</i>"]
    n_unpin["<b>Unpin</b><br/><i>Unpin</i>"]
    n_transformtoidea["<b>Transform into an idea</b><br/><i>TransformToIdea</i>"]
    n_transformtoquestion["<b>Transform into a question</b><br/><i>TransformToQuestion</i>"]
    n_see["<b>Details</b><br/><i>SeeComment</i>"]
    n_eg{"X"}
    n_end((("end")))
    n_start --> n_pg
    n_pg --> n_respond
    n_respond --> n_eg
    n_pg --> n_transformtoidea
    n_transformtoidea --> n_eg
    n_pg --> n_transformtoquestion
    n_transformtoquestion --> n_eg
    n_pg --> n_edit
    n_edit --> n_eg
    n_pg --> n_remove
    n_remove --> n_eg
    n_pg --> n_pin
    n_pin --> n_eg
    n_pg --> n_unpin
    n_unpin --> n_eg
    n_pg --> n_see
    n_see --> n_eg
    n_eg --> n_end
```

| Node | Type | Title | Behaviors |
|---|---|---|---|
| `respond` | activity | Answer | `Respond` |
| `edit` | activity | Edit | `Edit` |
| `remove` | activity | Remove | `Remove` |
| `pin` | activity | Pin | `Pin` |
| `unpin` | activity | Unpin | `Unpin` |
| `transformtoidea` | activity | Transform into an idea | `TransformToIdea` |
| `transformtoquestion` | activity | Transform into a question | `TransformToQuestion` |
| `see` | activity | Details | `SeeComment` |


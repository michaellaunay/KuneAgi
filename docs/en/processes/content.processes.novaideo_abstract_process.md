# content.processes.novaideo_abstract_process

## Process `novaideoabstractprocess`

```mermaid
flowchart TD
    n_start(("start"))
    n_pg{"+"}
    n_select["<b>Follow</b><br/><i>SelectEntity, SelectEntityAnonymous</i>"]
    n_deselect["<b>Unfollow</b><br/><i>DeselectEntity</i>"]
    n_addreaction["<b>Add a reaction</b><br/><i>AddReaction</i>"]
    n_updatereaction["<b>Update the reaction</b><br/><i>UpdateReaction</i>"]
    n_adddeadline["<b>Add the next deadline</b><br/><i>AddDeadLine</i>"]
    n_editdeadline["<b>Edit the current deadline</b><br/><i>EditDeadLine</i>"]
    n_eg{"X"}
    n_end((("end")))
    n_start --> n_pg
    n_pg --> n_select
    n_select --> n_eg
    n_pg --> n_addreaction
    n_addreaction --> n_eg
    n_pg --> n_updatereaction
    n_updatereaction --> n_eg
    n_pg --> n_deselect
    n_deselect --> n_eg
    n_pg --> n_adddeadline
    n_adddeadline --> n_eg
    n_pg --> n_editdeadline
    n_editdeadline --> n_eg
    n_eg --> n_end
```

| Node | Type | Title | Behaviors |
|---|---|---|---|
| `select` | activity | Follow | `SelectEntity`, `SelectEntityAnonymous` |
| `deselect` | activity | Unfollow | `DeselectEntity` |
| `addreaction` | activity | Add a reaction | `AddReaction` |
| `updatereaction` | activity | Update the reaction | `UpdateReaction` |
| `adddeadline` | activity | Add the next deadline | `AddDeadLine` |
| `editdeadline` | activity | Edit the current deadline | `EditDeadLine` |


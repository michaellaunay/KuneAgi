# content.processes.ballot_processes.referendum

This module represent the Referendum election process definition
powered by the dace engine. This process is vlolatile, which means
that this process is automatically removed after the end. And is controlled,
which means that this process is not automatically instanciated.

## Process `referendumprocess`

```mermaid
flowchart TD
    n_start(("start"))
    n_vote["<b>Vote</b><br/><i>Vote</i>"]
    n_end((("end")))
    n_start --> n_vote
    n_vote --> n_end
```

| Node | Type | Title | Behaviors |
|---|---|---|---|
| `vote` | activity | Vote | `Vote` |


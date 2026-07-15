# content.processes.ballot_processes.majorityjudgment

This module represent the Majority Judgment election process definition
powered by the dace engine. This process is vlolatile, which means
that this process is automatically removed after the end. And is controlled,
which means that this process is not automatically instanciated.

## Processus `majorityjudgmentprocess`

```mermaid
flowchart TD
    n_start(("start"))
    n_vote["<b>Vote</b><br/><i>Vote</i>"]
    n_end((("end")))
    n_start --> n_vote
    n_vote --> n_end
```

| Nœud | Type | Titre | Behaviors |
|---|---|---|---|
| `vote` | activity | Vote | `Vote` |


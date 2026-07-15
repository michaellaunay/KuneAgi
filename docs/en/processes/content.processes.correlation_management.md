# content.processes.correlation_management

This module represent the Correlation management process definition
powered by the dace engine. This process is unique, which means that
this process is instantiated only once.

## Process `correlationmanagement`

```mermaid
flowchart TD
    n_start(("start"))
    n_pg{"+"}
    n_comment["<b>Comment</b><br/><i>CommentCorrelation</i>"]
    n_see["<b>Detail</b><br/><i>SeeCorrelation</i>"]
    n_eg{"X"}
    n_end((("end")))
    n_start --> n_pg
    n_pg --> n_comment
    n_comment --> n_eg
    n_pg --> n_see
    n_see --> n_eg
    n_eg --> n_end
```

| Node | Type | Title | Behaviors |
|---|---|---|---|
| `comment` | activity | Comment | `CommentCorrelation` |
| `see` | activity | Detail | `SeeCorrelation` |


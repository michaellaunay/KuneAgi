# content.processes.amendment_management

This module represent the Amendments management process definition
powered by the dace engine. This process is unique, which means that
this process is instantiated only once.

## Process `amendmentmanagement`

```mermaid
flowchart TD
    n_start(("start"))
    n_delamendment["<b>Delete</b><br/><i>DelAmendment</i>"]
    n_duplicate["<b>Duplicate</b><br/><i>DuplicateAmendment</i>"]
    n_edit["<b>Edit</b><br/><i>EditAmendment</i>"]
    n_explanation["<b>Explain my improvements</b><br/><i>ExplanationAmendment</i>"]
    n_explanationitem["<b>Justification of the item</b><br/><i>ExplanationItem</i>"]
    n_submit["<b>Prepare amendments</b><br/><i>SubmitAmendment</i>"]
    n_directsubmit["<b>Submit</b><br/><i>DirectSubmitAmendment</i>"]
    n_present["<b>Share</b><br/><i>PresentAmendment</i>"]
    n_comment["<b>Comment</b><br/><i>CommentAmendment</i>"]
    n_associate["<b>Associate</b><br/><i>Associate</i>"]
    n_see["<b>Details</b><br/><i>SeeAmendment</i>"]
    n_pg{"+"}
    n_eg{"X"}
    n_end((("end")))
    n_start --> n_pg
    n_pg --> n_edit
    n_pg --> n_submit
    n_pg --> n_directsubmit
    n_pg --> n_explanation
    n_pg --> n_explanationitem
    n_pg --> n_delamendment
    n_pg --> n_duplicate
    n_pg --> n_comment
    n_pg --> n_present
    n_pg --> n_associate
    n_pg --> n_see
    n_duplicate --> n_eg
    n_submit --> n_eg
    n_directsubmit --> n_eg
    n_delamendment --> n_eg
    n_edit --> n_eg
    n_comment --> n_eg
    n_present --> n_eg
    n_associate --> n_eg
    n_see --> n_eg
    n_eg --> n_end
```

| Node | Type | Title | Behaviors |
|---|---|---|---|
| `delamendment` | activity | Delete | `DelAmendment` |
| `duplicate` | activity | Duplicate | `DuplicateAmendment` |
| `edit` | activity | Edit | `EditAmendment` |
| `explanation` | activity | Explain my improvements | `ExplanationAmendment` |
| `explanationitem` | activity | Justification of the item | `ExplanationItem` |
| `submit` | activity | Prepare amendments | `SubmitAmendment` |
| `directsubmit` | activity | Submit | `DirectSubmitAmendment` |
| `present` | activity | Share | `PresentAmendment` |
| `comment` | activity | Comment | `CommentAmendment` |
| `associate` | activity | Associate | `Associate` |
| `see` | activity | Details | `SeeAmendment` |


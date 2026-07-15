# content.processes.question_management

This module represent the Question management process definition
powered by the dace engine. This process is unique, which means that
this process is instantiated only once.

## Processus `questionmanagement`

```mermaid
flowchart TD
    n_start(("start"))
    n_creat["<b>Ask a question</b><br/><i>AskQuestion</i>"]
    n_delquestion["<b>Delete</b><br/><i>DelQuestion</i>"]
    n_edit["<b>Edit</b><br/><i>EditQuestion</i>"]
    n_archive["<b>Archive</b><br/><i>ArchiveQuestion</i>"]
    n_present["<b>Share</b><br/><i>PresentQuestion, PresentQuestionAnonymous</i>"]
    n_comment["<b>Comment</b><br/><i>CommentQuestion, CommentQuestionAnonymous</i>"]
    n_answer["<b>Answer</b><br/><i>AnswerQuestion, AnswerQuestionAnonymous</i>"]
    n_associate["<b>Associate</b><br/><i>Associate</i>"]
    n_see["<b>Details</b><br/><i>SeeQuestion</i>"]
    n_support["<b>This question is useful</b><br/><i>SupportQuestion, SupportQuestionAnonymous</i>"]
    n_oppose["<b>This question is not useful</b><br/><i>OpposeQuestion, OpposeQuestionAnonymous</i>"]
    n_withdraw_token["<b>Withdraw my opinion</b><br/><i>WithdrawToken</i>"]
    n_close["<b>Close</b><br/><i>Close</i>"]
    n_pg{"+"}
    n_eg{"X"}
    n_end((("end")))
    n_start --> n_pg
    n_pg --> n_creat
    n_pg --> n_edit
    n_pg --> n_delquestion
    n_pg --> n_comment
    n_pg --> n_answer
    n_pg --> n_present
    n_pg --> n_associate
    n_pg --> n_see
    n_pg --> n_archive
    n_pg --> n_support
    n_pg --> n_close
    n_support --> n_eg
    n_pg --> n_oppose
    n_oppose --> n_eg
    n_pg --> n_withdraw_token
    n_withdraw_token --> n_eg
    n_creat --> n_eg
    n_delquestion --> n_eg
    n_edit --> n_eg
    n_comment --> n_eg
    n_answer --> n_eg
    n_present --> n_eg
    n_associate --> n_eg
    n_see --> n_eg
    n_archive --> n_eg
    n_close --> n_eg
    n_eg --> n_end
```

| Nœud | Type | Titre | Behaviors |
|---|---|---|---|
| `creat` | activity | Ask a question | `AskQuestion` |
| `delquestion` | activity | Delete | `DelQuestion` |
| `edit` | activity | Edit | `EditQuestion` |
| `archive` | activity | Archive | `ArchiveQuestion` |
| `present` | activity | Share | `PresentQuestion`, `PresentQuestionAnonymous` |
| `comment` | activity | Comment | `CommentQuestion`, `CommentQuestionAnonymous` |
| `answer` | activity | Answer | `AnswerQuestion`, `AnswerQuestionAnonymous` |
| `associate` | activity | Associate | `Associate` |
| `see` | activity | Details | `SeeQuestion` |
| `support` | activity | This question is useful | `SupportQuestion`, `SupportQuestionAnonymous` |
| `oppose` | activity | This question is not useful | `OpposeQuestion`, `OpposeQuestionAnonymous` |
| `withdraw_token` | activity | Withdraw my opinion | `WithdrawToken` |
| `close` | activity | Close | `Close` |

## Processus `answermanagement`

```mermaid
flowchart TD
    n_start(("start"))
    n_delanswer["<b>Delete</b><br/><i>DelAnswer</i>"]
    n_edit["<b>Edit</b><br/><i>EditAnswer</i>"]
    n_archive["<b>Archive</b><br/><i>ArchiveAnswer</i>"]
    n_present["<b>Share</b><br/><i>PresentAnswer, PresentAnswerAnonymous</i>"]
    n_comment["<b>Comment</b><br/><i>CommentAnswer, CommentAnswerAnonymous</i>"]
    n_associate["<b>Associate</b><br/><i>AssociateAnswer</i>"]
    n_see["<b>Details</b><br/><i>SeeAnswer</i>"]
    n_support["<b>This answer is useful</b><br/><i>SupportAnswer, SupportAnswerAnonymous</i>"]
    n_oppose["<b>This answer is not useful</b><br/><i>OpposeAnswer, OpposeAnswerAnonymous</i>"]
    n_withdraw_token["<b>Withdraw my opinion</b><br/><i>WithdrawTokenAnswer</i>"]
    n_validate["<b>Validate</b><br/><i>ValidateAnswer</i>"]
    n_transformtoidea["<b>Transform into an idea</b><br/><i>TransformToIdea</i>"]
    n_pg{"+"}
    n_eg{"X"}
    n_end((("end")))
    n_start --> n_pg
    n_pg --> n_edit
    n_pg --> n_delanswer
    n_pg --> n_comment
    n_pg --> n_present
    n_pg --> n_associate
    n_pg --> n_see
    n_pg --> n_archive
    n_pg --> n_support
    n_pg --> n_validate
    n_pg --> n_transformtoidea
    n_support --> n_eg
    n_pg --> n_oppose
    n_oppose --> n_eg
    n_pg --> n_withdraw_token
    n_withdraw_token --> n_eg
    n_delanswer --> n_eg
    n_edit --> n_eg
    n_comment --> n_eg
    n_present --> n_eg
    n_associate --> n_eg
    n_see --> n_eg
    n_archive --> n_eg
    n_validate --> n_eg
    n_transformtoidea --> n_eg
    n_eg --> n_end
```

| Nœud | Type | Titre | Behaviors |
|---|---|---|---|
| `delanswer` | activity | Delete | `DelAnswer` |
| `edit` | activity | Edit | `EditAnswer` |
| `archive` | activity | Archive | `ArchiveAnswer` |
| `present` | activity | Share | `PresentAnswer`, `PresentAnswerAnonymous` |
| `comment` | activity | Comment | `CommentAnswer`, `CommentAnswerAnonymous` |
| `associate` | activity | Associate | `AssociateAnswer` |
| `see` | activity | Details | `SeeAnswer` |
| `support` | activity | This answer is useful | `SupportAnswer`, `SupportAnswerAnonymous` |
| `oppose` | activity | This answer is not useful | `OpposeAnswer`, `OpposeAnswerAnonymous` |
| `withdraw_token` | activity | Withdraw my opinion | `WithdrawTokenAnswer` |
| `validate` | activity | Validate | `ValidateAnswer` |
| `transformtoidea` | activity | Transform into an idea | `TransformToIdea` |


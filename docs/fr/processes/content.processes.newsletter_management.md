# content.processes.newsletter_management

## Processus `newslettermanagement`

```mermaid
flowchart TD
    n_start(("start"))
    n_pg{"+"}
    n_creat["<b>Create a newsletter</b><br/><i>CreateNewsletter</i>"]
    n_edit["<b>Edit</b><br/><i>EditNewsletter</i>"]
    n_configure["<b>Configure</b><br/><i>ConfigureNewsletter</i>"]
    n_redact["<b>Write</b><br/><i>RedactNewsletter</i>"]
    n_send["<b>Send</b><br/><i>SendNewsletter</i>"]
    n_remove["<b>Remove</b><br/><i>RemoveNewsletter</i>"]
    n_subscribe["<b>Newsletters</b><br/><i>SubscribeNewsletter</i>"]
    n_unsubscribe["<b>Unsubscribe</b><br/><i>UserUnsubscribeNewsletter</i>"]
    n_unsubscribes["<b>Unsubscribe</b><br/><i>UnsubscribeNewsletter</i>"]
    n_see["<b>See</b><br/><i>SeeNewsletter</i>"]
    n_seesubscribed["<b>Subscribed users</b><br/><i>SeeSubscribed</i>"]
    n_see_all["<b>Newsletters</b><br/><i>SeeNewsletters</i>"]
    n_see_content_history["<b>Content history</b><br/><i>SeeNewsletterHistory</i>"]
    n_eg{"X"}
    n_end((("end")))
    n_start --> n_pg
    n_pg --> n_creat
    n_creat --> n_eg
    n_pg --> n_edit
    n_edit --> n_eg
    n_pg --> n_configure
    n_configure --> n_eg
    n_pg --> n_redact
    n_redact --> n_eg
    n_pg --> n_send
    n_send --> n_eg
    n_pg --> n_remove
    n_remove --> n_eg
    n_pg --> n_subscribe
    n_subscribe --> n_eg
    n_pg --> n_unsubscribe
    n_unsubscribe --> n_eg
    n_pg --> n_unsubscribes
    n_unsubscribes --> n_eg
    n_pg --> n_see
    n_see --> n_eg
    n_pg --> n_see_all
    n_see_all --> n_eg
    n_pg --> n_seesubscribed
    n_seesubscribed --> n_eg
    n_pg --> n_see_content_history
    n_see_content_history --> n_eg
    n_eg --> n_end
```

| Nœud | Type | Titre | Behaviors |
|---|---|---|---|
| `creat` | activity | Create a newsletter | `CreateNewsletter` |
| `edit` | activity | Edit | `EditNewsletter` |
| `configure` | activity | Configure | `ConfigureNewsletter` |
| `redact` | activity | Write | `RedactNewsletter` |
| `send` | activity | Send | `SendNewsletter` |
| `remove` | activity | Remove | `RemoveNewsletter` |
| `subscribe` | activity | Newsletters | `SubscribeNewsletter` |
| `unsubscribe` | activity | Unsubscribe | `UserUnsubscribeNewsletter` |
| `unsubscribes` | activity | Unsubscribe | `UnsubscribeNewsletter` |
| `see` | activity | See | `SeeNewsletter` |
| `seesubscribed` | activity | Subscribed users | `SeeSubscribed` |
| `see_all` | activity | Newsletters | `SeeNewsletters` |
| `see_content_history` | activity | Content history | `SeeNewsletterHistory` |


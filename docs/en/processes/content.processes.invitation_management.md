# content.processes.invitation_management

## Process `invitationmanagement`

```mermaid
flowchart TD
    n_start(("start"))
    n_pg{"+"}
    n_add["<b>Upload invitations</b><br/><i>UploadUsers</i>"]
    n_invite["<b>Invite users</b><br/><i>InviteUsers</i>"]
    n_seeinvitation["<b>Details</b><br/><i>SeeInvitation</i>"]
    n_seeinvitations["<b>The invitations</b><br/><i>SeeInvitations</i>"]
    n_edits["<b>Edit the invitations</b><br/><i>EditInvitations</i>"]
    n_edit["<b>Edit the invitation</b><br/><i>EditInvitation</i>"]
    n_accept["<b>Accept the invitation</b><br/><i>AcceptInvitation</i>"]
    n_refuse["<b>Refuse the invitation</b><br/><i>RefuseInvitation</i>"]
    n_remove["<b>Remove the invitation</b><br/><i>RemoveInvitation</i>"]
    n_reinvite["<b>Re-invite the person</b><br/><i>ReinviteUser</i>"]
    n_remind["<b>Remind the person</b><br/><i>RemindInvitation</i>"]
    n_eg{"X"}
    n_end((("end")))
    n_start --> n_pg
    n_pg --> n_add
    n_pg --> n_invite
    n_pg --> n_edits
    n_pg --> n_edit
    n_pg --> n_seeinvitation
    n_pg --> n_seeinvitations
    n_pg --> n_accept
    n_pg --> n_refuse
    n_pg --> n_remove
    n_pg --> n_reinvite
    n_pg --> n_remind
    n_accept --> n_eg
    n_refuse --> n_eg
    n_remove --> n_eg
    n_reinvite --> n_eg
    n_remind --> n_eg
    n_add --> n_eg
    n_seeinvitation --> n_eg
    n_seeinvitations --> n_eg
    n_invite --> n_eg
    n_edits --> n_eg
    n_edit --> n_eg
    n_eg --> n_end
```

| Node | Type | Title | Behaviors |
|---|---|---|---|
| `add` | activity | Upload invitations | `UploadUsers` |
| `invite` | activity | Invite users | `InviteUsers` |
| `seeinvitation` | activity | Details | `SeeInvitation` |
| `seeinvitations` | activity | The invitations | `SeeInvitations` |
| `edits` | activity | Edit the invitations | `EditInvitations` |
| `edit` | activity | Edit the invitation | `EditInvitation` |
| `accept` | activity | Accept the invitation | `AcceptInvitation` |
| `refuse` | activity | Refuse the invitation | `RefuseInvitation` |
| `remove` | activity | Remove the invitation | `RemoveInvitation` |
| `reinvite` | activity | Re-invite the person | `ReinviteUser` |
| `remind` | activity | Remind the person | `RemindInvitation` |


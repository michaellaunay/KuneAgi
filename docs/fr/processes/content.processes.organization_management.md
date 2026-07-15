# content.processes.organization_management

## Processus `organizationmanagement`

```mermaid
flowchart TD
    n_start(("start"))
    n_pg{"+"}
    n_add["<b>Upload organizations</b><br/><i>AddOrganizations</i>"]
    n_creat["<b>Create organizations</b><br/><i>CreatOrganizations</i>"]
    n_edits["<b>Edit organizations</b><br/><i>EditOrganizations</i>"]
    n_sees["<b>The Organizations</b><br/><i>SeeOrganizations</i>"]
    n_edit["<b>Edit</b><br/><i>EditOrganization</i>"]
    n_see["<b>Details</b><br/><i>SeeOrganization</i>"]
    n_remove["<b>Remove</b><br/><i>RemoveOrganization</i>"]
    n_add_members["<b>Add Members</b><br/><i>AddMembers</i>"]
    n_remove_members["<b>Remove Members</b><br/><i>RemoveMembers</i>"]
    n_user_edit_organization["<b>Edit the organization</b><br/><i>UserEditOrganization</i>"]
    n_withdraw_user["<b>Withdraw from the organization</b><br/><i>WithdrawUser</i>"]
    n_eg{"X"}
    n_end((("end")))
    n_start --> n_pg
    n_pg --> n_add
    n_pg --> n_creat
    n_pg --> n_add_members
    n_pg --> n_remove_members
    n_pg --> n_user_edit_organization
    n_pg --> n_withdraw_user
    n_pg --> n_remove
    n_pg --> n_see
    n_pg --> n_edit
    n_add --> n_eg
    n_pg --> n_edits
    n_edits --> n_eg
    n_pg --> n_sees
    n_sees --> n_eg
    n_creat --> n_eg
    n_add_members --> n_eg
    n_remove_members --> n_eg
    n_user_edit_organization --> n_eg
    n_withdraw_user --> n_eg
    n_remove --> n_eg
    n_edit --> n_eg
    n_see --> n_eg
    n_eg --> n_end
```

| Nœud | Type | Titre | Behaviors |
|---|---|---|---|
| `add` | activity | Upload organizations | `AddOrganizations` |
| `creat` | activity | Create organizations | `CreatOrganizations` |
| `edits` | activity | Edit organizations | `EditOrganizations` |
| `sees` | activity | The Organizations | `SeeOrganizations` |
| `edit` | activity | Edit | `EditOrganization` |
| `see` | activity | Details | `SeeOrganization` |
| `remove` | activity | Remove | `RemoveOrganization` |
| `add_members` | activity | Add Members | `AddMembers` |
| `remove_members` | activity | Remove Members | `RemoveMembers` |
| `user_edit_organization` | activity | Edit the organization | `UserEditOrganization` |
| `withdraw_user` | activity | Withdraw from the organization | `WithdrawUser` |


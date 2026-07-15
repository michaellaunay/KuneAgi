# content.processes.smart_folder_management

## Processus `smartfoldermanagement`

```mermaid
flowchart TD
    n_start(("start"))
    n_pg{"+"}
    n_add_smart_folder["<b>Create a topic of interest</b><br/><i>AddSmartFolder</i>"]
    n_addsub_smart_folder["<b>Create a sub topic of interest</b><br/><i>AddSubSmartFolder</i>"]
    n_edit_smart_folder["<b>Edit</b><br/><i>EditSmartFolder</i>"]
    n_remove_smart_folder["<b>Remove</b><br/><i>RemoveSmartFolder</i>"]
    n_see_smart_folder["<b>See a topic of interest</b><br/><i>SeeSmartFolder</i>"]
    n_publish_smart_folder["<b>Publish</b><br/><i>PublishSmartFolder</i>"]
    n_withdraw_smart_folder["<b>Withdraw</b><br/><i>WithdrawSmartFolder</i>"]
    n_see_smart_folders["<b>Registered topics of interest</b><br/><i>SeeSmartFolders</i>"]
    n_order_smart_folders["<b>Sort</b><br/><i>OrderSmartFolders</i>"]
    n_order_sub_smart_folders["<b>Sort</b><br/><i>OrderSubSmartFolders</i>"]
    n_eg{"X"}
    n_end((("end")))
    n_start --> n_pg
    n_pg --> n_add_smart_folder
    n_add_smart_folder --> n_eg
    n_pg --> n_publish_smart_folder
    n_publish_smart_folder --> n_eg
    n_pg --> n_withdraw_smart_folder
    n_withdraw_smart_folder --> n_eg
    n_pg --> n_addsub_smart_folder
    n_addsub_smart_folder --> n_eg
    n_pg --> n_edit_smart_folder
    n_edit_smart_folder --> n_eg
    n_pg --> n_remove_smart_folder
    n_remove_smart_folder --> n_eg
    n_pg --> n_see_smart_folder
    n_see_smart_folder --> n_eg
    n_pg --> n_see_smart_folders
    n_see_smart_folders --> n_eg
    n_pg --> n_order_smart_folders
    n_order_smart_folders --> n_eg
    n_pg --> n_order_sub_smart_folders
    n_order_sub_smart_folders --> n_eg
    n_eg --> n_end
```

| Nœud | Type | Titre | Behaviors |
|---|---|---|---|
| `add_smart_folder` | activity | Create a topic of interest | `AddSmartFolder` |
| `addsub_smart_folder` | activity | Create a sub topic of interest | `AddSubSmartFolder` |
| `edit_smart_folder` | activity | Edit | `EditSmartFolder` |
| `remove_smart_folder` | activity | Remove | `RemoveSmartFolder` |
| `see_smart_folder` | activity | See a topic of interest | `SeeSmartFolder` |
| `publish_smart_folder` | activity | Publish | `PublishSmartFolder` |
| `withdraw_smart_folder` | activity | Withdraw | `WithdrawSmartFolder` |
| `see_smart_folders` | activity | Registered topics of interest | `SeeSmartFolders` |
| `order_smart_folders` | activity | Sort | `OrderSmartFolders` |
| `order_sub_smart_folders` | activity | Sort | `OrderSubSmartFolders` |


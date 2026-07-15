# content.processes.user_management

## Process `usermanagement`

```mermaid
flowchart TD
    n_start(("start"))
    n_pg{"+"}
    n_login["<b>Log in</b><br/><i>LogIn</i>"]
    n_logout["<b>Log out</b><br/><i>LogOut</i>"]
    n_edit["<b>Edit</b><br/><i>Edit</i>"]
    n_quit["<b>Quit the platform</b><br/><i>Quit</i>"]
    n_confirm_quit["<b>Confirm the resignation request</b><br/><i>ConfirmQuitRequest</i>"]
    n_deactivate["<b>Disactivate the profile</b><br/><i>Deactivate</i>"]
    n_activate["<b>Activate the profile</b><br/><i>Activate</i>"]
    n_assign_roles["<b>Assign roles</b><br/><i>AssignRoles</i>"]
    n_see["<b>Details</b><br/><i>SeePerson</i>"]
    n_see_notations["<b>The marks</b><br/><i>SeeNotations</i>"]
    n_discuss["<b>Discuss</b><br/><i>Discuss</i>"]
    n_get_api_token["<b>Get API token</b><br/><i>GetAPIToken</i>"]
    n_general_discuss["<b>Discuss</b><br/><i>GeneralDiscuss</i>"]
    n_extract_alerts["<b>Extract alerts</b><br/><i>ExtractAlerts</i>"]
    n_eg{"X"}
    n_end((("end")))
    n_start --> n_pg
    n_pg --> n_login
    n_pg --> n_logout
    n_login --> n_eg
    n_pg --> n_extract_alerts
    n_extract_alerts --> n_eg
    n_logout --> n_eg
    n_pg --> n_discuss
    n_discuss --> n_eg
    n_pg --> n_general_discuss
    n_general_discuss --> n_eg
    n_pg --> n_edit
    n_edit --> n_eg
    n_pg --> n_get_api_token
    n_get_api_token --> n_eg
    n_pg --> n_deactivate
    n_deactivate --> n_eg
    n_pg --> n_quit
    n_quit --> n_eg
    n_pg --> n_confirm_quit
    n_confirm_quit --> n_eg
    n_pg --> n_activate
    n_activate --> n_eg
    n_pg --> n_assign_roles
    n_assign_roles --> n_eg
    n_pg --> n_see_notations
    n_see_notations --> n_eg
    n_pg --> n_see
    n_see --> n_eg
    n_eg --> n_end
```

| Node | Type | Title | Behaviors |
|---|---|---|---|
| `login` | activity | Log in | `LogIn` |
| `logout` | activity | Log out | `LogOut` |
| `edit` | activity | Edit | `Edit` |
| `quit` | activity | Quit the platform | `Quit` |
| `confirm_quit` | activity | Confirm the resignation request | `ConfirmQuitRequest` |
| `deactivate` | activity | Disactivate the profile | `Deactivate` |
| `activate` | activity | Activate the profile | `Activate` |
| `assign_roles` | activity | Assign roles | `AssignRoles` |
| `see` | activity | Details | `SeePerson` |
| `see_notations` | activity | The marks | `SeeNotations` |
| `discuss` | activity | Discuss | `Discuss` |
| `get_api_token` | activity | Get API token | `GetAPIToken` |
| `general_discuss` | activity | Discuss | `GeneralDiscuss` |
| `extract_alerts` | activity | Extract alerts | `ExtractAlerts` |

## Process `registrationmanagement`

```mermaid
flowchart TD
    n_start(("start"))
    n_pg{"+"}
    n_registration["<b>User registration</b><br/><i>Registration</i>"]
    n_confirmregistration["<b>Confirm registration</b><br/><i>ConfirmRegistration</i>"]
    n_remind["<b>Remind</b><br/><i>Remind</i>"]
    n_see_registration["<b>Details</b><br/><i>SeeRegistration</i>"]
    n_see_registrations["<b>Registrations</b><br/><i>SeeRegistrations</i>"]
    n_remove["<b>Remove</b><br/><i>RemoveRegistration</i>"]
    n_eg{"X"}
    n_end((("end")))
    n_start --> n_pg
    n_pg --> n_registration
    n_registration --> n_eg
    n_pg --> n_confirmregistration
    n_confirmregistration --> n_eg
    n_pg --> n_remind
    n_remind --> n_eg
    n_pg --> n_see_registration
    n_see_registration --> n_eg
    n_pg --> n_see_registrations
    n_see_registrations --> n_eg
    n_pg --> n_remove
    n_remove --> n_eg
    n_eg --> n_end
```

| Node | Type | Title | Behaviors |
|---|---|---|---|
| `registration` | activity | User registration | `Registration` |
| `confirmregistration` | activity | Confirm registration | `ConfirmRegistration` |
| `remind` | activity | Remind | `Remind` |
| `see_registration` | activity | Details | `SeeRegistration` |
| `see_registrations` | activity | Registrations | `SeeRegistrations` |
| `remove` | activity | Remove | `RemoveRegistration` |

## Process `registrationalert`

```mermaid
flowchart TD
    n_start(("start"))
    n_timer(("&#9200; time_date"))
    n_alert["<b>User registration</b><br/><i>AlertRegistration</i>"]
    n_end((("end")))
    n_start --> n_timer
    n_timer --> n_alert
    n_alert --> n_end
```

| Node | Type | Title | Behaviors |
|---|---|---|---|
| `alert` | activity | User registration | `AlertRegistration` |


# content.processes.reports_management

## Processus `reportsmanagement`

```mermaid
flowchart TD
    n_start(("start"))
    n_pg{"+"}
    n_report["<b>Report</b><br/><i>Report</i>"]
    n_report_max["<b>Report</b><br/><i>ReportMax</i>"]
    n_see_reports["<b>Reported contents</b><br/><i>SeeReports</i>"]
    n_restor["<b>Restore the content</b><br/><i>Restor</i>"]
    n_eg{"X"}
    n_end((("end")))
    n_start --> n_pg
    n_pg --> n_report
    n_report --> n_eg
    n_pg --> n_report_max
    n_report_max --> n_eg
    n_pg --> n_see_reports
    n_see_reports --> n_eg
    n_pg --> n_restor
    n_restor --> n_eg
    n_eg --> n_end
```

| Nœud | Type | Titre | Behaviors |
|---|---|---|---|
| `report` | activity | Report | `Report` |
| `report_max` | activity | Report | `ReportMax` |
| `see_reports` | activity | Reported contents | `SeeReports` |
| `restor` | activity | Restore the content | `Restor` |


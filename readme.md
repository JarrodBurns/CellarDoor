# CellarDoor File Backup
Schedule and execute daily file backups operations to copy and save your data to a secondary source automatically.

![Demo Image](/resources/demo.png?raw=true "Example Operation")

## First Time Setup
Navigate to **CellarDoor > Data > settings.json** and populate all values

| Field       | Description                                         |
|-------------|-----------------------------------------------------|
| DESTINATION | Where to save your backups too                      |
| GO_TIME     | When you want the script to run                     |
| MAX_BACKUPS | How many backups to create before deleting old ones |
| SOURCE      | The directories you want to backup                  |

## Automatic Backups
In order to run automatically, CellarDoor will register a task with Windows Task Scheduler named "CellarDoor File Backup". This will happen at the time you specify in *settings.json > GO_TIME*

## Dependencies
- Python 3.7
- Win 7

# CellarDoor File Backup
The intent of this script is to provide a quick and basic way to handle file backup operations.

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
In order for CellarDoor to execute daily, a task must be created in Windows Task Scheduler. If you haven't done this sort of thing before checkout [this guide](https://www.technipages.com/scheduled-task-windows) to get started.

Note:

On some systems windows may have trouble resolving your python interpreter and script location. It is recommended you fill the the optional parameter: **Actions > Edit > Start In** to ensure it fires correctly.

![Example](/resources/start_in.png?raw=true "Windows Task Scheduler Setup")

## Dependencies
- Python 3.7
- Win 7


# Copyright (c) 2022, Jarrod Burns
# All rights reserved.

# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.


from pathlib import Path

from . import filemanager


APP_NAME        = "CellarDoor File Backup"
XML_NAMESPACE   = "http://schemas.microsoft.com/windows/2004/02/mit/task"

FMT_DATE        = "%Y-%m-%d"
FMT_TIME        = "%H-%M-%S"
FMT_DATETIME    = "%Y-%m-%d--%H-%M-%S"

DATA_DIR        = Path().cwd().parent.joinpath("data")
SETTINGS_PATH   = DATA_DIR.joinpath("settings.json")
STATS_PATH      = DATA_DIR.joinpath("stats.json")
XML_PATH        = DATA_DIR.joinpath("task_recipe.xml")

SETTINGS        = filemanager.get_settings(SETTINGS_PATH)
SOURCE          = SETTINGS["APP"]["SOURCE"]
DST             = Path(SETTINGS["APP"]["DESTINATION"])

MAX_BACKUPS     = SETTINGS["APP"]["MAX_BACKUPS"]
GO_TIME         = SETTINGS["APP"]["GO_TIME"]

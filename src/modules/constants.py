
# Copyright (c) 2022, Jarrod Burns
# All rights reserved.

# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.


from pathlib import Path

from . import filemanager


APP_NAME = "CellarDoor File Backup"

FMT_DATE = "%Y-%m-%d"
FMT_TIME = "%H-%M-%S"
FMT_DATETIME = "%Y-%m-%d--%H-%M-%S"

DATA_DIR = Path().cwd().parent.joinpath("data")
SETTINGS_PATH = DATA_DIR.joinpath("settings.json")
STATS_PATH = DATA_DIR.joinpath("stats.json")

SETTINGS = filemanager.get_settings(SETTINGS_PATH)
SOURCE = SETTINGS["APP"]["SOURCE"]
DST = Path(SETTINGS["APP"]["DESTINATION"])

MAX_BACKUPS = SETTINGS["APP"]["MAX_BACKUPS"]

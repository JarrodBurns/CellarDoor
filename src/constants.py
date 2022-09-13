
from pathlib import Path

import filemanager


FMT_DATE        = "%Y-%m-%d"
FMT_TIME        = "%H-%M-%S"
FMT_DATETIME    = "%Y-%m-%d--%H-%M-%S"

CWD             = Path().cwd()
SETTINGS_PATH   = CWD.parent.joinpath("data", "settings.json")
STATS_PATH      = CWD.parent.joinpath("data", "stats.json")

SETTINGS        = filemanager.get_json(SETTINGS_PATH)
SRC             = Path(SETTINGS["APP"]["SOURCE"])
DST             = Path(SETTINGS["APP"]["DESTINATION"])
ARCHIVE_DST     = filemanager.get_archive_dst(SRC, DST)

MAX_BACKUPS     = SETTINGS["APP"]["MAX_BACKUPS"]

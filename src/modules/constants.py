
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
SRC = SETTINGS["APP"]["SOURCE"]
DST = Path(SETTINGS["APP"]["DESTINATION"])

MAX_BACKUPS = SETTINGS["APP"]["MAX_BACKUPS"]

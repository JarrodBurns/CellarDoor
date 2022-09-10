
import os
import time
from datetime import datetime
from pathlib import Path

import filemanager
import ui


def main() -> None:

    CWD = Path().cwd()

    SETTINGS_PATH = CWD.joinpath("settings.json")
    STATS_PATH = CWD.joinpath("stats.json")

    SETTINGS = filemanager.get_app_settings(SETTINGS_PATH)
    SRC = Path(SETTINGS["APP"]["SOURCE"])
    DST = Path(SETTINGS["APP"]["DESTINATION"])
    ARCHIVE_DST = filemanager.get_archive_dst(SRC, DST)

    MAX_BACKUPS = SETTINGS["APP"]["MAX_BACKUPS"]

    all_time = filemanager.get_stats(STATS_PATH)

    os.system("mode con cols=64 lines=27")

    ui.print_header(SETTINGS_PATH)

    if not filemanager.backup_made_today(DST):

        ui.print_with_timestamp("Beginning file backup.")

        stopwatch = datetime.now()

        filemanager.zip_with_animation(SRC, ARCHIVE_DST)

        stopwatch = (datetime.now() - stopwatch).seconds

        file_size = filemanager.bytes_to_scale(
            Path(f"{ARCHIVE_DST}.zip").stat().st_size
        )
        all_time["stats"]["work_time"] += stopwatch
        all_time["stats"]["executions"] += 1
        all_time["stats"]["data_transacted"][0] += file_size.size

    else:

        print("[E] Backup already exists for today!\n")

    filemanager.delete_excess_backup_files(DST, MAX_BACKUPS)
    filemanager.set_stats(STATS_PATH, all_time)

    ui.print_stats_all_time(STATS_PATH)
    ui.print_footer()
    time.sleep(5)


if __name__ == "__main__":
    main()

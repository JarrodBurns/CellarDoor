
import time
import os
from datetime import datetime

import filemanager
import ui


def main() -> None:

    SETTINGS_PATH = f"{os.path.abspath(os.getcwd())}\\settings.json"
    SETTINGS = filemanager.get_app_settings(SETTINGS_PATH)
    SRC = SETTINGS["APP"]["SOURCE"]
    DST = SETTINGS["APP"]["DESTINATION"]
    MAX_BACKUPS = SETTINGS["APP"]["MAX_BACKUPS"]
    ARCHIVE_DST = filemanager.get_archive_name(SRC, DST)
    STATS_PATH = f"{os.path.abspath(os.getcwd())}\\stats.json"

    all_time = filemanager.get_stats(STATS_PATH)

    ui.print_header()

    if not filemanager.backup_made_today(DST):

        ui.print_with_timestamp("Beginning file backup.")

        stopwatch = datetime.now()

        filemanager.zip_with_animation(SRC, ARCHIVE_DST)

        stopwatch = (datetime.now() - stopwatch).seconds

        file_size = filemanager.bytes_to_scale(
            os.path.getsize(ARCHIVE_DST + ".zip")
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

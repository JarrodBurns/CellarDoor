
import utils
import filemanager
import ui
# import schedule
# import os
import time
from datetime import datetime


def main() -> None:

    SETTINGS = utils.get_settings()
    SRC = SETTINGS["APP"]["SOURCE"]
    DST = SETTINGS["APP"]["DESTINATION"]
    MAX_BACKUPS = SETTINGS["APP"]["MAX_BACKUPS"]

    NAME = SRC.split('\\')[-1]
    BACKUP_DEST = f"{DST}\\{utils.timestamp()}_{NAME}"

    ui.print_header()

    if not filemanager.backup_made_today(DST):

        # current_time = datetime.now().strftime("%H:%M:%S")
        # print(f"[{current_time}]  Beginning file backup.\n")
        ui.print_with_timestamp("Beginning file backup.")

        filemanager.zip_and_report(SRC, BACKUP_DEST)

    else:
        print("[E] Backup already exists for today!\n")

    filemanager.delete_excess_backup_files(DST, MAX_BACKUPS)

    ui.print_footer()

    time.sleep(500)


if __name__ == "__main__":
    main()

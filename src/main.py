
import time

import filemanager
import ui


def main() -> None:

    SETTINGS = filemanager.get_app_settings()
    SRC = SETTINGS["APP"]["SOURCE"]
    DST = SETTINGS["APP"]["DESTINATION"]
    MAX_BACKUPS = SETTINGS["APP"]["MAX_BACKUPS"]
    ARCHIVE_DST = filemanager.get_archive_name(SRC, DST)

    ui.print_header()

    if not filemanager.backup_made_today(DST):

        ui.print_with_timestamp("Beginning file backup.")

        filemanager.zip_with_animation(SRC, ARCHIVE_DST)

    else:

        print("[E] Backup already exists for today!\n")

    filemanager.delete_excess_backup_files(DST, MAX_BACKUPS)

    ui.print_footer()

    time.sleep(5)


if __name__ == "__main__":
    main()

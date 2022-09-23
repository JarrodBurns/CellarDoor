
import logging
import logging.config
from pathlib import Path
import time

import modules.constants as C
import modules.filemanager as filemanager
import modules.ui as ui
import modules.zipit as zipit


def main() -> None:

    log = logging.getLogger(__name__)
    log.info("CellarDoor Started")

    ui.draw_console()
    ui.print_header(C.APP_NAME, C.SETTINGS)

    for path in C.SOURCE:

        archive = zipit.ZipIt(Path(path), C.DST).zip_dir()

        filemanager.update_stats(C.STATS_PATH, archive.file_size.size, archive.stopwatch)
        filemanager.police_backup_files(archive.zipfile_dir, C.MAX_BACKUPS)

    ui.print_stats_all_time(filemanager.get_stats(C.STATS_PATH))
    ui.print_footer()

    log.info("CellarDoor Completed")


if __name__ == "__main__":

    main()
    time.sleep(10)

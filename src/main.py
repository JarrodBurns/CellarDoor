
from pathlib import Path
from threading import Thread

from datetime import datetime
import time

import modules.constants as C
import modules.filemanager as filemanager
import modules.ui as ui


def zip_with_animation(src: Path, dst: Path) -> None:

    ui.print_with_timestamp("Beginning file backup.")

    zip_files = Thread(target=lambda: filemanager.zip_dir(src, dst))
    zip_files.start()

    while zip_files.is_alive():

        ui.in_progress_animation()
        zip_files.join(0.2)

    ui.finalize_animation()


def main() -> None:

    ui.draw_console()
    ui.print_header(C.APP_NAME, C.SETTINGS)

    if not filemanager.backup_made_today(C.DST, C.FMT_DATE):

        archive_name = filemanager.get_archive_name(C.SRC, C.DST, C.FMT_DATETIME)
        stopwatch = datetime.now()

        zip_with_animation(C.SRC, archive_name)

        stopwatch = datetime.now() - stopwatch
        file_size = archive_name.stat().st_size
        file_size = filemanager.scale_bytes(file_size, size_format="gb")

        filemanager.update_stats(C.STATS_PATH, file_size, stopwatch)
        filemanager.police_backup_files(C.DST, C.MAX_BACKUPS)

    ui.print_stats_all_time(filemanager.get_stats(C.STATS_PATH))
    ui.print_footer()


if __name__ == "__main__":

    main()
    time.sleep(10)

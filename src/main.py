
from datetime import datetime
import time

import modules.constants as C
import modules.filemanager as filemanager
import modules.ui as ui


def main() -> None:

    ui.draw_console()
    ui.print_header(C.APP_NAME)

    if not filemanager.backup_made_today(C.DST):

        stopwatch = datetime.now()

        filemanager.zip_with_animation(C.SRC, C.ARCHIVE_DST)

        stopwatch = datetime.now() - stopwatch
        file_size = C.ARCHIVE_DST.stat().st_size
        file_size = filemanager.scale_bytes(file_size, size_format="gb")

        filemanager.update_stats(C.STATS_PATH, file_size, stopwatch)
        filemanager.police_backup_files(C.DST, C.MAX_BACKUPS)

    ui.print_stats_all_time(C.STATS_PATH)
    ui.print_footer()


if __name__ == "__main__":

    main()
    time.sleep(10)

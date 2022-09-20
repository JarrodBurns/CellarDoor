
from pathlib import Path
import time

import modules.constants as C
import modules.filemanager as filemanager
import modules.ui as ui
import modules.zipit as zipit


def main() -> None:

    ui.draw_console()
    ui.print_header(C.APP_NAME, C.SETTINGS)

    # if not filemanager.backup_made_today(C.DST, C.FMT_DATE):

    for path in C.SRC:

        j = zipit.ZipIt(Path(path), C.DST).zip_dir()

        filemanager.update_stats(C.STATS_PATH, j.file_size.size, j.stopwatch)
        filemanager.police_backup_files(j.zipfile_dir, C.MAX_BACKUPS)

    ui.print_stats_all_time(filemanager.get_stats(C.STATS_PATH))
    ui.print_footer()


if __name__ == "__main__":

    main()
    time.sleep(10)

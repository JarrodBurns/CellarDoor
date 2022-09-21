
from pathlib import Path
import time

import modules.constants as C
import modules.filemanager as filemanager
import modules.ui as ui
import modules.zipit as zipit


def main() -> None:

    ui.draw_console()
    ui.print_header(C.APP_NAME, C.SETTINGS)

    for path in C.SRC:

        archive = zipit.ZipIt(Path(path), C.DST).zip_dir()

        filemanager.update_stats(C.STATS_PATH, archive.file_size.size, archive.stopwatch)
        filemanager.police_backup_files(archive.zipfile_dir, C.MAX_BACKUPS)

    ui.print_stats_all_time(filemanager.get_stats(C.STATS_PATH))
    ui.print_footer()


if __name__ == "__main__":

    main()
    time.sleep(10)

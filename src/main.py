
# Copyright (c) 2022, Jarrod Burns
# All rights reserved.

# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.


from pathlib import Path
import logging
import time

import modules.constants as C
import modules.filemanager as filemanager
import modules.ui as ui
import modules.zipit as zipit


def main() -> None:

    log.info("CellarDoor Started")

    filemanager.validate_source_list(C.SOURCE)

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

    log = logging.getLogger(__name__)

    main()
    time.sleep(10)

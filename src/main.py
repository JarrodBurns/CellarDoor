
# Copyright (c) 2022, Jarrod Burns
# All rights reserved.

# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.


from pathlib import Path
from typing import Callable
import logging
import time

from modules import constants as C
from modules import filemanager
from modules import schedule
from modules import ui
from modules import zipit


def draw_ui(func: Callable) -> Callable:

    def function_wrapper():

        ui.draw_console()
        ui.print_header(C.APP_NAME, C.SETTINGS)

        func()

        ui.print_stats_all_time(filemanager.get_stats(C.STATS_PATH))
        ui.print_footer()

    return function_wrapper


@draw_ui
def manage_archive_operation() -> None:

    if not isinstance(C.SOURCE, list):

        log.error("Expected list object for SOURCE. Got %s", type(C.SOURCE))
        return

    for path in C.SOURCE:

        archive = zipit.ZipIt(Path(path), C.DST)
        archive.zip_dir()

        filemanager.update_stats(
            C.STATS_PATH, archive.file_size.size, archive.stopwatch
        )
        filemanager.police_backup_files(
            archive.zipfile_dir, C.MAX_BACKUPS
        )


def manage_scheduled_task() -> None:
    """
    Update or create a Windows Scheduler Task for CellarDoor.

    GO_TIME = null | 0 | ''

        If a task has been previously scheduled, it will be removed.
        A task will not be scheduled
    """
    if not C.GO_TIME:

        schedule.delete_task(C.APP_NAME)
        return

    filemanager.write_xml(C.XML_PATH, C.XML_NAMESPACE, C.GO_TIME)
    schedule.delete_task(C.APP_NAME)
    schedule.new_task(C.APP_NAME, C.XML_PATH)


def main() -> None:

    log.info("CellarDoor Started")

    manage_scheduled_task()
    manage_archive_operation()

    log.info("CellarDoor Completed")


if __name__ == "__main__":

    log = logging.getLogger(__name__)

    main()
    time.sleep(10)


# Copyright (c) 2022, Jarrod Burns
# All rights reserved.

# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.


from pathlib import Path
import logging
import subprocess


log = logging.getLogger(__name__)


def _log_output(process: subprocess.CompletedProcess) -> None:

    encoding = "utf-8"

    if process.returncode == 0:

        success_mesage = process.stdout.decode(encoding)
        log.info(success_mesage.rstrip())

    if process.returncode == 1:

        error_message = process.stderr.decode(encoding)
        log.error(error_message.rstrip())


def new_task(task_name: str, xml_recipe: Path) -> None:
    """
    Register an automated task with Windows Task Scheduler

    task_name is a unique identifier you will use to manage the task.

    This function will automatically overwrite an existing task of
    the same name.
    """
    process = subprocess.run(
        [
            "schtasks.exe",
            "/Create",
            "/XML",
            xml_recipe,
            "/TN",
            task_name
        ],
        capture_output=True
    )

    _log_output(process)


def delete_task(task_name: str) -> None:
    """
    Remove a Windows Task Scheduler task.
    """
    process = subprocess.run(
        [
            "schtasks.exe",
            "/Delete",
            "/F",
            "/TN",
            task_name,
        ],
        capture_output=True
    )

    _log_output(process)


def run_task(task_name: str) -> None:
    """
    Run existing Windows Task Scheduler task.
    """
    process = subprocess.run(
        [
            "schtasks.exe",
            "/Run",
            "/TN",
            task_name
        ],
        capture_output=True
    )

    _log_output(process)


def main() -> None:

    # Convenience code to run a manual backup,
    # Will break if you haven't ran CellarDoor once before.
    # Output will not be logged.

    task = "CellarDoor File Backup"
    run_task(task)


if __name__ == "__main__":
    main()

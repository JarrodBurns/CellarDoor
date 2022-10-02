
# Copyright (c) 2022, Jarrod Burns
# All rights reserved.

# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.


from datetime import datetime, date
from pathlib import Path
from typing import Any
import getpass
import json
import logging
import xml.etree.ElementTree as ET


log = logging.getLogger(__name__)


def _get_json(src: Path) -> dict[str, Any]:

    try:

        with open(src, 'r') as file_handle:

            return json.load(file_handle)

    except FileNotFoundError as e:

        log.exception(e)


def _set_json(src: Path, json_to_write: dict[str, Any]) -> None:

    try:

        with open(src, 'w') as file_handle:

            json.dump(json_to_write, file_handle, indent=4)

    except FileNotFoundError as e:

        log.exception(e)


def _get_or_set_json(src: Path, fallback: dict[str, Any]) -> dict[str, Any]:

    if not src.exists():

        _set_json(src, fallback)

        log.warn("Source file not found, using fallback. Expected: %s", src)

    return _get_json(src)


def _validate_go_time(go_time: str) -> str:

    go_time = str(go_time) + ":00"

    if len(go_time) != 8:

        log.error("Invalid 24 hour time format. Expected: NN:NN  Got: %s", go_time)
        raise ValueError()

    if int(go_time[:2]) > 23:

        log.error("Invalid 24 hour time format. Hours must be < 24  Got: %s", go_time[:1])
        raise ValueError()

    return go_time


def get_settings(src: Path) -> dict[str, Any]:

    fallback = {
        "APP": {
            "DESTINATION": "C:\\backups",
            "GO_TIME": "20:00",
            "MAX_BACKUPS": 5,
            "SOURCE": ["C:\\Users"]
        }
    }

    return _get_or_set_json(src, fallback)


def get_stats(src: Path) -> dict[str, Any]:

    fallback = {
        "stats": {
            "data_transacted": [0.0, "gb"],
            "executions": 0,
            "work_time": 0
        }
    }

    return _get_or_set_json(src, fallback)


def police_backup_files(archive_dir: Path, max_backups: int) -> None:
    """
    Removes files from a given directory until it aligns with the
    quantity specified by max_backups.

    Files which do not begin with the expected datetime format
    will be overlooked.

    Expected Datetime Format: "2022-07-07--22-13-12_"

    Sort order: Oldest first
    """
    n = "[0-9]" * 2
    pattern = f"**/{n * 2}-{n}-{n}--{n}-{n}-{n}_*"
    archives = list(archive_dir.glob(pattern))

    while len(archives) > max_backups:

        oldest_archive = min(archives)
        oldest_archive.unlink()
        archives.remove(oldest_archive)

        log.info("Deleted file: %s", oldest_archive)


def update_stats(
    json_path: Path,
    file_size: float,
    stopwatch: datetime,
    executions: int = 1
) -> None:

    all_time = get_stats(json_path)

    all_time["stats"]["data_transacted"][0] += file_size
    all_time["stats"]["executions"] += executions
    all_time["stats"]["work_time"] += stopwatch.seconds

    _set_json(json_path, all_time)


def write_xml(xml_src: Path, xml_namespace: str, go_time: str) -> None:
    """
    Specific to the prepared XML file:  CellarDoor > data > task_recipe.xml

    Prepares XML schema for the Windows Task Scheduler.
    MS Documentation reference: https://tinyurl.com/yckmzuaz
    """
    start_in_dir = xml_src.parent.parent.joinpath("src")
    mainfile_path = start_in_dir.joinpath("main.py")

    ET.register_namespace('', xml_namespace)
    tree = ET.parse(xml_src)
    root = tree.getroot()

    _date = str(date.today()) + 'T'
    go_time = _validate_go_time(go_time)

    root[1][0][0].text = _date + go_time        # Task start boundary
    root[2][0][0].text = getpass.getuser()      # Current user name
    root[4][0][0].text = str(mainfile_path)     # Path to main.py
    root[4][0][1].text = str(start_in_dir)      # Parent dir for main.py

    tree.write(xml_src, encoding="UTF-16", xml_declaration=True)


def main() -> None:
    pass


if __name__ == "__main__":
    main()


from dataclasses import dataclass, astuple
from datetime import datetime
from pathlib import Path
from typing import Any
from zipfile import ZipFile, ZIP_DEFLATED
import json


@dataclass
class FileSize:
    size: float
    scale: str

    def __str__(self):
        return f"{self.size} {self.scale}"

    def __iter__(self):
        return iter(astuple(self))


def backup_made_today(archive_dir: Path, date_fmt: str = "%Y-%m-%d") -> bool:
    """
    Enumerates the given directory for a file name beginning
    with today's date. A bool is returned to reflect the results.
    """
    if list(archive_dir.glob(f"**/{datetime.now():{date_fmt}}*")):

        print("[E] Backup already exists for today!\n")

        return True


def police_backup_files(archive_dir: Path, max_backups: int) -> None:
    """
    Removes files from a given directory until it aligns with the
    quantity specified by max_backups.

    Sort order: Oldest first
    """
    n = "[0-9]" * 2
    pattern = f"**/{n * 2}-{n}-{n}--{n}-{n}-{n}_*"
    archives = list(archive_dir.glob(pattern))

    while len(archives) > max_backups:

        oldest_archive = min(archives)
        oldest_archive.unlink()
        archives.remove(oldest_archive)


def get_archive_name(
    src: Path,
    archive_dir: Path,
    datetime_fmt: str = "%Y-%m-%d--%H-%M-%S"
) -> Path:

    archive_dir.mkdir(parents=True, exist_ok=True)

    date_and_time = f"{datetime.now():{datetime_fmt}}"
    archive_name = f"{date_and_time}_{src.parts[-1]}.zip"

    return archive_dir.joinpath(archive_name)


def get_settings(src: Path) -> dict[str, Any]:

    fallback = {
        "APP": {
            "DESTINATION": "C:\\backups",
            "GO_TIME": "20:00",
            "MAX_BACKUPS": 5,
            "SOURCE": "C:\\Users"
        }
    }

    if not src.exists():

        set_json(src, fallback)

    return get_json(src)


def get_stats(src: Path) -> dict[str, Any]:

    fallback = {
        "stats": {
            "data_transacted": [0.0, "gb"],
            "executions": 0,
            "work_time": 0
        }
    }

    if not src.exists():

        set_json(src, fallback)

    return get_json(src)


def get_json(src: Path) -> dict[str, Any]:

    with open(src, 'r') as file_handle:

        return json.load(file_handle)


def set_json(src: Path, json_to_write: dict[str, Any]) -> None:

    with open(src, 'w') as file_handle:

        json.dump(json_to_write, file_handle, indent=4)


def scale_bytes(
    size_in_bytes: int,
    size_format: str = "gb",
    rounding_precision: int = 2
) -> FileSize:

    scales = {
        "kb": 1,
        "mb": 2,
        "gb": 3,
        "tb": 4,
    }

    if size_format not in scales.keys():

        raise ValueError(f"Invalid mode: '{size_format}'")

    converted_size = size_in_bytes / (1024 ** scales[size_format])
    converted_size = round(converted_size, rounding_precision)

    return FileSize(converted_size, size_format)


def update_stats(
    json_path: Path,
    file_size: FileSize,
    stopwatch: datetime,
    executions: int = 1
) -> None:

    all_time = get_settings(json_path)

    all_time["stats"]["data_transacted"][0] += file_size.size
    all_time["stats"]["executions"] += executions
    all_time["stats"]["work_time"] += stopwatch.seconds

    set_json(json_path, all_time)


def zip_dir(src: Path, dst: Path) -> None:

    with ZipFile(
            dst,
            'w',
            allowZip64=True,
            compression=ZIP_DEFLATED
    ) as archive:

        for file_path in src.rglob('*'):

            archive.write(file_path, arcname=file_path.relative_to(src))


def main() -> None:
    pass


if __name__ == "__main__":
    main()

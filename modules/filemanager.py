
from dataclasses import dataclass, astuple
from datetime import datetime
from pathlib import Path
from threading import Thread
from typing import Any
from zipfile import ZipFile, ZIP_DEFLATED
import json

from . import ui


@dataclass
class FileSize:
    size: float
    scale: str

    def __str__(self):
        return f"{self.size} {self.scale}"

    def __iter__(self):
        return iter(astuple(self))


def _sort_backup_files(archives: list[Path, ...]
                       ) -> list[tuple[int, datetime], ...]:
    """
    Orders and returns a given list by oldest date to youngest date
    """
    index_datetime = []  # int, datetime

    for index, path in enumerate(archives):

        try:

            date_and_time = datetime.strptime(
                "_".join(path.stem.split("_")[:2]), "%d-%b-%y_%H-%M-%S"
            )

            index_datetime.append((index, date_and_time))

        except ValueError:
            pass

        except BaseException as e:
            print(e)
            break

    index_datetime = sorted(
        index_datetime, key=lambda x: x[1], reverse=True
    )

    return index_datetime


def backup_made_today(src_dir: Path) -> bool:
    """
    Enumerates the source directory for a file name beginning
    with todays date. A bool is returned to reflect the results.
    """
    if list(src_dir.glob(f"**/{datetime.now():%d-%b-%y}*")):

        print("[E] Backup already exists for today!\n")

        return True


def police_backup_files(src_dir: Path, max_backups: int) -> None:
    """
    Removes files from a given directory until it aligns with the
    quantity specified by max_backups.

    Sort order: Oldest first
    """
    pattern = "**/[0-9]?-[A-z]??-[0-9]?*"
    archives = list(src_dir.glob(pattern))

    index_datetime = _sort_backup_files(archives)

    while len(index_datetime) > max_backups:

        archives[index_datetime.pop()[0]].unlink()


def get_archive_dst(src: Path, dst: Path) -> Path:

    date_and_time = f"{datetime.now():%d-%b-%y_%H-%M-%S}"
    archive_name = f"{date_and_time}_{src.parts[-1]}.zip"

    return dst.joinpath(archive_name)


def get_json(path: Path) -> dict[str, Any]:

    with open(path, "r") as file_handle:

        return json.load(file_handle)


def set_json(path: Path, json_to_write: dict[str, Any]) -> None:

    with open(path, "w") as file_handle:

        json.dump(json_to_write, file_handle)


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

    all_time = get_json(json_path)

    all_time["stats"]["data_transacted"][0] += file_size.size
    all_time["stats"]["executions"] += executions
    all_time["stats"]["work_time"] += stopwatch.seconds

    set_json(json_path, all_time)


def zip_dir(src: Path, dst: Path) -> None:

    with ZipFile(
            dst, 'w', allowZip64=True, compression=ZIP_DEFLATED) as archive:

        for file_path in src.rglob('*'):

            archive.write(file_path, arcname=file_path.relative_to(src))


def zip_with_animation(src: Path, dst: Path) -> None:

    ui.print_with_timestamp("Beginning file backup.")

    zip_files = Thread(target=lambda: zip_dir(src, dst))
    zip_files.start()

    while zip_files.is_alive():

        ui.in_progress_animation()
        zip_files.join(0.2)

    ui.finalize_animation()


def main() -> None:
    pass


if __name__ == "__main__":
    main()

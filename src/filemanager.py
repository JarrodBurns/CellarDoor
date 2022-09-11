
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from threading import Thread
from typing import Any
from zipfile import ZipFile, ZIP_DEFLATED
import json

import ui


@dataclass
class FileSize:
    size: float
    scale: str

    def __str__(self):
        return f"{self.size} {self.scale}"


def backup_made_today(path: Path) -> bool:

    today = datetime.now().strftime("%b-%d-%y")

    for i in path.glob("**/*"):

        if i.parts[-1].split('_')[0] == today:
            return True

    return False


def delete_excess_backup_files(path: Path, max_backups: int) -> None:

    archives = [str(x) for x in list(path.glob("**/*"))]

    while len(archives) > max_backups:

        oldest_archive = archives.pop(archives.index(min(archives)))

        Path(oldest_archive).unlink()


def get_archive_dst(src: Path, dst: Path) -> Path:

    date_and_time = datetime.now().strftime("%b-%d-%y_%H-%M-%S")
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
    all_time["stats"]["work_time"] += stopwatch

    set_json(json_path, all_time)


def zip_dir(src: Path, dst: Path) -> None:

    with ZipFile(dst, 'w', compression=ZIP_DEFLATED) as archive:

        for file_path in src.rglob('*'):

            archive.write(file_path, arcname=file_path.relative_to(src))


def zip_with_animation(src: Path, dst: Path) -> None:

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

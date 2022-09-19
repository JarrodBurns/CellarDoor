
from datetime import datetime
from pathlib import Path
from typing import Optional
from zipfile import ZipFile, ZIP_DEFLATED


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


def _progress_report(
    current_progress: float,
    file_path: Path,
    minify_path: bool = True
) -> str:
    """
    Example Out: [=====-----][ 50.0%  ] -- "C:/Users/.../my_dir/my_file.txt"
    """
    fill_percent = int(current_progress // 10)
    progress_bar = f"[{'=' * fill_percent}{'-' * (10 - fill_percent)}]"

    truncate_progress = f"{current_progress:.1f}%"
    progress_percent = f"[{truncate_progress:^8}]"

    if minify_path:
        file_path = minify_path(file_path)

    return f"{progress_bar}{progress_percent} -- {file_path}"


def minify_path(path_to_shorten: Path) -> Path:
    """
    Shortens file paths for display purposes. Only the first and last two
    directories/files are shown, the rest are replaced with "..."

    Example Out: "C:/Users/.../my_dir/my_file.txt"
    """
    parts = path_to_shorten.parts

    if len(parts) < 4:

        return path_to_shorten

    return Path().joinpath(*parts[:2], "...", *parts[-2:])


class ZipIt:

    FMT_DATETIME = "%Y-%m-%d--%H-%M-%S"

    def __init__(self, dir_to_zip: Path, user_backup_path: Path):

        self.dir_to_zip: Path = dir_to_zip
        self.user_backup_path: Path = user_backup_path

        self.zipfile_dir: Path = self._create_zipfile_dir()
        self.zipfile_name: Path = self._create_zipfile_name()

        self.stopwatch: Optional[datetime] = None
        self.file_size: Optional[int] = None

    def _create_zipfile_dir(self) -> Path:
        """
        Example In: C:/my_dir               # Directory to backup
        Example Out: D:/backups/my_dir/     # Dir to save backup to
        """
        zipfile_dir = self.user_backup_path.joinpath(self.dir_to_zip.parts[-1])
        zipfile_dir.mkdir(parents=True, exist_ok=True)

        return zipfile_dir

    def _create_zipfile_name(self) -> Path:
        """
        Example Out: 'datetime_parentdirectory.zip'
        Example Out: '2022-07-07--22-13-12_sourcedir.zip'
        """
        date_and_time = f"{datetime.now():{self.FMT_DATETIME}}"
        zipfile_name = f"{date_and_time}_{self.zipfile_dir.parts[-1]}.zip"

        return self.zipfile_dir.joinpath(zipfile_name)

    def zip_dir(self) -> ZipFile:

        self.stopwatch = datetime.now()
        current_progress = 0

        with ZipFile(
            self.zipfile_name, 'w', allowZip64=True, compression=ZIP_DEFLATED
        ) as archive:

            # Loads all files into memory, could be slow for large archives
            files_to_zip = list(self.dir_to_zip.rglob('*'))

            progress_increment = 100 / len(files_to_zip)

            for file in files_to_zip:

                archive.write(file, arcname=file.relative_to(self.dir_to_zip))

                current_progress += progress_increment

                print(_progress_report(current_progress, file), end='\r', flush=True)

        self.stopwatch = datetime.now() - self.stopwatch
        self.file_size = self.zipfile_name.stat().st_size

        return self


if __name__ == "__main__":

    cwd = Path().cwd()

    paths = [
        cwd.joinpath("t1"),
        cwd.joinpath("t2"),
        cwd.joinpath("t3")
    ]

    backup_path = cwd.joinpath("backups")

    for i in paths:

        # j = ZipIt(i, backup_path).zip_dir()
        # print(j.stopwatch, j.file_size)
        # police_backup_files(j.zipfile_dir, 5)
        print()

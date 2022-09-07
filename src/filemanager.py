
import json
import os
import shutil
import threading
from datetime import datetime

import ui


def backup_made_today(path: str) -> bool:

    today = datetime.now().strftime("%b-%d-%y")

    for i in os.listdir(path):

        if i.split('_')[0] == today:
            return True

    return False


def delete_excess_backup_files(path: str, max_backups: int) -> None:

    while len(os.listdir(path)) > max_backups:

        os.remove(f"{path}\\{min(os.listdir(path))}")


def get_archive_name(src: str, dst: str) -> str:

    date_and_time = datetime.now().strftime("%b-%d-%y_%H-%M-%S")

    backup_directory = src.split('\\')[-1]
    archive_name = f"{date_and_time}_{backup_directory}"

    return f"{dst}\\{archive_name}"


def get_app_settings(path: str = "settings.json"):

    with open(path, "r") as file_handle:
        return json.load(file_handle)


def get_stats(path: str = "stats.json"):

    with open(path, "r") as file_handle:
        return json.load(file_handle)


def set_stats(json_to_write: dict, path: str = "stats.json"):

    with open(path, "w") as file_handle:
        json.dump(json_to_write, file_handle)


def zip_dir(src: str, dst: str) -> None:

    shutil.make_archive(dst, "zip", src)


def zip_with_animation(src: str, dst: str) -> None:

    def wrapper(func, *args):
        func(*args)

    zip_files = threading.Thread(target=wrapper, args=(zip_dir, src, dst))
    zip_files.start()

    while zip_files.is_alive():

        ui.in_progress_animation()
        zip_files.join(0.2)

    ui.finalize_animation()

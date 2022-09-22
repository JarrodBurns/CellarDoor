
from pathlib import Path
import logging
import logging.config


LOGS_DIR = Path().cwd().parent.joinpath("logs")
LOGS_CONFIG = LOGS_DIR.joinpath("config", "logging.config")


def update_log_save_location(logs_dir: Path) -> None:

    log_save_file = logs_dir.joinpath("cellardoor.log")
    log_config_file = logs_dir.joinpath("config", "logging.config")

    replacement = ""
    replace_statment = f"args=({repr(str(log_save_file))}, 'a')"

    with open(log_config_file, 'r') as file_handle:

        for line in file_handle:

            line = line.strip()

            if line.startswith("args") and ".log" in line:

                line = line.replace(line, replace_statment)

            replacement += line + '\n'

    with open(log_config_file, 'w') as file_handle:
        file_handle.write(replacement)


update_log_save_location(LOGS_DIR)
logging.config.fileConfig(LOGS_CONFIG)

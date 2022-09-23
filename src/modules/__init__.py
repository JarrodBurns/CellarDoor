
from pathlib import Path
import logging
import logging.config


LOG_DIR = Path().cwd().parent.joinpath("logs")
LOG_CONFIG = LOG_DIR.joinpath("config", "logging.config")
LOG_FILE_PATH = repr(str(LOG_DIR.joinpath("cellardoor.log")))
CONFIG_PATH_ARGS = f"args=({LOG_FILE_PATH}, 'a')"


def update_log_save_location(log_config: Path, config_path_args: str) -> None:
    """
    Checks the filehandler path in the log config and updates
    the value based on the current working dir of the project file.
    """
    out = ""

    with open(log_config, "r+") as file_handle:

        file_content = file_handle.read().rstrip()

        for line in file_content.split('\n'):

            if line.startswith("args") and ".log" in line:

                line = line.replace(line, config_path_args)

            out += line + '\n'

        file_handle.seek(0)
        file_handle.write(out)
        file_handle.truncate()


update_log_save_location(LOG_CONFIG, CONFIG_PATH_ARGS)
logging.config.fileConfig(LOG_CONFIG)

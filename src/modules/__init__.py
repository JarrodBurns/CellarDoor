
# Copyright (c) 2022, Jarrod Burns
# All rights reserved.

# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.


from contextlib import closing
from pathlib import Path
import fileinput
import logging
import logging.config
import sys


LOG_DIR = Path().cwd().parent.joinpath("logs")
LOG_CONFIG = LOG_DIR.joinpath("config", "logging.config")
LOG_FILE_PATH = repr(str(LOG_DIR.joinpath("cellardoor.log")))
CONFIG_PATH_ARGS = f"args=({LOG_FILE_PATH}, 'a')\n"


def update_log_save_location(log_config: Path, config_path_args: str) -> None:
    """
    Checks the filehandler path in the log config and updates
    the value based on the current working dir of the project file.
    """
    with closing(fileinput.input(log_config, inplace=1)) as file_handle:

        for line in file_handle:

            if line.startswith("args") and ".log" in line:

                line = line.replace(line, config_path_args)

            sys.stdout.write(line)


update_log_save_location(LOG_CONFIG, CONFIG_PATH_ARGS)
logging.config.fileConfig(LOG_CONFIG)

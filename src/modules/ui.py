
from datetime import datetime
from typing import Any
import os

from . import clock


CONSOLE_WIDTH = 80
CONSOLE_HEIGHT = 35


def draw_console() -> None:

    os.system(f"mode con cols={CONSOLE_WIDTH} lines={CONSOLE_HEIGHT}")


def _print_source_directories(src_dirs: list[str, ...]) -> None:

    if len(src_dirs) == 1:

        print(f"[!] Backup this directory:  {src_dirs[0]}\n\n")

        return

    print("[!] Backup these directories:")

    for directory in src_dirs:

        print(f"    [&] {directory}")

    print()


def print_header(
    app_name: str,
    json_obj: dict[str, Any],
    fill_char: str = '#'
) -> None:

    fill = fill_char * CONSOLE_WIDTH
    pad = fill_char * 4
    spaces = CONSOLE_WIDTH - 8

    print(fill, f'{pad}{app_name:^{spaces}}{pad}', fill, sep='\n', end="\n\n")

    print(
        f"[!] File backup starts at:  {json_obj['APP']['GO_TIME']}\n"
        f"[!] Maximum backups to store:  {json_obj['APP']['MAX_BACKUPS']}\n"
        f"[!] Save backup to:  {json_obj['APP']['DESTINATION']}"
    )

    _print_source_directories(json_obj['APP']['SOURCE'])

    print('.' * CONSOLE_WIDTH, end="\n\n")


def print_footer(fill_char: str = '#') -> None:

    fill = fill_char * CONSOLE_WIDTH
    print(fill, fill, sep='\n')


def print_stats_all_time(json_obj: dict[str, Any]) -> None:

    executions = json_obj['stats']['executions']
    total_data = json_obj['stats']['data_transacted'][0]
    hr_time = clock.from_seconds(json_obj["stats"]["work_time"])

    print()
    print('.' * CONSOLE_WIDTH, end="\n\n")

    print("[&] Stats all time:\n")
    print(
        f"[!] Archives saved by this script:  {executions}\n"
        f"[!] Data written to disk:  {total_data:.2f} GB\n"
        f"[!] Time spent handling files:  {hr_time}\n"
    )


def main() -> None:
    pass


if __name__ == "__main__":
    main()

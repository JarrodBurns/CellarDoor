
from datetime import datetime
from typing import Any
import os

from . import clock


def draw_console() -> None:

    os.system("mode con cols=64 lines=27")


def print_header(
    app_name: str,
    json_obj: dict[str, Any],
    fill_char: str = '#'
) -> None:

    fill = fill_char * 64
    pad = fill_char * 4

    print(fill, f'{pad}{app_name:^56}{pad}', fill, sep='\n', end="\n\n")

    print(
        f"[!] File backup starts at:  {json_obj['APP']['GO_TIME']}\n"
        f"[!] Maximum backups to store:  {json_obj['APP']['MAX_BACKUPS']}\n"
        # f"[!] Backup this directory:  {json_obj['APP']['SOURCE']}\n"
        f"[!] Save backup to:  {json_obj['APP']['DESTINATION']}"
    )

    t = json_obj['APP']['SOURCE']

    if len(t) > 1:

        print("[!] Backup these directories:")

        for i in t:
            print(f"    [&] {i}")

    else:
        print(f"[!] Backup this directory:  {json_obj['APP']['SOURCE']}\n")

    print('\n', '.' * 64, end="\n\n")


def print_footer(fill_char: str = '#') -> None:

    fill = fill_char * 64
    print(fill, fill, sep='\n')


def print_with_timestamp(statment: str, time_fmt: str = "%H-%M-%S") -> None:

    print(f"[{datetime.now():{time_fmt}}]  {statment}")


def print_stats_all_time(json_obj: dict[str, Any]) -> None:

    executions = json_obj['stats']['executions']
    total_data = json_obj['stats']['data_transacted'][0]
    hr_time = clock.from_seconds(json_obj["stats"]["work_time"])

    print('\n', '.' * 64, end="\n\n")

    print("[&] Stats all time:\n")
    print(
        f"[!] Times this script has been executed:  {executions}\n"
        f"[!] Data written to disk:  {total_data:.2f} GB\n"
        f"[!] Time spent handeling files:  {hr_time}\n"
    )


def main() -> None:
    pass


if __name__ == "__main__":
    main()

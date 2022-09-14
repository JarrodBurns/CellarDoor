
from datetime import datetime
from pathlib import Path
from time import sleep
import os

from . clock import Clock
from . import constants as C
from . import filemanager


def draw_console() -> None:

    os.system("mode con cols=64 lines=27")


def finalize_animation() -> None:

    print(f"\r[========]  Constructing archive.", flush=True)
    print_with_timestamp("Completed file backup.\n")


def in_progress_animation() -> None:

    animation = [
        "[=       ]",
        "[==      ]",
        "[===     ]",
        "[====    ]",
        "[=====   ]",
        "[======  ]",
        "[======= ]",
        "[========]",
        "[ =======]",
        "[  ======]",
        "[   =====]",
        "[    ====]",
        "[     ===]",
        "[      ==]",
        "[       =]",
        "[        ]"
    ]

    for frame in animation:
        print(frame, " Constructing archive.", end='\r', flush=True)
        sleep(.2)


def print_header(app_name: str, fill_char: str = '#') -> None:

    fill = fill_char * 64
    pad = fill_char * 4

    print(fill, f'{pad}{app_name:^56}{pad}', fill, sep='\n', end="\n\n")

    print(
        f"[!] File backup starts at:  {C.SETTINGS['APP']['GO_TIME']}\n"
        f"[!] Maximum backups to store:  {C.SETTINGS['APP']['MAX_BACKUPS']}\n"
        f"[!] Backup this directory:  {C.SETTINGS['APP']['SOURCE']}\n"
        f"[!] Save backup to:  {C.SETTINGS['APP']['DESTINATION']}\n"
    )

    print('.' * 64, end="\n\n")


def print_footer(fill_char: str = '#') -> None:

    fill = fill_char * 64
    print(fill, fill, sep='\n')


def print_with_timestamp(statment: str) -> None:

    print(f"[{datetime.now():{C.FMT_TIME}}]  {statment}")


def print_stats_all_time(path: Path) -> None:

    all_time = filemanager.get_json(path)

    executions = all_time['stats']['executions']
    total_data = all_time['stats']['data_transacted'][0]
    hr_time = Clock.clock_from_seconds(all_time["stats"]["work_time"])

    print('.' * 64, end="\n\n")

    print("[&] Stats all time:\n")
    print(
        f"[!] Times this script has been executed:  {executions}\n"
        f"[!] Data written to disk:  {total_data:.2f}\n"
        f"[!] Time spent handeling files:  {hr_time}\n"
    )


def main() -> None:
    pass


if __name__ == "__main__":
    main()
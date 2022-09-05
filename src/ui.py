
from datetime import datetime
from time import sleep

import filemanager


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


def print_header() -> None:

    SETTINGS = filemanager.get_settings()

    print(
        "################################################################\n"
        "####                 CellarDoor File Backup                 ####\n"
        "################################################################\n"
    )

    print(
        f"[!] File backup starts at:  {SETTINGS['APP']['GO_TIME']}\n"
        f"[!] Maximum backups to store:  {SETTINGS['APP']['MAX_BACKUPS']}\n"
        f"[!] Backup this directory:  {SETTINGS['APP']['SOURCE']}\n"
        f"[!] Save backup to:  {SETTINGS['APP']['DESTINATION']}\n"
    )

    print('.' * 64 + '\n')


def print_footer() -> None:

    line = '#' * 64
    print(line, line, sep='\n')


def print_with_timestamp(statment: str) -> None:

    current_time = datetime.now().strftime("%H:%M:%S")

    print(f"[{current_time}]  {statment}")

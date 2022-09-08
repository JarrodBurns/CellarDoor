
from datetime import datetime
from time import sleep

import filemanager
from clock import Clock


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

    SETTINGS = filemanager.get_app_settings()

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

    print('.' * 64, end="\n\n")


def print_footer() -> None:

    line = '#' * 64
    print(line, line, sep='\n')


def print_with_timestamp(statment: str) -> None:

    current_time = datetime.now().strftime("%H:%M:%S")

    print(f"[{current_time}]  {statment}")


def print_stats_all_time(path: str) -> None:

    all_time = filemanager.get_stats(path)

    executions = all_time['stats']['executions']
    total_data = all_time['stats']['data_transacted']

    hr_time = Clock.clock_from_seconds(all_time["stats"]["work_time"])
    hr_data = ' '.join([str(x) for x in total_data])

    print('.' * 64, end="\n\n")
    print("[&] Stats all time:\n")
    print(
        f"[!] Times this script has been executed:  {executions}\n"
        f"[!] Data written to disk:  {hr_data}\n"
        f"[!] Time spent handeling files:  {hr_time}\n"
    )

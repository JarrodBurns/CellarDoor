
from pathlib import Path
import subprocess


def new_task(task_name: str, xml_recipe: Path) -> None:
    """
    Register an automated task with Windows Task Scheduler

    task_name is a unique identifier you will use to manage the task.

    This function will automatically overwrite an existing task of
    the same name.
    """
    subprocess.run(
        [
            "schtasks.exe",
            "/Create",
            "/XML",
            xml_recipe,
            "/TN",
            task_name
        ],
        capture_output=True
    )


def delete_task(task_name: str) -> None:
    """
    Remove a Windows Task Scheduler task.
    """
    subprocess.run(
        [
            "schtasks.exe",
            "/Delete",
            "/F",
            "/TN",
            task_name,
        ],
        capture_output=True
    )


def run_task(task_name: str) -> None:
    """
    Run existing Windows Task Scheduler task.
    """
    subprocess.run(
        [
            "schtasks.exe",
            "/Run",
            "/TN",
            task_name
        ],
        capture_output=True
    )


def main() -> None:

    # Convience code to run a manual backup,
    # Will break if you haven't ran CellarDoor once before

    task = "CellarDoor File Backup"
    run_task(task)


if __name__ == "__main__":
    main()


from math import prod
import re


_CLOCK_MULTIPLES = [86_400, 3_600, 60, 1]
_CLOCK_INTERVALS = ["day", "hour", "minute", "second"]


def _clock_segments(seconds: int) -> tuple:

    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)

    return days, hours, minutes, seconds


def _parse_clock(clock: str) -> list:

    search = re.findall(r"[0-9]+", clock)

    parts = [int(i) for i in search]

    while len(parts) < 4:

        parts.insert(0, 0)

    return parts


def from_seconds(seconds: int) -> str:
    """
    Example output: 1 hours, 16 minutes, and 9 seconds
    Example output: 9 seconds
    """
    if seconds < 1:
        return "None"

    # Zip clock values and intervals for safer processing
    values = [
        list(i)
        for i
        in zip(_clock_segments(seconds), _CLOCK_INTERVALS)
    ]

    # Convert interval to plural
    for pos, value in enumerate(values):

        if value[0] != 1:

            values[pos][1] += 's'

    # Format to strings
    clock = [
        ' '.join([str(i[0]), i[1]])
        for i
        in values
        if i[0]
    ]

    # Check if "and" is needed
    if len(clock) > 1:
        clock.insert(-1, "and")

    # Add the commas; this format employs the oxford comma.
    if "and" in clock and len(clock) > 3:
        for i, _ in enumerate(clock[:-2]):
            clock[i] += ','

    return ' '.join(clock)


def to_seconds(clock: str) -> int:
    """
    Example intput: 1 hours, 16 minutes, and 9 seconds
    Example output: 9 seconds
    """
    seconds = 0

    for i in zip(_CLOCK_MULTIPLES, _parse_clock(clock)):
        seconds += prod(i)

    return seconds


def main() -> None:
    pass


if __name__ == "__main__":
    main()

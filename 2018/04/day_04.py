from collections import defaultdict
from datetime import datetime, timedelta
import re
from typing import DefaultDict, Dict


@dataclass
class Guard:
    num: int
    asleep: Dict[int, int]
    awake: Dict[int, int]

    def most_asleep_minute(self):
        max_val = max(asleep.keys(), key=lambda k: asleep[k])
        return max_val


def read_input(fname: str) -> Dict[str, Dict[int, str]]:
    """
    Reads the formatted input file and returns a dictionary with dates as keys,
    and values as a dictionary mapping minute to the line text. This is an
    intermediary function, which needs to be processed further to construct the
    data on the individual guards' sleeping patterns.
    """

    timestamp_pattern = re.compile(r"\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2})\]")
    date_entries: DefaultDict[str, Dict[int, str]] = defaultdict(dict)
    with open(fname, "r") as f:
        for line in f:
            m = timestamp_pattern.search(line)
            if m:
                timestamp = datetime.fromisoformat(m.group(1))
            else:
                raise RuntimeError("Error reading file. Is it correctly formatted?")
            if timestamp.hour != 0:
                date = format(timestamp + timedelta(days=1), "%m-%d")
                time = 0
            else:
                date = format(timestamp, "%m-%d")
                time = timestamp.minute
            date_entries[date][time] = line
    return date_entries


def track_guards(date_entries: Dict[str, Dict[int, str]]) -> Dict[int, Guard]:
    guards = Dict[int, Guard]

    for date, time in date_entries.items():
        guard = int(re.search(r"#(\d+)", date[0]).group(1))


def part_1(guards: Dict) -> None:
    pass

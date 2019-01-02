"""
I'm experimenting with MyPy for this challenge. I'm not convinced that I like
it.
"""

from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime, timedelta
import re
from typing import Callable, DefaultDict, Dict, List


def create_minute_dict() -> Dict[int, int]:
    """Start with -1 because any minute before midnight is coded as -1"""
    return {i: 0 for i in range(-1, 60)}


@dataclass
class Guard:
    """
    Data class to hold information about individual guards. Provides an int
    defaultdict as defaults for .asleep and .awake, but num is required

    Provides two methods: 
        most_asleep_minute returns the minute number (0 through 59) during
            which the guard was asleep the most.
        sum_asleep_minutes returns the total number of minutes that the guard
            was asleep
    """

    num: int
    asleep: Dict[int, int] = field(default_factory=create_minute_dict)
    awake: Dict[int, int] = field(default_factory=create_minute_dict)

    def most_asleep_minute(self) -> int:
        return max(self.asleep.keys(), key=lambda k: self.asleep[k])

    def sum_asleep_minutes(self) -> int:
        return sum(self.asleep.values())


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
                time = -1
            else:
                date = format(timestamp, "%m-%d")
                time = timestamp.minute
            date_entries[date][time] = line
    return date_entries


def track_guards(date_entries: Dict[str, Dict[int, str]]) -> Dict[int, Guard]:
    # Initialize a guards variable
    guards: Dict[int, Guard] = {}

    # For each date in date_entries, there will be a dictionary of entries
    # For each date, sort the entries by their keys (the minute that the block
    # in question starts). Determine the guard ID, and if that guard is not
    # already in the guards dict, add it as a Guard object with their id
    # Then assign the Guard instance at guards[id] to a variable
    for date, entries in date_entries.items():
        sorted_entries: List[int] = sorted(entries.keys())
        m = re.search(r"#(\d+)", entries[sorted_entries[0]])

        # I have to add in the "if m is None" section to satisfy MyPy
        # Because the result of re.search can be None, MyPy will yell at me if
        # I ask for re.search(...).group(1) because None does not have a .group
        # attribute. While it makes sense to ensure type stability, it doesn't
        # work so well in this case where I have to assume that there is a
        # guard ID in the first entry for a given date. Otherwise, the entry
        # isn't properly formatted.
        #
        # It turns out this actually came in handy because it allowed me to
        # find an error that came up in read_input() that I hadn't noticed
        # with the test file. I probably would've found it alright without
        # having this explicit error in place, and I could probably make the
        # error message more informative, but it definitely helped.
        if m is None:
            raise RuntimeError("Error parsing entry -- cannot find Guard ID")
        guard_id: int = int(m.group(1))
        if guard_id not in guards.keys():
            guards[guard_id] = Guard(guard_id)
        guard: Guard = guards[guard_id]

        # For each entry (range through len - 1 to allow for using i+1),
        # identify the current entry and the next entry.
        for i in range(len(entries) - 1):
            this_entry: int = sorted_entries[i]
            next_entry: int = sorted_entries[i + 1]

            # We start with i = 0, i+1 = 1
            # In this first block, the guard is always awake
            # So in the blocks where i+1 is even, the guard is asleep
            if (i + 1) % 2 == 0:
                for j in range(this_entry, next_entry):
                    guard.asleep[j] += 1
            else:
                for j in range(this_entry, next_entry):
                    guard.awake[j] += 1

    return guards


def part_1(guards: Dict[int, Guard]) -> int:
    """
    Returns the product of the id of the guard who slept the most minutes and
    the minute during which they were asleep the most
    """
    guard_id: int = 0
    max_minutes_asleep: int = 0
    most_asleep_minute: int = 0

    for guard in guards.values():
        if guard.sum_asleep_minutes() > max_minutes_asleep:
            guard_id = guard.num
            max_minutes_asleep = guard.sum_asleep_minutes()
            most_asleep_minute = guard.most_asleep_minute()

    return guard_id * most_asleep_minute


def part_2(guards: Dict[int, Guard]) -> int:
    """
    Returns the product of the ID of the guard who had the greatest number of
    days asleep at a particular minute and the number of that minute
    """
    guard_id: int = 0
    most_asleep_minute: int = 0
    minutes_slept_then: int = 0

    for guard in guards.values():
        if guard.asleep[guard.most_asleep_minute()] > minutes_slept_then:
            guard_id = guard.num
            most_asleep_minute = guard.most_asleep_minute()
            minutes_slept_then = guard.asleep[guard.most_asleep_minute()]

    return guard_id * most_asleep_minute

"""
2018 Day 7: The Sum of Its Parts
"""
from __future__ import annotations
from dataclasses import dataclass, field
import re
from string import ascii_uppercase
from typing import Dict, List, Set


@dataclass
class Step:
    """Data class to hold information about steps for sleigh construction"""

    letter: str
    parents: Set[str] = field(default_factory=set)
    children: Set[str] = field(default_factory=set)


def read_input(fname: str) -> Dict[str, Step]:
    """
    Reads in a text file of the format provided by the AoC website.

    Each line has the pattern "Step X must be finished before step Y can begin."
    This function returns a dictionary with the step letter as keys, and Step
    objects as the values. Each Step object has a set containing the letters of
    its parent steps and children steps.
    """
    results: Dict[str, Step] = {}
    pattern = re.compile(r"\b([A-Z])\b")
    with open(fname, "r") as f:
        for line in f:
            pair = pattern.findall(line)
            try:
                parent_step = pair[0]
                child_step = pair[1]
            except (IndexError, TypeError):
                raise RuntimeError("Error reading input file")

            if parent_step in results:
                results[parent_step].children.add(child_step)
            else:
                results[parent_step] = Step(parent_step, children={child_step})

            if child_step in results:
                results[child_step].parents.add(parent_step)
            else:
                results[child_step] = Step(child_step, parents={parent_step})

    return results


def part_1(steps: Dict[str, Step]) -> str:
    """
    Returns a string containing the step letters in the correct order.

    NOTE: This function modifies the `steps` input.
    """
    answer = ""

    # Set containing the letters that do not have any unsatisfied dependents
    ready = {step.letter for step in steps.values() if not step.parents}

    # As long as `ready` is not empty, take the first character alphabetically
    # Remove it from `ready`, and add it to `answer`
    while ready:
        letter = min(ready)
        ready.remove(letter)
        answer += letter

        # For each child step of that letter, remove the current letter from
        # that child's parent set
        for child in steps[letter].children:
            if letter in steps[child].parents:
                steps[child].parents.remove(letter)
            # If that child step does not have anything in the parents set, it
            # is ready to be added
            if not steps[child].parents:
                ready.add(child)

    return answer


def part_2(steps: Dict[str, Step], n_workers: int = 5, delay: int = 60) -> int:
    """
    Given a dict of Steps, a number of workers, and a delay (in seconds),
    return the number of seconds it takes to assemble the sleigh.

    NOTE: This function modifies the `steps` input.
    """

    timer = 0
    ready = {step.letter for step in steps.values() if not step.parents}

    # Each worker will be a dict with the letter it's working on and the time
    # remaining for that letter
    workers = [{"letter": "", "duration": 0} for _ in range(n_workers)]
    answer = ""

    # For each letter, add one (to account for 0-based indexing) and the delay
    # get the duration of that letter's work
    durations = {
        letter: ascii_uppercase.index(letter) + 1 + delay for letter in ascii_uppercase
    }

    while True:
        # I use a buffer variable for each run through so that I can put it in
        # alphabetical order before tacking it onto the answer
        buf = ""

        # For each worker, if it has a letter, decrement the duration by 1
        for w in workers:
            if w["letter"]:
                w["duration"] -= 1

            # If that worker's duration is 0, check if that letter is in the
            # steps dict. If it is, repeat the steps from part 1.
            if w["duration"] == 0:
                ltr = w["letter"]
                if ltr in steps:
                    for child in steps[ltr].children:
                        if ltr in steps[child].parents:
                            steps[child].parents.remove(ltr)
                        if not steps[child].parents:
                            ready.add(child)
                    buf += w["letter"]
                    w["letter"] = ""
                # If there are any steps ready to go, add the first one
                # (alphabetically) to the worker, and remove it from `ready`
                if ready:
                    current_letter = min(ready)
                    w["letter"] = current_letter
                    ready.remove(current_letter)
                    w["duration"] = durations[current_letter]
        answer += "".join(sorted(buf))

        # If the answer contains all of the steps, we're done!
        if set(answer) == set(steps):
            return timer
        # Otherwise, increment the timer and go back up to the top.
        timer += 1

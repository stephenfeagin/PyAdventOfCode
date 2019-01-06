"""
2018 Day 7: The Sum of Its Parts
"""
from __future__ import annotations
from collections import defaultdict
from dataclasses import dataclass, field
import re
from string import ascii_uppercase
from typing import DefaultDict, Dict, List, Set


@dataclass
class Step:
    letter: str
    parents: Set[str] = field(default_factory=set)
    children: Set[str] = field(default_factory=set)


def read_input(fname: str) -> Dict[str, Step]:
    results: Dict[str, Step] = {}
    pattern = re.compile(r"\b([A-Z])\b")
    with open(fname, "r") as f:
        for line in f:
            pair = pattern.findall(line)
            try:
                parent_step = pair[0]
                child_step = pair[1]
            except TypeError:
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
    answer = ""
    ready = {step.letter for step in steps.values() if not step.parents}

    while ready:
        letter = min(ready)
        ready.remove(letter)
        answer += letter

        for child in steps[letter].children:
            if letter in steps[child].parents:
                steps[child].parents.remove(letter)
            if not steps[child].parents:
                ready.add(child)

    return answer


def part_2(steps: Dict[str, Step], n_workers: int = 5, delay: int = 60) -> int:
    timer = 0
    ready = {step.letter for step in steps.values() if not step.parents}
    workers = [{"letter": "", "duration": 0} for _ in range(n_workers)]
    answer = ""
    durations = {
        letter: ascii_uppercase.index(letter) + 1 + delay for letter in ascii_uppercase
    }

    while True:
        buf = ""
        for w in workers:
            if w["letter"]:
                w["duration"] -= 1
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
                if ready:
                    current_letter = min(ready)
                    w["letter"] = current_letter
                    ready.remove(current_letter)
                    w["duration"] = durations[current_letter]
        answer += "".join(sorted(buf))
        if len(answer) == len(steps):
            return timer
        timer += 1


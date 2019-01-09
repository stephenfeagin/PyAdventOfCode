from __future__ import annotations
from collections import defaultdict
from copy import deepcopy
from dataclasses import dataclass, field
from pprint import pprint
import re
from typing import DefaultDict, Dict, List, Set


@dataclass
class Step:
    letter: str
    parents: Set = field(default_factory=set)
    children: Set = field(default_factory=set)


@dataclass
class Worker:
    letter: str = ""
    time: int = 0

    def get_work(self, instruction_set: Dict[str, Step], delay:int) -> str:
        try:
            self.letter = min(step for step in instruction_set.values() if not step.parents)
        except:
            pass
        else:
            self.time = ord(letter) - ord("A") + 1 + delay

    def do_work(self, instruction_set: Dict[str, Step], delay:int) -> str:
        if self.letter:
            self.time -= 1
        if not self.time:
            completed = self.letter
            return completed


def read_input(fname: str) -> Dict[str, Step]:
    results: Dict[str, Step] = {}
    pattern = re.compile(r"\b([A-Z])\b")
    with open(fname, "r") as f:
        for line in f:
            try:
                parent, child = pattern.findall(line)
            except ValueError:
                raise RuntimeError("Could not read input")
            if parent in results:
                results[parent].children.add(child)
            else:
                results[parent] = Step(parent, children={child})

            if child in results:
                results[child].parents.add(parent)
            else:
                results[child] = Step(child, parents={parent})
    return results


def part_1(instruction_set: Dict[str, Step]) -> str:
    instructions = deepcopy(instruction_set)
    answer: str = ""
    while len(answer) != len(instruction_set):
        ready = sorted(
            [step.letter for step in instructions.values() if not step.parents],
            reverse=True,
        )
        current = ready.pop()
        answer += current
        for step in instructions:
            try:
                instructions[step].parents.remove(current)
            except (KeyError, ValueError):
                pass
        instructions.pop(current)
    return answer


def part_2(instruction_set, n_workers, delay):


def part_2(instruction_set: Dict[str, Step], n_workers: int = 2, delay: int = 0) -> int:
    instructions = deepcopy(instruction_set)
    timer: int = 0
    completed: str = ""
    workers: List[Worker] = [Worker() for _ in range(n_workers)]

    while True:
        for w in workers:
            if w.letter:
                w.time -= 1
                if not w.time:
                    completed += w.letter
                    for step in instructions:
                        try:
                            instructions[step].parents.remove(w.letter)
                        except (KeyError, ValueError):
                            pass
                    w.letter = ""
            if not w.letter:
                ready = sorted(
                    [step.letter for step in instructions.values() if not step.parents],
                    reverse=True,
                )
                try:
                    w.letter = ready.pop()
                except IndexError:
                    continue
                else:
                    w.time = ord(w.letter) - ord("A") + 1 + delay
                    instructions.pop(w.letter)
        if not any(w.letter for w in workers):
            return timer
        else:
            timer += 1


if __name__ == "__main__":
    print("Part 1:", part_1(read_input("input.txt")))
    print("Part 2:", part_2(read_input("input.txt"), 5, 60))

from collections import defaultdict
from dataclasses import dataclass
import re
from string import ascii_uppercase
from typing import DefaultDict, Dict, List, Set, Tuple, Union


@dataclass
class Worker:
    letter: str = ""
    time: int = 0


def read_input(fname: str) -> Tuple[Set[str], DefaultDict[str, List[str]]]:
    pattern = re.compile(r"\b([A-Z])\b")
    instruction_set: DefaultDict[str, List[str]] = defaultdict(list)
    all_steps: Set[str] = set()

    with open(fname, "r") as f:
        for line in f:
            parent, child = pattern.findall(line)
            instruction_set[parent].append(child)
            all_steps.add(child)
            all_steps.add(parent)

    return all_steps, instruction_set


def find_ancestors(step: str, instruction_set: Dict[str, List[str]]) -> List[str]:
    results: List[str] = []
    for node, children in instruction_set.items():
        if step in children:
            results.append(node)
    return results


def find_ready_steps(
    all_steps: Set[str], instruction_set: Dict[str, List[str]]
) -> Set[str]:
    return {step for step in all_steps if not find_ancestors(step, instruction_set)}


def part_1(all_steps: Set[str], instruction_set: Dict[str, List[str]]) -> str:
    answer: str = ""
    ready = sorted(find_ready_steps(all_steps, instruction_set), reverse=True)
    while ready:
        current = ready.pop()
        all_steps.remove(current)
        instruction_set[current] = []
        answer += current
        ready = sorted(find_ready_steps(all_steps, instruction_set), reverse=True)

    return answer


def part_2(steps, instruction_set, n_workers, delay):
    answer: str = ""
    workers: List[Worker] = [Worker() for _ in range(n_workers)]
    in_progress: List[str] = []
    durations = {
        letter[1]: letter[0] + 1 + delay for letter in enumerate(ascii_uppercase)
    }
    timer: int = 0
    print("Time", end="\t")
    for i in range(n_workers):
        print(f"W{i}", end="\t")
    print("Answer")

    while True:
        for w in workers:

            if w.letter:
                w.time -= 1
                if w.time == 0:
                    answer += w.letter
                    steps.remove(w.letter)
                    in_progress.remove(w.letter)
                    instruction_set[w.letter] = [] 
                    w.letter = ""

            if not w.letter:
                ready = sorted(
                    [
                        step
                        for step in find_ready_steps(steps, instruction_set)
                        if step not in in_progress
                    ],
                    reverse=True,
                )
                try:
                    w.letter = ready.pop()
                except IndexError:
                    pass
                else:
                    w.time = durations[w.letter]
                    in_progress.append(w.letter)
        print(timer, end="\t")
        for w in workers:
            print(f"{w.letter or '.'}", end="\t")
        print(answer)
        if not any(w.letter for w in workers):
            return timer
        timer += 1


if __name__ == "__main__":
    INPUT = "test_input.txt"
    all_steps, instruction_set = read_input(INPUT)
    print("Part 1:", part_1(all_steps, instruction_set))

    all_steps, instruction_set = read_input("test_input.txt")
    print("Part 2 Test:", part_2(all_steps, instruction_set, 2, 0))

    all_steps, instruction_set = read_input("input.txt")
    print("Part 2:", part_2(all_steps, instruction_set, 5, 60))

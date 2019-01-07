from collections import defaultdict
import re
from typing import DefaultDict, Dict, List, Set, Tuple


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

def find_ready_steps(all_steps: Set[str], instruction_set: Dict[str, List[str]]) -> Set[str]:
    return {
        step for step in all_steps if not find_ancestors(step, instruction_set)
    }


def part_1(all_steps: Set[str], instruction_set: Dict[str, List[str]]) -> str:
    answer: str = ""
    ready = find_ready_steps(all_steps, instruction_set)
    while ready: 
        current = ready.pop()
        all_steps.remove(current)
        instruction_set[current] = []
        answer += current
        ready = find_ready_steps(all_steps, instruction_set)

    return answer


if __name__ == "__main__":
    INPUT = "test_input.txt"
    all_steps, instruction_set = read_input(INPUT)
    print("Part 1:", part_1(all_steps, instruction_set))

from collections import defaultdict
import re
from typing import DefaultDict, Dict, List, Set


def read_input(fname: str) -> DefaultDict[str, List[str]]:
    pattern = re.compile(r"\b([A-Z])\b")
    result: DefaultDict[str, List[str]] = defaultdict(list)

    with open(fname, "r") as f:
        for line in f:
            child, parent = pattern.findall(line)
            result[parent].append(child)

    return result


def find_ancestors(step: str, instruction_set: Dict[str, List[str]]) -> List[str]:
    results: List[str] = []
    for node, descendants in instruction_set.items():
        if step in descendants:
            results.append(node)
    return results


def find_ready_steps(instruction_set: Dict[str, List[str]]) -> Set[str]:
    return sorted({
        step for step in instruction_set if not find_ancestors(step, instruction_set)
    }, reverse=True)

def part_1(instruction_set: Dict[str, List[str]]) -> str:
    order: str = ""
    all_steps = set(instruction_set)
    while instruction_set: 
        ready = find_ready_steps(instruction_set)
        current = ready.pop()
        order += current
        instruction_set.pop(current)

    return order


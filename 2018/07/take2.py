from collections import defaultdict
import re
from string import ascii_uppercase
from typing import DefaultDict, Dict, List, Set, Tuple, Union


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


def part_2(
    all_steps: Set[str],
    instruction_set: Dict[str, List[str]],
    n_workers: int = 5,
    delay: int = 60,
) -> int:
    durations: Dict[str, int] = {
        ltr[1]: ltr[0] + 1 + delay for ltr in enumerate(ascii_uppercase)
    }
    workers: List[Dict[str, Union[str, int]]] = [
        {"letter": "", "time_left": 0} for _ in range(n_workers)
    ]
    timer: int = 0
    answer: str = ""
    ready: List[str]

    while True:
        print("Timer:", timer)
        for w in workers:
            print("Worker:", w)
            ready = sorted(
                find_ready_steps(all_steps, instruction_set),
                reverse=True
            )
            print("Ready:", ready)
            
            if w["letter"]:
                w["time_left"] -= 1
                if not w["time_left"]:
                    answer += w["letter"]
                    w["letter"] = ""
            
            if not w["letter"]:
                try:
                    w["letter"] = ready.pop()
                except IndexError:
                    pass
                else:
                    w["time_left"] = durations[w["letter"]]
                    all_steps.remove(w["letter"])
                    instruction_set[w["letter"]] = []
        if not any(w["letter"] for w in workers):
            return timer
        timer += 1
        
        
def part_2():
    answer: str = ""
    workers: Dict[str, int] = {}
    while True:
        
            
        # for _ in range(n_workers):
        #     try:
        #         current_letter = ready.pop()
        #     except IndexError:
        #         continue
        #     else:
        # workers.pop()......
        
        
if __name__ == "__main__":
    INPUT = "test_input.txt"
    all_steps, instruction_set = read_input(INPUT)
    print("Part 1:", part_1(all_steps, instruction_set))
    
    all_steps, instruction_set = read_input("test_input.txt")
    print("Part 2 Test:", part_2(all_steps, instruction_set, 2, 0))

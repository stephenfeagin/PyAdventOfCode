"""
This solution is adapted from Reddit user jonathan_paulson's solution on the
Day 7 Solutions Megathread -- 
https://www.reddit.com/r/adventofcode/comments/a3wmnl/2018_day_7_solutions/eb9sfnm

I still can't really tell why my original solution did not work.
"""

from collections import defaultdict
import re
from typing import DefaultDict, Dict, List, Set


class Challenge:
    def __init__(self):
        self.graph: DefaultDict[str, List[str]] = defaultdict(list)
        self.nodes: Set[str] = set()

    def read_input(self, fname: str) -> None:
        pattern = re.compile(r"\b([A-Z])\b")
        with open(fname, "r") as f:
            for line in f:
                first, second = pattern.findall(line)
                self.add_node(first, second)

    def add_node(self, first: str, second:str) -> None:
        self.graph[first].append(second)
        self.nodes.add(first)
        self.nodes.add(second)

    def get_depth(self) -> Dict[str, int]:
        depth: Dict[str, int] = {}
        for node in self.nodes:
            depth[node] = sum(node in arr for arr in self.graph.values())
        return depth

    def part_1(self) -> str:
        answer = ""
        depth = self.get_depth()
        queue = [n for n in self.nodes if depth[n] == 0]

        while queue:
            queue.sort(reverse=True)
            x = queue.pop()
            answer += x
            for n in self.graph[x]:
                depth[n] -= 1
                if depth[n] == 0:
                    queue.append(n)
        return answer

    def part_2(self, n_workers: int, delay: int) -> int:
        timer = 0
        workers = []
        depth = self.get_depth()
        queue = [n for n in self.nodes if depth[n] == 0]

        while len(workers) < n_workers and queue:
            queue.sort(reverse=True)
            x = queue.pop()
            workers.append((timer + delay + ord(x) - ord("A") + 1, x))
        
        while workers or queue: 
            if min(workers)[0] == timer:
                workers.sort(reverse=True)
                timer, x = workers.pop()
                for node in self.graph[x]:
                    depth[node] -= 1
                    if depth[node] == 0:
                        queue.append(node)
            
                while len(workers) < n_workers and queue:
                    queue.sort(reverse=True)
                    x = queue.pop()
                    workers.append((timer + delay + ord(x) - ord("A") + 1, x))
            else:
                timer += 1
        return timer


if __name__ == "__main__":
    example = Challenge()
    example.read_input("test_input.txt")
    print("Example Part 1:", example.part_1())
    print("Example Part 2:", example.part_2(2, 0))

    challenge = Challenge()
    challenge.read_input("input.txt")
    print("Challenge Part 1:", challenge.part_1())
    print("Challenge Part 2:", challenge.part_2(5, 60))


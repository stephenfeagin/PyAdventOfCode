"""
2018 Day 7: The Sum of Its Parts

This solution is adapted from Reddit user jonathan_paulson's solution on the
Day 7 Solutions Megathread -- 
https://www.reddit.com/r/adventofcode/comments/a3wmnl/2018_day_7_solutions/eb9sfnm

I still can't really tell why my original solution did not work.
"""

from collections import defaultdict
import re
from typing import DefaultDict, Dict, List, Set, Tuple


class Challenge:
    """
    A class to hold all of the data about the Day 7 challenge.

    It ended up making sense to put everything together to allow for a degree
    of communication and the ability to transparently modify in-place that I
    couldn't get quite satisfactory using separate functions.
    """

    def __init__(self) -> None:
        self.graph: DefaultDict[str, Set[str]] = defaultdict(set)
        self.nodes: Set[str] = set()

    def read_input(self, fname: str) -> None:
        """Reads an AoC input file and assigns each node to self.graph"""
        pattern = re.compile(r"\b([A-Z])\b")
        with open(fname, "r") as f:
            for line in f:
                first, second = pattern.findall(line)
                self.add_node(first, second)

    def add_node(self, first: str, second: str) -> None:
        """
        For each line in the instructions, the descendant step is added to the
        set for which the ancestor step is the key, in self.graph. Each step
        is also added to the set of all nodes.
        """
        self.graph[first].add(second)
        self.nodes.add(first)
        self.nodes.add(second)

    def get_depth(self) -> Dict[str, int]:
        """
        Returns a dictionary identifying the "depth," or number of ancestor
        nodes, that each node has. I created this as a method instead of an
        attribute so that I could modify depth values as I work through the
        graph.
        """
        depth: Dict[str, int] = {}
        for node in self.nodes:
            depth[node] = sum(node in arr for arr in self.graph.values())
        return depth

    def part_1(self) -> str:
        """In what order should the steps in your instructions be completed?"""
        answer = ""
        depth = self.get_depth()
        queue = [n for n in self.nodes if depth[n] == 0]

        while queue:
            queue.sort(reverse=True)
            letter = queue.pop()
            answer += letter
            for n in self.graph[letter]:
                depth[n] -= 1
                if depth[n] == 0:
                    queue.append(n)
        return answer

    def part_2(self, n_workers: int, delay: int) -> int:
        """
        With 5 workers and the 60+ second step durations described above, how
        long will it take to complete all of the steps?
        """
        timer = 0
        workers: List[Tuple[int, str]] = []
        depth = self.get_depth()
        queue: List[str] = [n for n in self.nodes if depth[n] == 0]

        while len(workers) < n_workers and queue:
            queue.sort(reverse=True)
            letter = queue.pop()
            workers.append((timer + delay + ord(letter) - ord("A") + 1, letter))

        while workers or queue:
            if min(workers)[0] == timer:
                workers.sort(reverse=True)
                timer, letter = workers.pop()
                for node in self.graph[letter]:
                    depth[node] -= 1
                    if depth[node] == 0:
                        queue.append(node)

                while len(workers) < n_workers and queue:
                    queue.sort(reverse=True)
                    letter = queue.pop()
                    workers.append((timer + delay + ord(letter) - ord("A") + 1, letter))
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

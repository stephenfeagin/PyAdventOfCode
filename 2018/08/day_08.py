"""
2018 Day 8: Memory Maneuver
"""

from __future__ import annotations
from typing import List, Tuple


class Tree:
    def __init__(
        self, data: List[int], address: Tuple[int, int], parent: Tree = None
    ) -> None:
        self.data = data
        self.parent = parent
        self.address = address
        self.n = self.data[0]
        self.m = self.data[1]
        self.metadata: Tuple[int] = self.data[-self.m :]
        self.children: List[Tree] = []


def read_input(fname: str) -> Tuple[int, ...]:
    with open(fname, "r") as f:
        data = tuple(int(x) for x in f.read().split())
    return data


def construct_tree(data: Tuple[int, ...]) -> Tree:
    n, m = data[:2]

    # The next line is only true for parent nodes, not sibling nodes
    # I need to figure out the logic to scan for siblings
    # Depth first, breadth first?
    root = Tree(root=(n, m), metadata=data[-m:])

    # Base case
    # Should this function be an iterator? nodes=[t for t in construct_tree(...)] perhaps?
    if n == 0:
        root.nodes = []
        return root
    else:
        return root


if __name__ == "__main__":
    data = read_input("test_input.txt")
    print(construct_tree(data))

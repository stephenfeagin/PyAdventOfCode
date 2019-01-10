"""
2018 Day 8: Memory Maneuver
"""

from __future__ import annotations
from dataclasses import dataclass, field
from pprint import pprint
from typing import List, Tuple


@dataclass
class Tree:
    root: Tuple[int, int] = field(default_factory=tuple)
    metadata: List[int] = field(default_factory=list)
    nodes: List[Tree] = field(default_factory=list)


def read_input(fname: str) -> Tuple[int, ...]:
    with open(fname, "r") as f:
        data = tuple(int(x) for x in f.read().split())
    return data

def construct_tree(data: Tuple[int, ...]) -> Tree:
    n, m = data[:2]
    if n == 0:
        return Tree(root=(n, m), metadata=data[2:2+m], nodes=[])
    else:
        return construct_tree(data[2:])

def construct_tree(data: Tuple[int, ...]) -> Tree:
    n, m = data[:2]
    
    # The next line is only true for parent nodes, not sibling nodes
    # I need to figure out the logic to scan for siblings
    # Depth first, breadth first?
    root = Tree(root=(n, m), metadata=data[-m:])

    # Base case
    # Should this function be an iterator? nodes=[t for t in construct_tree(...)] perhaps?
    if n == 0:
        root.nodes =[]
        return root
    else:
        return root


if __name__ == "__main__":
    data = read_input("test_input.txt")
    pprint(construct_tree(data))

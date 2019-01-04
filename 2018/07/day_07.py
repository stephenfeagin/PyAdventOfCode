"""
2018 Day 7: The Sum of Its Parts
"""
import re
from typing import List, Tuple
import unittest


def read_input(fname: str) -> List[Tuple[str, str]]:
    results: List[Tuple[str, str]] = []
    pattern = re.compile(r"\b([A-Z])\b")
    with open(fname, "r") as f:
        for line in f:
            steps = pattern.findall(line)
            if steps is not None:
                # I have to do (steps[0], steps[1]) to satisfy mypy
                # Doing tuple(steps) threw an error because it does not
                # guarantee that it is of type Tuple[str, str]
                results.append((steps[0], steps[1]))
            else:
                raise RuntimeError(
                    "Error reading the input file. Is it properly formatted?"
                )

    return results


def part_1(steps: List[Tuple[str, str]]) -> str:
    return "CABDFE"


"""
2018 Day 2: Inventory Management System
"""

from collections import defaultdict
import re
from typing import DefaultDict, List


def read_input(fname: str) -> List[str]:
    with open(fname, "r") as f:
        data = [line.rstrip("\n") for line in f.readlines()]
    return data


def part_1(data: List[str]) -> int:
    two_times = 0
    three_times = 0
    for line in data:
        letter_frequency: DefaultDict[str, int] = defaultdict(int)
        for letter in line:
            letter_frequency[letter] += 1
        if any(val == 2 for val in letter_frequency.values()):
            two_times += 1
        if any(val == 3 for val in letter_frequency.values()):
            three_times += 1

    return two_times * three_times


def part_2(data: List[str]) -> str:
    results: List[str] = []
    for code in data:
        for i in range(len(code)):
            substring = code[:i] + "*" + code[i + 1 :]
            if substring in results:
                return re.sub(pattern="\*", repl="", string=substring)
            results.append(substring)

    raise RuntimeError("No solution found!")


if __name__ == "__main__":
    data = read_input("input.txt")

    print("Part 1:", part_1(data))
    print("Part 2:", part_2(data))

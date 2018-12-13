"""
2018 Day 2: Inventory Management System
"""

from collections import defaultdict
import re

def part_1(data):
    two_times = 0
    three_times = 0
    for line in data:
        letter_frequency = defaultdict(int)
        for letter in line:
            letter_frequency[letter] += 1
        if any(val == 2 for val in letter_frequency.values()):
            two_times += 1
        if any(val == 3 for val in letter_frequency.values()):
            three_times += 1
    return two_times * three_times

def part_2(data):
    results = []
    for code in data:
        for i in range(len(code)):
            substring = code[:i] + "*" + code[i + 1:]
            if substring in results:
                return re.sub(pattern="\*", repl="", string=substring)
            results.append(substring)

if __name__ == "__main__":
    if __file__ == "aoc.py":
        INPUT = args.file
    else:
        INPUT = input("Puzzle input: ")
    with open(INPUT, "r") as f:
        DATA = [line.rstrip("\n") for line in f.readlines()]

    print("Part 1:")
    print(part_1(DATA))

    print("Part 2:")
    print(part_2(DATA))

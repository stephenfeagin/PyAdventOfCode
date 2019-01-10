"""
2018 Day 1: Chronal Calibration
"""
from collections import defaultdict
from typing import DefaultDict, List


def read_input(fname: str) -> List[int]:
    """Reads the input file as a list of integers"""
    with open(fname, "r") as f:
        data = [int(line) for line in f]
    return data


def part_1(data: List[int]) -> int:
    return sum(data)


def part_2(data: List[int]) -> int:
    """
    You start with frequency = 0, and the entire history of frequencies is [0]
    Because we may need to repeat the data list, we use a for loop nested in a while True
    loop.
    Each integer in the data list gets added to the current frequency. If the new
    current frequency is in the list of frequency history, break out of the loops and
    return that value.
    Otherwise, add the new frequency to the list of previous frequencies, and move to the
    next item in the data list
    """

    freqs: DefaultDict[int, int] = defaultdict(int)
    current_freq = 0
    freqs[current_freq] += 1
    while True:
        for change in data:
            current_freq += change
            if freqs[current_freq] > 0:
                return current_freq
            freqs[current_freq] += 1


if __name__ == "__main__":
    DATA = read_input("input.txt")

    print("Part 1:", part_1(DATA))
    print("Part 2:", part_2(DATA))

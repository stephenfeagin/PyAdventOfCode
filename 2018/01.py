"""
2018 Day 1: Chronal Calibration
"""
import unittest


def read_input(fname):
    """Reads the input file as a list of integers"""
    with open(fname, "r") as f:
        data = [int(line) for line in f]
    return data

def part_1(data):
    return sum(data)

def part_2(data):
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

    freqs = [0]
    current_freq = 0
    while True:
        for change in data:
            current_freq += change
            if current_freq in freqs:
                return current_freq
            freqs.append(current_freq)

# Testing
class TestDay1(unittest.TestCase):
    def test_part_1(self):
        test_cases = (([1, -2, 3, 1], 3),
                      ([1, 1, 1], 3),
                      ([1, 1, -2], 0),
                      ([-1, -2, -3], -6))
        for data, result in test_cases:
            self.assertEqual(part_1(data), result)

    def test_part_2(self):
        test_cases = (([1, -2, 3, 1], 2),
                      ([1, -1], 0),
                      ([3, 3, 4, -2, -4], 10),
                      ([-6, 3, 8, 5, -5], 5),
                      ([7, 7, -2, -7, -4], 14))
        for data, result in test_cases:
            self.assertEqual(part_2(data), result)

if __name__ == "__main__":
    if __file__ == "aoc.py":
        INPUT = args.file
    else:
        INPUT = input("Puzzle input:")
    DATA = read_input(INPUT)

    print(f"Part 1: {part_1(DATA)}")
    print(f"Part 2: {part_2(DATA)}")

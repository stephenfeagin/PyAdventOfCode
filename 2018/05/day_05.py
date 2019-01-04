"""
2018, Day 5: Alchemical Reduction

You've managed to sneak in to the prototype suit manufacturing lab. The Elves
are making decent progress, but are still struggling with the suit's size
reduction capabilities.

While the very latest in 1518 alchemical technology might have solved their
problem eventually, you can do better. You scan the chemical composition of the
suit's material and discover that it is formed by extremely long polymers (one
of which is available as your puzzle input).

The polymer is formed by smaller units which, when triggered, react with each
other such that two adjacent units of the same type and opposite polarity are
destroyed. Units' types are represented by letters; units' polarity is
represented by capitalization. For instance, r and R are units with the same
type but opposite polarity, whereas r and s are entirely different types and do
not react.
"""

import re
from typing import List, Set
import unittest


def part_1(polymer: str) -> int:
    """
    How many units remain after fully reacting the polymer you scanned?

    This answer is shamelessly copied from a post by Reddit user eltrufas.
    I had originally solved this using the method shown below in this
    docstring, which worked fine but would crash when attempting to use it in
    part 2 (MemoryError).

    i: int = 0

    # Go to len(polymer) - 1 to allow for using i+1
    while i < (len(polymer) - 1):
        # If the two letters match except for case, then drop those them
        # You then have to decrement i by 1 to allow for the possibility that
        # i-1 == i+2, which are now adjacent
        if polymer[i].swapcase() == polymer[i + 1]:
            polymer = polymer[:i] + polymer[i + 2 :]
            i -= 1
        else:
            i += 1
    return len(polymer)
    """

    # Initialize an empty list to hold the characters that will be in the
    # final polymer
    result: List[str] = []

    # For each character, check if the result list is empty.
    # If it's not empty and the last item in it is equal to the opposite case
    # of the character, remove the last item from results and move on to the
    # next character.
    # Otherwise, append the character to the end of the results vector.
    for char in polymer:
        if result and char == result[-1].swapcase():
            result.pop()

        else:
            result.append(char)

    return len(result)


def part_2(polymer: str) -> int:
    """
    One of the unit types is causing problems: it's preventing the polymer
    from collapsing as much as it should. Your goal is to figure out which
    unit type is causing the most problems, remove all instances of it
    (regardless of polarity), fully react the remaining polymer, and measure
    its length.
    """
    letters: Set = set(polymer.casefold())
    lengths: List[int] = []

    for letter in letters:
        sub_polymer: str = re.sub(
            pattern=letter, repl="", string=polymer, flags=re.IGNORECASE
        )
        lengths.append(part_1(sub_polymer))

    return min(lengths)


class TestDay5(unittest.TestCase):
    def setUp(self):
        with open("test_input.txt", "r") as f:
            self.TEST_CASE = f.read().strip()

    def test_part_1(self):
        self.assertEqual(part_1(self.TEST_CASE), 10)

    def test_part_2(self):
        self.assertEqual(part_2(self.TEST_CASE), 4)

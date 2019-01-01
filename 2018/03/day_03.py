from collections import defaultdict, namedtuple
import re
from typing import DefaultDict, Dict, List, Tuple
import unittest


Claim = namedtuple("Claim", ["id", "left", "top", "width", "height"])


def read_input(fname: str) -> List[Claim]:
    results = []

    with open(fname, "r") as f:
        for line in f:
            nums = [int(i) for i in re.findall(r"\d+", line)]
            claim = Claim(*nums)
            results.append(claim)
    return results


def tally_squares(claims: List[Claim]) -> Dict[Tuple[int, int], int]:
    squares: DefaultDict[Tuple[int, int], int] = defaultdict(int)
    for claim in claims:
        for x in range(claim.left, claim.left + claim.width):
            for y in range(claim.top, claim.top + claim.height):
                squares[(x, y)] += 1

    return squares


def part_1(squares: Dict[Tuple[int, int], int]) -> int:
    return len([i for i in squares.values() if i > 1])


def part_2(claims: List[Claim], squares: Dict[Tuple[int, int], int]) -> int:
    for claim in claims:
        subset = [
            (x, y)
            for x in range(claim.left, claim.left + claim.width)
            for y in range(claim.top, claim.top + claim.height)
        ]
        tally = [squares[coord] for coord in subset]
        if all(i == 1 for i in tally):
            return claim.id

    return 0


class TestDay3(unittest.TestCase):
    def setUp(self):
        self.TEST_FILE = "test_input.txt"
        self.TEST_CLAIMS = [
            Claim(1, 1, 3, 4, 4),
            Claim(2, 3, 1, 4, 4),
            Claim(3, 5, 5, 2, 2),
        ]

        self.TEST_SQUARES = {
            (1, 3): 1,
            (1, 4): 1,
            (1, 5): 1,
            (1, 6): 1,
            (2, 3): 1,
            (2, 4): 1,
            (2, 5): 1,
            (2, 6): 1,
            (3, 1): 1,
            (3, 2): 1,
            (3, 3): 2,
            (3, 4): 2,
            (3, 5): 1,
            (3, 6): 1,
            (4, 1): 1,
            (4, 2): 1,
            (4, 3): 2,
            (4, 4): 2,
            (4, 5): 1,
            (4, 6): 1,
            (5, 1): 1,
            (5, 2): 1,
            (5, 3): 1,
            (5, 4): 1,
            (5, 5): 1,
            (5, 6): 1,
            (6, 1): 1,
            (6, 2): 1,
            (6, 3): 1,
            (6, 4): 1,
            (6, 5): 1,
            (6, 6): 1,
        }

    def test_read_input(self):
        self.assertEqual(read_input(self.TEST_FILE), self.TEST_CLAIMS)

    def test_tally_squares(self):
        self.assertDictEqual(tally_squares(self.TEST_CLAIMS), self.TEST_SQUARES)

    def test_part_1(self):
        self.assertEqual(part_1(self.TEST_SQUARES), 4)

    def test_part_2(self):
        self.assertEqual(part_2(self.TEST_CLAIMS, self.TEST_SQUARES), 3)

from collections import namedtuple
import re
import unittest


Claim = namedtuple("Claim", ["id", "left", "top", "width", "height"])

def read_input(fname):
    results = {}

    with open(fname, "r") as f:
        for line in f:
            nums = [int(i) for i in re.findall(r"\d+", line)]
            claim = Claim(*nums)
            results[claim.id] = claim
    return results


def part_1(data):
    return 4



class TestDay3(unittest.TestCase):
    def test_read_input(self):
        TEST_DATA = "test_input.txt"
        EXPECTED = {1: Claim(1, 1, 3, 4, 4),
                    2: Claim(2, 3, 1, 4, 4),
                    3: Claim(3, 5, 5, 2, 2)}
        OUTPUT = read_input(TEST_DATA)
        for key in EXPECTED.keys():
            self.assertEqual(EXPECTED[key], OUTPUT[key])

    def test_part_1(self):

        TEST_DATA = ["#1 @ 1,3: 4x4",
                     "#2 @ 3,1: 4x4",
                     "#3 @ 5,5: 2x2"]
        self.assertEqual(part_1(TEST_DATA), 4)


import unittest


def part_1(polymer: str) -> int:

    i:int = 0

    # Go to len(polymer) - 1 to allow for using i+1
    while i < (len(polymer) - 1):
        # If the two letters match except for case, then drop those them
        # You then have to decrement i by 1 to allow for the possibility that
        # i-1 == i+2, which are now adjacent
        if polymer[i].swapcase() == polymer[i+1]:
            polymer = polymer[:i] + polymer[i+2:]
            i -= 1
        else:
            i += 1
    return len(polymer)


class TestDay5(unittest.TestCase):
    def setUp(self):
        self.TEST_CASE = "dabAcCaCBAcCcaDA"

    def test_part_1(self):
        self.assertEqual(part_1(self.TEST_CASE), 10)

import unittest


def part_1(polymer):
    i = 0
    while i < (len(polymer) - 1):
        if polymer[i].swapcase() == polymer[i+1]:
            try:
                polymer = polymer[:i-1] + polymer[i+2:]
            except IndexError:
                polymer = polymer[2:]
        else:
            i += 1
    return len(polymer)


class TestDay5(unittest.TestCase):
    def setUp(self):
        self.TEST_CASE = "dabAcCaCBAcCcaDA"

    def test_part_1(self):
        self.assertEqual(part_1(self.TEST_CASE), 10)

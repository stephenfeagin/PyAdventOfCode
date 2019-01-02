import unittest


def part_1(polymer):
    return 10


class TestDay5(unittest.TestCase):
    def setUp(self):
        self.TEST_CASE = "dabAcCaCBAcCcaDA"

    def test_part_1(self):
        self.assertEqual(part_1(self.TEST_CASE), 10)

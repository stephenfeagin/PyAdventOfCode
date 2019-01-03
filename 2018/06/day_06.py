from dataclasses import dataclass
import unittest


@dataclass
class Point:
    x: int
    y: int


def read_input(fname):
    pass


def part_1(points):
    pass


class TestDay6(unittest.TestCase):
    def setUp(self):
        self.POINTS: Dict[int, Point] = {
                1: Point(1, 1),
                2: Point(1, 6),
                3: Point(8, 3),
                4: Point(3, 4),
                5: Point(5, 5),
                6: Point(8, 9),
        }

    def test_read_input(self):
        self.assertEqual(read_input("test_input.txt"), self.POINTS)

    def test_part_1(self):
        self.assertEqual(part_1(self.POINTS), 17)


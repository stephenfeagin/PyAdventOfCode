from dataclasses import dataclass
from typing import Dict, List, Tuple
import unittest


@dataclass
class Point:
    x: int
    y: int


def read_input(fname: str) -> List[Point]:
    results: List[Point] = []
    with open(fname, "r") as f:
        for line in f:
            pair = [int(string) for string in line.split(",")]
            results.append(Point(*pair))

    return results


def define_canvas(min_x: int, min_y: int, max_x: int, max_y: int) -> Dict[Tuple, Point]:
    return {(x, y) for x in range(min_x, max_x + 1) for y in range(min_y, max_y + 1)}


def part_1(points):
    # I know that the points with either x or y being the maximum or minimum
    # of the group will have infinite areas, so I can eliminate them
    max_x: int = max(pt.x for pt in points)
    min_x: int = min(pt.x for pt in points)
    max_y: int = max(pt.y for pt in points)
    min_y: int = min(pt.y for pt in points)

    candidates: List[Point] = [
        pt for pt in points if pt.x not in (max_x, min_x) and pt.y not in (max_y, min_y)
    ]

    return candidates[0]


class TestDay6(unittest.TestCase):
    def setUp(self):
        self.POINTS: List[Point] = [
            Point(1, 1),
            Point(1, 6),
            Point(8, 3),
            Point(3, 4),
            Point(5, 5),
            Point(8, 9),
        ]

    def test_read_input(self):
        self.assertEqual(read_input("test_input.txt"), self.POINTS)

    def test_part_1(self):
        self.assertEqual(part_1(self.POINTS), 17)

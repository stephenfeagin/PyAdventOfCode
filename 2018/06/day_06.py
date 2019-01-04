from __future__ import annotations
from collections import defaultdict
from dataclasses import dataclass
from typing import DefaultDict, List, Set, Union
import unittest


@dataclass(frozen=True)
class Point:
    """
    Class for dealing with points in a Cartesian plane. Provides functions for
    calculating Manhattan distances and finding the nearest point based on
    Manhattan distance.
    """

    x: int
    y: int

    def get_distance(self, other: Point) -> int:
        """Calculates the Manhattan distance to another point"""
        x_dist = abs(self.x - other.x)
        y_dist = abs(self.y - other.y)
        return x_dist + y_dist

    def find_nearest_point(self, points: List[Point]) -> Union[Point, None]:
        """
        Returns a Point that is the closest to self, measured by Manhattan
        distance. If two or more points are equally close, return None.
        """
        distances: DefaultDict[int, List[Point]] = defaultdict(list)

        for pt in points:
            dist = self.get_distance(pt)
            distances[dist].append(pt)

        nearest = distances[min(distances.keys())]
        if len(nearest) > 1:
            return None
        else:
            return nearest[0]


def read_input(fname: str) -> List[Point]:
    results: List[Point] = []
    with open(fname, "r") as f:
        for line in f:
            pair = [int(string) for string in line.split(",")]
            results.append(Point(*pair))

    return results


def define_canvas(min_x: int, min_y: int, max_x: int, max_y: int) -> Set[Point]:
    """Returns the set of all points in a plane bounded by the arguments"""
    return set(Point(x, y) for x in range(min_x, max_x + 1) for y in range(min_y, max_y + 1))


def part_1(points: List[Point]) -> int:
    max_x: int = max(pt.x for pt in points)
    min_x: int = min(pt.x for pt in points)
    max_y: int = max(pt.y for pt in points)
    min_y: int = min(pt.y for pt in points)

    # Get the canvas that we're working with. This helps to eliminate points
    # with non-finite areas
    canvas = define_canvas(min_x, min_y, max_x, max_y)

    # Make a default dict to keep track of the areas of the points
    pt_areas: DefaultDict[Point, int] = defaultdict(int)

    for pt in canvas:
        nearest = pt.find_nearest_point(points)
        if nearest is not None:
            pt_areas[nearest] += 1

    return max(pt_areas.values())


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

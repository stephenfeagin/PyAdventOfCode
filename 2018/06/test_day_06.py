from day_06 import part_1, part_2, Point, read_input


POINTS = [Point(1, 1), Point(1, 6), Point(8, 3), Point(3, 4), Point(5, 5), Point(8, 9)]


def test_read_input():
    assert read_input("test_input.txt") == POINTS


def test_part_1():
    assert part_1(POINTS) == 17


def test_part_2():
    assert part_2(POINTS, 32) == 16

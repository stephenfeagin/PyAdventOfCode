from day_07 import part_1, read_input


STEPS = [
    ("C", "A"),
    ("C", "F"),
    ("A", "B"),
    ("A", "D"),
    ("B", "E"),
    ("D", "E"),
    ("F", "E"),
]


def test_read_input():
    assert read_input("test_input.txt") == STEPS


def test_part_1():
    assert part_1(STEPS) == "CABDFE"

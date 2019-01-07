import pytest

from day_07 import part_1, part_2, read_input, Step


@pytest.fixture
def steps():
    steps = {
        "A": Step(letter="A", parents={"C"}, children={"D", "B"}),
        "B": Step(letter="B", parents={"A"}, children={"E"}),
        "C": Step(letter="C", parents=set(), children={"F", "A"}),
        "D": Step(letter="D", parents={"A"}, children={"E"}),
        "E": Step(letter="E", parents={"F", "D", "B"}, children=set()),
        "F": Step(letter="F", parents={"C"}, children={"E"}),
    }
    return steps


def test_read_input(steps):
    assert read_input("test_input.txt") == steps


def test_part_1(steps):
    assert part_1(steps) == "CABDFE"


def test_part_2(steps):
    assert part_2(steps, 2, 0) == 15

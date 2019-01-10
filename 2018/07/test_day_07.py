import pytest

from day_07 import Challenge


@pytest.fixture
def steps():
    steps = {"A": {"B", "D"}, "B": {"E"}, "C": {"A", "F"}, "D": {"E"}, "F": {"E"}}
    return steps


@pytest.fixture
def example():
    example = Challenge()
    example.read_input("test_input.txt")
    return example


def test_read_input(example, steps):
    assert example.graph == steps


def test_part_1(example):
    assert example.part_1() == "CABDFE"


def test_part_2(example):
    assert example.part_2(2, 0) == 15

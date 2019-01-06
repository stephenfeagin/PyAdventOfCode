from day_07 import part_1, read_input, Step


STEPS = {
        "A": Step(letter="A", parents={"C"}, children={"D", "B"}),
        "B": Step(letter="B", parents={"A"}, children={"E"}),
        "C": Step(letter="C", parents=set(), children={"F", "A"}),
        "D": Step(letter="D", parents={"A"}, children={"E"}),
        "E": Step(letter="E", parents={"F", "D", "B"}, children=set()),
        "F": Step(letter="F", parents={"C"}, children={"E"}),
        }


def test_read_input():
    assert read_input("test_input.txt") == STEPS


def test_part_1():
    assert part_1(STEPS) == "CABDFE"

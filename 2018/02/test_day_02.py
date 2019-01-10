from day_02 import part_1, part_2, read_input


def test_part_1():
    data = read_input("test_input_1.txt")
    assert part_1(data) == 12


def test_part_2():
    data = read_input("test_input_2.txt")
    assert part_2(data) == "fgij"


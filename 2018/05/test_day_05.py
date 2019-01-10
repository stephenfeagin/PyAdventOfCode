from day_05 import part_1, part_2


with open("test_input.txt", "r") as f:
    TEST_CASE = f.read().strip()


def test_part_1():
    assert part_1(TEST_CASE) == 10


def test_part_2():
    assert part_2(TEST_CASE) == 4

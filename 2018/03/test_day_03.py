from day_03 import Claim, part_1, part_2, read_input, tally_squares


TEST_FILE = "test_input.txt"
TEST_CLAIMS = [Claim(1, 1, 3, 4, 4), Claim(2, 3, 1, 4, 4), Claim(3, 5, 5, 2, 2)]

TEST_SQUARES = {
    (1, 3): 1,
    (1, 4): 1,
    (1, 5): 1,
    (1, 6): 1,
    (2, 3): 1,
    (2, 4): 1,
    (2, 5): 1,
    (2, 6): 1,
    (3, 1): 1,
    (3, 2): 1,
    (3, 3): 2,
    (3, 4): 2,
    (3, 5): 1,
    (3, 6): 1,
    (4, 1): 1,
    (4, 2): 1,
    (4, 3): 2,
    (4, 4): 2,
    (4, 5): 1,
    (4, 6): 1,
    (5, 1): 1,
    (5, 2): 1,
    (5, 3): 1,
    (5, 4): 1,
    (5, 5): 1,
    (5, 6): 1,
    (6, 1): 1,
    (6, 2): 1,
    (6, 3): 1,
    (6, 4): 1,
    (6, 5): 1,
    (6, 6): 1,
}


def test_read_input():
    assert read_input(TEST_FILE) == TEST_CLAIMS


def test_tally_squares():
    assert tally_squares(TEST_CLAIMS) == TEST_SQUARES


def test_part_1():
    assert part_1(TEST_SQUARES) == 4


def test_part_2():
    assert part_2(TEST_CLAIMS, TEST_SQUARES) == 3

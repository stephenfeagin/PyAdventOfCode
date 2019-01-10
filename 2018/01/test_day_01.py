from day_01 import part_1, part_2


def test_part_1():
    test_cases = (
        ([1, -2, 3, 1], 3),
        ([1, 1, 1], 3),
        ([1, 1, -2], 0),
        ([-1, -2, -3], -6),
     )
    for data, result in test_cases:
       assert part_1(data) == result


def test_part_2():
    test_cases = (
        ([1, -2, 3, 1], 2),
        ([1, -1], 0),
        ([3, 3, 4, -2, -4], 10),
        ([-6, 3, 8, 5, -5], 5),
        ([7, 7, -2, -7, -4], 14),
    )
    for data, result in test_cases:
        assert part_2(data) == result

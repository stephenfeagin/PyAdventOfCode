"""
2019 Day 1 Tests
"""
from day01 import find_fuel_req, find_total_fuel_req


def test_find_fuel_req():
    test_cases = (
        (12, 2),
        (14, 2),
        (1969, 654),
        (100756, 33583),
    )
    for data, result in test_cases:
        assert find_fuel_req(data) == result


def test_find_total_fuel_req():
    test_cases = ((14, 2), (1969, 966), (100756, 50346))
    for data, result in test_cases:
        assert find_total_fuel_req(data) == result

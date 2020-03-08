"""
2019 Day 1: The Tyranny of the Rocket Equation

Part 1:
    Fuel required to launch a given module is based on its mass. Specifically,
    to find the fuel required for a module, take its mass, divide by three,
    round down, then subtract 2.
    What is the sum of the fuel requirements for all of the modules on your spacecraft?

Part 2:
    Fuel itself requires fuel just like a module - take its mass, divide by three,
    round down, and subtract 2. However, that fuel also requires fuel, and that fuel
    requires fuel, and so on. Any mass that would require negative fuel should instead
    be treated as if it requires zero fuel; the remaining mass, if any, is instead
    handled by wishing really hard, which has no mass and is outside the scope of this
    calculation.

    So, for each module mass, calculate its fuel and add it to the total. Then, treat
    the fuel amount you just calculated as the input mass and repeat the process,
    continuing until a fuel requirement is zero or negative.
"""
import math


def read_input(fname):
    """Reads input file as a list of integers"""
    with open(fname, "r") as f:
        try:
            data = [int(line) for line in f]
        except ValueError:
            raise
    return data


def find_fuel_req(mass):
    """Returns the amount of fuel required to launch a module given its mass."""
    return math.floor(mass / 3) - 2


def part1(mass_list):
    return sum(find_fuel_req(mass) for mass in mass_list)


def find_total_fuel_req(mass):
    fuel_req = find_fuel_req(mass)
    total_fuel_req = fuel_req
    while fuel_req > 0:
        fuel_fuel_req = max(find_fuel_req(fuel_req), 0)
        total_fuel_req += fuel_fuel_req
        fuel_req = fuel_fuel_req
    return total_fuel_req


def part2(mass_list):
    return sum(find_total_fuel_req(mass) for mass in mass_list)


if __name__ == "__main__":
    data = read_input("input.txt")
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))

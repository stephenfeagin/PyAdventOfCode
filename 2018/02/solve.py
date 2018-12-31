from day_02 import part_1, part_2


INPUT = "input.txt"
with open(INPUT, "r") as f:
    DATA = [line.rstrip("\n") for line in f.readlines()]

print("Part 1:", part_1(DATA))
print("Part 2:", part_2(DATA))


from day_01 import part_1, part_2


INPUT = "input.txt"

with open(INPUT, "r") as f:
    NUM = int(f.read())

print("Part 1: ", part_1(NUM))
print("Part 2: ", part_2(NUM))


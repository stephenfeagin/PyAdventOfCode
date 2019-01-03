from day_05 import part_1, part_2


with open("input.txt", "r") as f:
    polymer = f.read().rstrip()

print("Part 1:", part_1(polymer))
print("Part 2:", part_2(polymer))

from day_04 import part_1, part_2, read_input, track_guards


INPUT = "input.txt"
date_entries = read_input(INPUT)
guards = track_guards(date_entries)
print("Part 1:", part_1(guards))
print("Part 2:", part_2(guards))

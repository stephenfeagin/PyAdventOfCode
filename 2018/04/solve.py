from day_04 import Guard, part_1, read_input, track_guards


INPUT = "input.txt"
date_entries = read_input(INPUT)
guards = track_guards(date_entries)
print("Part 1:", part_1(guards))

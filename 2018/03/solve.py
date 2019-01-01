from day_03 import read_input, tally_squares, part_1, part_2


input_file = "input.txt"
input_data = read_input(input_file)
squares = tally_squares(input_data)

print("Part 1:", part_1(squares))
print("Part 2:", part_2(input_data, squares))

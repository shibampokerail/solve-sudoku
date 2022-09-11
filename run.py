from main import Reader, Analyzer

read = Reader("problem1.txt")
grid = read.unsolved_grid
nine_groups = read.array_3d
print(nine_groups)

analyze = Analyzer(grid)
# print((analyze.empty_positions))
# analyze.get_row_data((analyze.empty_positions)[0][0])
# analyze.get_column_data(8)
possible_numbers_from_row_check = analyze.row_and_column_check([6, 8])
analyze.check_redundancy_in_groups([6, 8], grid, possible_numbers_from_row_check)
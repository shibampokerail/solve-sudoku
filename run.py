from main import Reader, Analyzer


# print((analyze.empty_positions))
# analyze.get_row_data((analyze.empty_positions)[0][0])
# analyze.get_column_data(8)
class Solver:
    def __init__(self):
        read = Reader("problem1.txt")
        self.grid = read.unsolved_grid
        self.nine_groups = read.generate_nine_groups()
        self.analyze = Analyzer(self.grid)
        self.empty_positions = self.analyze.find_empty_positions()
        print(self.grid)

    def get_probable_value(self, empty_position):
        possible_numbers_from_row_check = self.analyze.row_and_column_check(empty_position)
        possibilities = self.analyze.check_redundancy_in_groups(empty_position, self.nine_groups,
                                                                possible_numbers_from_row_check)
        return possibilities

    def get_all_probable_values(self, solve_if_one=True):
        probable_values = []

        for empty_position in self.empty_positions:

            probable_values = self.get_probable_value(empty_position)
            print(probable_values)
            # solve if one probability
            if len(probable_values) == 1 and solve_if_one:
                self._solve(empty_position, probable_values[0])

                self.empty_positions[self.empty_positions.index(empty_position)] = []
                self.empty_positions.remove([])
        return probable_values

    def _solve(self, empty_position: list, value):
        self.grid[empty_position[0]][empty_position[1]] = value

    # display feature only for devlopment

    def show_grid(self):
        for i in self.grid:
            print(i)


shibam = Solver()
shibam.show_grid()
shibam.get_all_probable_values()
print("----------")
shibam.show_grid()

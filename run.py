from main import Reader, Analyzer


# print((analyze.empty_positions))
# analyze.get_row_data((analyze.empty_positions)[0][0])
# analyze.get_column_data(8)
class Solver:
    def __init__(self, filename):
        self.filename = filename
        self.read = Reader(filename=self.filename)
        self.grid = self.read.unsolved_grid
        self.nine_groups = self.read.generate_nine_groups()
        self.analyze = Analyzer(self.grid)
        self.empty_positions = self.analyze.find_empty_positions()
        self.solved_grid = []
        self.rough_grid = []
        print(self.grid)

    def get_probable_value(self, empty_position):
        possible_numbers_from_row_check = self.analyze.row_and_column_check(empty_position)

        possibilities = self.analyze.check_redundancy_in_groups(empty_position, self.nine_groups,
                                                                possible_numbers_from_row_check)
        return possibilities

    def get_all_probable_values(self, solve_if_one=False):
        probable_values = []
        possibilities = []
        print("-------")
        for empty_position in self.empty_positions:

            probable_values = self.get_probable_value(empty_position)
            print(probable_values, f"|{empty_position}|")
            # solve if one probability
            if len(probable_values) == 1 and solve_if_one:
                self._solve(empty_position, probable_values[0])

                self.empty_positions[self.empty_positions.index(empty_position)] = []
                self.empty_positions.remove([])
            possibilities.append(probable_values)

        return possibilities

    def _solve(self, empty_position: list, value):
        self.grid[empty_position[0]][empty_position[1]] = value
        self.update_grids()

    def solve_with_rowcol_and_grouping(self):

        def check_one_probable_value(probable_array):
            for i in probable_array:
                if len(i) == 1:
                    return True

        probable_arrays = self.get_all_probable_values()
        exist_one_probable_value = check_one_probable_value(probable_arrays)

        if exist_one_probable_value:
            while exist_one_probable_value:
                self.get_all_probable_values(solve_if_one=True)
                probable_arrays = self.get_all_probable_values()
                exist_one_probable_value = check_one_probable_value(probable_arrays)

        for i in probable_arrays:
            pass

    def solve_with_random_possibilities(self, empty_positions, probabilities):
        pass

    def update_grids(self):
        three_d_grid = self.read.generate_3d_array(self.grid)
        self.read.row_arrays = self.read.generate_row_arrays(three_d_grid)
        self.nine_groups = self.read.generate_nine_groups()




    # display feature only for devlopment

    def show_grid(self):
        for i in self.grid:
            print(i)


shibam = Solver("problem1.txt")
shibam.show_grid()
# shibam.solve_with_rowcol_and_grouping()
shibam.solve_with_rowcol_and_grouping()
print("--------------------------")
shibam.show_grid()
print(shibam.get_probable_value([1, 0]))

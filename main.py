import os

# make it scalabe to any dimension of matrix // search if sudoku is always 9x9
# you can make mistakes at first and then check at last
# check row and column and check the 3x3 box
# types of value sure & assumed
# learn numpy


# group = the 3x3 grid of nine elements

'''
ALL THE COORDINATES ARE IN (ROW,COLUMN) FORMAT 
'''


class Reader:
    def __init__(self, filename):
        self.filename = filename
        self.unsolved_grid = self.generate_array_from_txt()
        self.array_3d = self.generate_3d_array(self.unsolved_grid)
        self.row_arrays = self.generate_row_arrays(self.array_3d)
        print(self.row_arrays)

    def generate_array_from_txt(self):
        with open(self.filename, "r") as problem:
            sudoku_data = problem.read()
        problem.close()
        unsolved_grid = [[0 for x in range(9)] for y in range(9)]
        row = 0
        column = 0
        for i in sudoku_data:
            if i != "\n":

                if row == 9:
                    row = 0
                    column += 1
                unsolved_grid[column][row] = int(i)
                row += 1

        return unsolved_grid

    def generate_3d_array(self, two_d_grid):
        '''
            generates 9 3x3 groups of sudoku

            returns a 3d grid with 9 grids of nine elements from a 2d grid

            two_d_grid:parameter
        '''
        row_1 = 0
        column_1 = 0
        # for 3d array 3d grid with 9 grids of nine elements from a 2d grid
        array_3d = [[[0 for f in range(3)] for g in range(3)] for h in range(9)]
        for i in range(9):
            three_by_three = [[0 for x in range(3)] for y in range(3)]
            for j in range(9):
                three_by_three[column_1][row_1] = two_d_grid[i][j]
                row_1 += 1
                if row_1 == 3:
                    row_1 = 0
                    column_1 += 1
                    if column_1 == 3:
                        column_1 = 0
            array_3d[i] = three_by_three

        return array_3d

    def generate_row_arrays(self, three_d_grid):
        row_arrays = []
        row_array = []
        count = 0
        for j in range(9):
            for k in range(3):
                for l in range(3):
                    if count > 8:
                        count = 0
                        row_arrays.append(row_array)
                        row_array = []

                    row_array.append(three_d_grid[j][k][l])
                    count += 1

        return row_arrays

    def generate_nine_groups(self):

        array_counter = 0
        row_counter = 0

        nine_groups = []

        for row in self.row_arrays:
            for number in row:


class Analyzer:
    _3x3_mapper = three_by_three_mapper = {"00": 1,
                                           "01": 2,
                                           "02": 3,
                                           "10": 4,
                                           "11": 5,
                                           "12": 6,
                                           "20": 7,
                                           "21": 8,
                                           "22": 9,
                                           }

    def __init__(self, two_d_grid):
        self.two_d_grid = two_d_grid
        self.empty_positions = self.find_empty_positions(self.two_d_grid)

    def find_empty_positions(self, two_d_grid):
        empty_positions = []
        for column in range(9):
            for row in range(9):
                if two_d_grid[column][row] == 0:
                    empty_positions.append([column, row])
        return empty_positions

    def find_the_easiest_boxes_to_fill(self):
        '''Maybe do this later first let this program fill only one box then two box and then 3 and so on'''
        # check number of elements in a row and column
        # check number of elements in a group

        pass

    def get_row_data(self, row_position: int):

        '''
            returns a dictionary
            {
                "row_position" : 4,
                "number_of_non_empty_fields_in_row" : 0,
                "number_of_empty_fields_in_row" : 0,
                "numbers_present_in_row" : [1,2,3,4,5,6],
                "location_of_numbers_present" :{1:[2,4],2:[2,5]},
                "location_of_empty_fields" : [[2, 0], [3, 0], [5, 0], [6, 0], [7, 0], [8, 0]],
                "row_array":[5, 3, 0, 0, 7, 0, 0, 0, 0]
            }
        '''

        number_of_empty_fields_in_row = 0
        numbers_present_in_row = []
        location_of_numbers_present = {}
        location_of_empty_fields_in_row = []

        row = self.two_d_grid[row_position]

        for column in range(9):
            current_position = [row_position, column]
            if row[column] != 0:
                location_of_numbers_present.update({row[column]: current_position})
                numbers_present_in_row.append(row[column])
            else:
                number_of_empty_fields_in_row += 1
                location_of_empty_fields_in_row.append(current_position)

        number_of_non_empty_fields_in_row = 9 - number_of_empty_fields_in_row

        row_data = {
            "row_position": row_position,
            "number_of_non_empty_fields_in_row": number_of_non_empty_fields_in_row,
            "number_of_empty_fields_in_row": number_of_empty_fields_in_row,
            "numbers_present_in_row": numbers_present_in_row,
            "location_of_numbers_present": location_of_numbers_present,
            "location_of_empty_fields_in_row": location_of_empty_fields_in_row,
            "row_array": row
        }

        return row_data

    def get_column_data(self, column_position: int):

        '''
            returns a dictionary
            {
                "column_position" : 4,
                "number_of_non_empty_fields_in_column" : 0,
                "number_of_empty_fields_in_column" : 0,
                "numbers_present_in_column" : [1,2,3,4,5,6],
                "location_of_numbers_present" :{1:[2,4],2:[2,5]},
                "location_of_empty_fields" : [[2, 0], [3, 0], [5, 0], [6, 0], [7, 0], [8, 0]],
                "column_array":[5, 3, 0, 0, 7, 0, 0, 0, 0]
            }
        '''

        number_of_empty_fields_in_column = 0
        numbers_present_in_column = []
        location_of_numbers_present = {}
        location_of_empty_fields_in_column = []

        column = []
        for i in range(9):
            column.append(self.two_d_grid[i][column_position])

        # print(column)

        for row in range(9):
            current_position = [row, column_position]
            if column[row] != 0:
                location_of_numbers_present.update({column[row]: current_position})
                numbers_present_in_column.append(column[row])
            else:
                number_of_empty_fields_in_column += 1
                location_of_empty_fields_in_column.append(current_position)

        number_of_non_empty_fields_in_column = 9 - number_of_empty_fields_in_column

        column_data = {
            "column_position": column_position,
            "number_of_non_empty_fields_in_column": number_of_non_empty_fields_in_column,
            "number_of_empty_fields_in_row": number_of_empty_fields_in_column,
            "numbers_present_in_column": numbers_present_in_column,
            "location_of_numbers_present": location_of_numbers_present,
            "location_of_empty_fields_in_column": location_of_empty_fields_in_column,
            "column_array": column
        }

        return column_data

    def row_and_column_check(self, empty_position):
        possible_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        row_data = self.get_row_data(empty_position[0])
        row_array = row_data["row_array"]

        for number in row_array:
            if number in possible_numbers:
                possible_numbers.remove(number)

        column_data = self.get_column_data(empty_position[1])
        column_array = column_data["column_array"]

        for number in column_array:
            if number in possible_numbers:
                possible_numbers.remove(number)

        print(possible_numbers)
        return possible_numbers

    def check_redundancy_in_groups(self, empty_position, nine_groups_grid, probabilities=None):
        if probabilities is None:
            probabilities = []

        row = empty_position[0]
        column = empty_position[1]

        box_row_position = 0
        box_column_position = 0

        while row > 3:
            row -= 3
            box_row_position += 1

        while column > 3:
            column -= 3
            box_column_position += 1

        print(row, column)
        print(box_row_position, box_column_position)
        mapper = self._3x3_mapper
        box_position = mapper[f"{box_row_position}{box_column_position}"]
        possible_numbers_from_group_check = []

        current_group = nine_groups_grid[box_position]

        for i in current_group:
            if i != 0:
                possible_numbers_from_group_check.append(i)

        if probabilities is not None:
            for i in current_group:
                if i in probabilities:
                    probabilities.remove(i)

    def check_redundancy_in_rows(self):
        pass

    def check_redundancy_in_columns(self):
        pass


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

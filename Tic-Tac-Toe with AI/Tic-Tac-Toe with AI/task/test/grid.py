from hstest import WrongAnswer
from test.minimax import Position
from test.enum import CellState, GameState
from copy import copy


class Grid:
    def __init__(self):
        self.__grid = [[CellState.EMPTY for _ in range(3)] for _ in range(3)]

    def get_grid(self):
        return self.__grid

    @classmethod
    def from_line(cls, line):
        if len(line) != 9:
            raise WrongAnswer("Wrong input length. Expected 9.\nFound " + str(len(line)))

        grid = Grid()

        for i, char in enumerate(line):
            grid.__grid[(int(i / 3))][i % 3] = CellState.get(char)

        return grid

    @classmethod
    def from_output(cls, string_field: str, field_number: int = 1):
        grid = Grid()

        field_lines = list(map(str.strip, string_field.splitlines()))
        field_lines = list(filter(lambda field_line:
                                  str(field_line).startswith('|') and str(field_line).endswith('|'),
                                  field_lines))

        if len(field_lines) < 3 * field_number:
            raise WrongAnswer("Expected not less than " + str(field_number) + " grids in the output!\n" +
                              "Make sure you print the game grids in the correct format!")

        field_lines = field_lines[field_number * 3 - 3:field_number * 3]

        for i, line in enumerate(field_lines):
            if len(line) != 9:
                raise WrongAnswer("Can't parse the game field. The following line has wrong length:\n" + line)
            for j in range(3):
                grid.__grid[i][j] = CellState.get(line[j * 2 + 2])

        return grid

    @classmethod
    def all_grids_from_output(cls, string_field: str):

        grid_list = list()

        field_lines = list(map(str.strip, string_field.splitlines()))
        field_lines = list(filter(lambda field_line:
                                  str(field_line).startswith('|') and str(field_line).endswith('|'),
                                  field_lines))

        if len(field_lines) % 3 != 0:
            raise WrongAnswer(
                "Wrong grid output format! Each grid should contain 3 lines that starts and ends with '|' symbol!")

        for i in range(len(field_lines) // 3):
            grid_lines = field_lines[i * 3:i * 3 + 3]

            grid = Grid()

            for j, line in enumerate(grid_lines):
                if len(line) != 9:
                    raise WrongAnswer("Can't parse the game field. The following line has wrong length:\n" + line)
                for k in range(3):
                    grid.__grid[j][k] = CellState.get(line[k * 2 + 2])

            grid_list.append(grid)

        return grid_list

    @classmethod
    def get_move(cls, from_grid, to_grid):
        for i in range(3):
            for j in range(3):
                if from_grid.__grid[i][j] != to_grid.__grid[i][j]:
                    return Position(i, j)
        raise WrongAnswer("After making a move the grid was the same!")

    def is_win(self, player) -> bool:
        for i in range(3):
            if self.__grid[i][0] == self.__grid[i][1] and self.__grid[i][1] == self.__grid[i][2] and self.__grid[i][
                2] == player:
                return True

        for i in range(3):
            if self.__grid[0][i] == self.__grid[1][i] and self.__grid[1][i] == self.__grid[2][i] and self.__grid[2][
                i] == player:
                return True

        return (self.__grid[0][0] == self.__grid[1][1] and self.__grid[1][1] == self.__grid[2][2] and self.__grid[2][
            2] == player) or (self.__grid[2][0] == self.__grid[1][1] and self.__grid[1][1] == self.__grid[0][2] and
                              self.__grid[0][2] == player)

    def has_empty_cells(self):
        for cells in self.__grid:
            for cell in cells:
                if cell == CellState.EMPTY:
                    return True

    def get_num_of_empty_cells(self):
        result = 0
        for cells in self.__grid:
            for cell in cells:
                if cell == CellState.EMPTY:
                    result += 1
        return result

    def get_game_state(self):
        if self.is_win(CellState.X):
            return GameState.X_WIN
        if self.is_win(CellState.O):
            return GameState.O_WIN
        if self.has_empty_cells():
            return GameState.NOT_FINISHED
        return GameState.DRAW

    def set_cell(self, x, y, cell_state):
        self.__grid[x][y] = cell_state

    def is_correct_next_grid(self, grid):
        return self.get_num_of_empty_cells() - grid.get_num_of_empty_cells() == 1

    def is_valid_grid(self):
        num_of_o = 0
        num_of_x = 0
        for cells in self.__grid:
            for cell in cells:
                if cell == CellState.O:
                    num_of_o += 1
                elif cell == CellState.X:
                    num_of_x += 1
        return abs(num_of_x - num_of_o) <= 1

    @classmethod
    def check_grid_sequence(cls, grids):

        if len(grids) <= 1:
            return

        for i in range(1, len(grids) - 1):
            prev_grid = grids[i - 1]
            grid = grids[i]

            if not grid.is_valid_grid():
                raise WrongAnswer(
                    "Impossible grid was printed! The difference between Os and Xs in the grid is greater than 1:\n" + str(
                        grid))

            if not prev_grid.is_correct_next_grid(grid):
                raise WrongAnswer("After making a move on grid\n" + str(prev_grid) + "\n it can't become\n" + str(grid))

            last_grid = grids[-1]

            if last_grid.get_game_state() == GameState.NOT_FINISHED:
                raise WrongAnswer("Last grid is not terminal!\n" + str(last_grid))

    def __str__(self):
        result = '---------\n'
        for cell in self.__grid:
            result += '| {} {} {} |\n'.format(cell[0].value, cell[1].value, cell[2].value)
        result += '---------'
        return result

    def __eq__(self, other):
        if type(self) != type(other):
            return False

        for i in range(9):
            if self.__grid[int(i / 3)][i % 3] != other.__grid[int(i / 3)][i % 3]:
                return False
        return True

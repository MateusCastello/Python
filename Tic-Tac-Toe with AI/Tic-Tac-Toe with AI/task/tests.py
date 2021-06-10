from copy import copy

from hstest import StageTest, dynamic_test, TestedProgram, CheckResult

from test.enum import GameState, CellState
from test.grid import Grid
from test.minimax import Minimax


class Test:
    def __init__(self, inp, result, state, additional_contains=None):
        self.inp = inp
        self.result = result
        self.state = state
        self.additional_contains = additional_contains


class TicTacToeTests(StageTest):
    easy_ai_moves = [0 for _ in range(9)]

    @dynamic_test(order=1)
    def test_grid_output(self):
        program = TestedProgram()
        output = program.start()

        printed_grid = Grid.from_output(output)
        empty_grid = Grid.from_line("_________")

        if printed_grid != empty_grid:
            return CheckResult.wrong(f"After starting the program you should print an empty grid!\n"
                                     f"Correct empty grid:\n{empty_grid}")

        if "enter the coordinates:" not in output.lower():
            return CheckResult.wrong("After printing an empty grid you should ask to enter cell coordinates!")

        output = program.execute("2 2")

        grid_after_move = Grid.from_output(output)
        correct_grid_after_move = Grid.from_line("____X____")

        if grid_after_move != correct_grid_after_move:
            return CheckResult.wrong(f"After making the move wrong grid was printed.\n"
                                     f"Your grid:\n{grid_after_move}\n"
                                     f"Correct grid:\n{correct_grid_after_move}")

        if "making move level \"easy\"" not in output.lower():
            return CheckResult.wrong("After entering a cell coordinates you should print:\n"
                                     "Making move level \"easy\"")

        grid_after_ai_move = Grid.from_output(output, 2)

        if grid_after_ai_move == grid_after_move:
            return CheckResult.wrong("After AI move grid wasn't changed!")

        game_grid = grid_after_ai_move

        while True:
            game_state = game_grid.get_game_state()
            if game_grid.get_game_state() != GameState.NOT_FINISHED:
                if game_state == GameState.X_WIN and "X wins" not in output:
                    return CheckResult.wrong("You should print 'X wins' if X win the game!")
                if game_state == GameState.O_WIN and "O wins" not in output:
                    return CheckResult.wrong("You should print 'O wins' if O win the game!")
                if game_state == GameState.DRAW and "Draw" not in output:
                    return CheckResult.wrong("You should print 'Draw' if the game ends with draw!")
                break

            next_move = Minimax.get_move(game_grid, CellState.X)
            temp_grid = copy(game_grid)

            temp_grid.set_cell(next_move.x, next_move.y, CellState.X)

            output = program.execute(f"{next_move.x + 1} {next_move.y + 1}")

            game_grid = Grid.from_output(output)

            if game_grid != temp_grid:
                return CheckResult.wrong(f"After making move ({next_move}) the grid is wrong!\n"
                                         f"Your grid:\n{game_grid}\n"
                                         f"Correct grid:\n{temp_grid}")

            if game_grid.get_game_state() != GameState.NOT_FINISHED:
                continue

            game_grid = Grid.from_output(output, 2)

        return CheckResult.correct()

    @dynamic_test(repeat=100, order=2)
    def check_easy_ai(self):

        program = TestedProgram()
        program.start()

        output = program.execute("2 2")

        grid_after_ai_move = Grid.from_output(output, 2)

        cells = grid_after_ai_move.get_grid()

        for i in range(9):
            if i == 4:
                continue

            if cells[int(i / 3)][i % 3] == CellState.O:
                self.easy_ai_moves[i] += 1

        return CheckResult.correct()

    @dynamic_test(order=3)
    def check_random(self):

        average_score = 0

        for i in range(len(self.easy_ai_moves)):
            average_score += (i + 1) * self.easy_ai_moves[i]

        average_score /= 8

        expected_value = (1 + 2 + 3 + 4 + 6 + 7 + 8 + 9) * 100 / 8 / 8

        if abs(average_score - expected_value) > 20:
            return CheckResult.wrong("Looks like your Easy level AI doesn't make a random move!")

        return CheckResult.correct()

    is_easy_not_moving_like_medium = False

    @dynamic_test(repeat=30, order=4)
    def check_easy_not_moving_like_medium(self):

        if self.is_easy_not_moving_like_medium:
            return CheckResult.correct()

        program = TestedProgram()
        program.start()

        program.execute("start user easy")

        output = program.execute("2 2")

        game_grid = Grid.from_output(output, 2)

        cells = game_grid.get_grid()

        if cells[0][0] == CellState.EMPTY and cells[2][2] == CellState.EMPTY:
            output = program.execute("1 1")
            game_grid = Grid.from_output(output, 2)
            if game_grid.get_grid()[2][2] == CellState.EMPTY:
                self.is_easy_not_moving_like_medium = True
        else:
            output = program.execute("1 3")
            game_grid = Grid.from_output(output, 2)
            if game_grid.get_grid()[2][0] == CellState.EMPTY:
                self.is_easy_not_moving_like_medium = True

        program.stop()

        return CheckResult.correct()

    @dynamic_test(order=5)
    def check_easy_not_moving_like_medium_after(self):
        if not self.is_easy_not_moving_like_medium:
            return CheckResult.wrong("Looks like your Easy level AI doesn't make a random move!")
        return CheckResult.correct()


if __name__ == '__main__':
    TicTacToeTests().run_tests()

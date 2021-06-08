from hstest import CheckResult, StageTest, dynamic_test, TestedProgram

from test.grid import Grid


class Test:
    def __init__(self, inp, result, state, additional_contains=None):
        self.inp = inp
        self.result = result
        self.state = state
        self.additional_contains = additional_contains


class TicTacToeTests(StageTest):
    test_cases = [
        Test("_XXOO_OX_\n1 1", "XXXOO_OX_", "X wins"),
        Test("_XXOO_OX_\n1 3\n1 1", "XXXOO_OX_", "X wins", "This cell is occupied! Choose another one!"),
        Test("_XXOO_OX_\n1 4\n1 1", "XXXOO_OX_", "X wins", "Coordinates should be from 1 to 3!"),
        Test("_XXOO_OX_\none\n1 1", "XXXOO_OX_", "X wins", "You should enter numbers!"),
        Test("_XXOO_OX_\none three\n1 1", "XXXOO_OX_", "X wins", "You should enter numbers!"),
        Test("_XXOO_OX_\n2 3", "_XXOOXOX_", "Game not finished"),
        Test("_XXOO_OX_\n3 3", "_XXOO_OXX", "Game not finished"),
        Test("XX_XOXOO_\n1 3", "XXOXOXOO_", "O wins"),
        Test("XX_XOXOO_\n3 3", "XX_XOXOOO", "O wins"),
        Test("_XO_OX___\n1 1", "XXO_OX___", "Game not finished"),
        Test("_XO_OX___\n2 1", "_XOXOX___", "Game not finished"),
        Test("_XO_OX___\n3 1", "_XO_OXX__", "Game not finished"),
        Test("_XO_OX___\n3 2", "_XO_OX_X_", "Game not finished"),
        Test("_XO_OX___\n3 3", "_XO_OX__X", "Game not finished"),
        Test("_XO_OX__X\n1 1", "OXO_OX__X", "Game not finished"),
        Test("_XO_OX__X\n2 1", "_XOOOX__X", "Game not finished"),
        Test("_XO_OX__X\n3 1", "_XO_OXO_X", "O wins"),
        Test("_XO_OX__X\n3 2", "_XO_OX_OX", "Game not finished"),
        Test("XO_OXOX__\n1 3", "XOXOXOX__", "X wins"),
        Test("XO_OXOX__\n3 2", "XO_OXOXX_", "Game not finished"),
        Test("XO_OXOX__\n3 3", "XO_OXOX_X", "X wins"),
    ]

    @dynamic_test(data=test_cases)
    def test_grid_output(self, test):
        program = TestedProgram()
        program.start()

        output = program.execute(test.inp)

        grid = Grid.from_line(test.inp.split('\n')[0])
        output_grid = Grid.from_output(output)

        if grid != output_grid:
            return CheckResult.wrong("The printed grid is not equal to the input grid!\n"
                                     "Correct grid:\n\n" + str(grid))

        if test.additional_contains is not None and test.additional_contains not in output:
            return CheckResult.wrong("'{}' expected in the output!".format(test.additional_contains))

        result_grid = Grid.from_output(output, 2)
        correct_result_grid = Grid.from_line(test.result)

        if result_grid != correct_result_grid:
            return CheckResult.wrong(
                f"The printed result grid is not correct!\nCorrect result grid:\n\n {correct_result_grid}")

        if test.state not in output:
            return CheckResult.wrong(f"The game result is wrong. Expected result '{test.state}'")

        return CheckResult.correct()


if __name__ == '__main__':
    TicTacToeTests().run_tests()

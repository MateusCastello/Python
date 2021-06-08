from test.enum import GameState, CellState


class Position:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return str(self.x) + " " + str(self.y)

    def __eq__(self, other):
        return other.x == self.x and other.y == self.y


class Minimax:

    @classmethod
    def minimax(cls, grid, player, is_maximize, start_player, depth):

        game_state = grid.get_game_state()

        if game_state == GameState.X_WIN:
            return 10 - depth if start_player == CellState.X else depth - 10
        elif game_state == GameState.O_WIN:
            return 10 - depth if start_player == CellState.O else depth - 10
        elif game_state == GameState.DRAW:
            return 0

        best_score = -999 if is_maximize else 999

        for i in range(3):
            for j in range(3):
                if grid.get_grid()[i][j] == CellState.EMPTY:
                    grid.set_cell(i, j, player)
                    score = cls.minimax(grid, CellState.get_opponent(player), not is_maximize, start_player, depth + 1)
                    grid.set_cell(i, j, CellState.EMPTY)
                    best_score = max(best_score, score) if is_maximize else min(best_score, score)

        return best_score

    @classmethod
    def get_move(cls, grid, player):
        best_score = -999
        best_position = None

        for i in range(3):
            for j in range(3):
                if grid.get_grid()[i][j] == CellState.EMPTY:
                    grid.set_cell(i, j, player)
                    score = cls.minimax(grid, CellState.get_opponent(player), False, player, 1)
                    grid.set_cell(i, j, CellState.EMPTY)
                    if score > best_score:
                        best_score = score
                        best_position = Position(i, j)

        return best_position

    @classmethod
    def get_available_positions(cls, grid, player):

        positions = list()

        for i in range(3):
            for j in range(3):
                if grid.get_grid()[i][j] == CellState.EMPTY:
                    grid.set_cell(i, j, player)
                    score = cls.minimax(grid, CellState.get_opponent(player), False, player, 1)
                    if score >= 0:
                        positions.append(Position(i, j))
                    grid.set_cell(i, j, CellState.EMPTY)

        return positions

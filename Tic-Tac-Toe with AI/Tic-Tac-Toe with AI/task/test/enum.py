from enum import Enum
from hstest import WrongAnswer


class GameState(Enum):
    X_WIN = 'X_WIN'
    O_WIN = 'O_WIN'
    DRAW = 'DRAW'
    NOT_FINISHED = 'NOT_FINISHED'


class CellState(Enum):
    X = 'X'
    O = 'O'
    EMPTY = ' '

    @classmethod
    def get(cls, char: str):

        char_to_cell_state = {
            'X': cls.X,
            'O': cls.O,
            ' ': cls.EMPTY,
            '_': cls.EMPTY
        }

        if char not in char_to_cell_state:
            raise WrongAnswer('Bad symbol ' + char + ' in the game grid')
        return char_to_cell_state[char]

    @classmethod
    def get_opponent(cls, player):
        if player == CellState.X:
            return CellState.O
        if player == CellState.O:
            return CellState.X
        raise Exception('Wrong method argument!')

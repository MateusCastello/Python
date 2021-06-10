import random


def get_valid_moves(table):
    valid_moves = []
    for i in range(3):
        for j in range(3):
            if table[i][j] == " ":
                valid_moves.append((i, j))
    return valid_moves


def random_move(table, moves):
    move = random.choice(moves)
    table[move[0]][move[1]] = "O"

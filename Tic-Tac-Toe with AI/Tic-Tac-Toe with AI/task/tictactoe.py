from winner import winner
import computer_logic

table = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
count = 0
x_number = 0
o_number = 0
game_over = False


def print_table(table):
    print("---------")
    for i in range(3):
        print("| " + " ".join(table[i]) + " |")
    print("---------")


print_table(table)


while not game_over:
    if x_number > o_number:
        print('Making move level "easy"')
        moves = computer_logic.get_valid_moves(table)
        computer_logic.random_move(table, moves)
        o_number += 1

    else:
        coords = input("Enter the coordinates: ")

        if not coords[0].isdigit():
            print("You should enter numbers!")
            continue
        else:
            line, row = coords.split()

        line = int(line)
        row = int(row)

        if line < 1 or line > 3 or row < 1 or row > 3:
            print("Coordinates should be from 1 to 3!")
            continue
    
        if table[line-1][row-1] != " ":
            print("This cell is occupied! Choose another one!")
            continue
        else:
            table[line - 1][row - 1] = "X"
            x_number += 1

    if winner(table) == 1:
        print_table(table)
        print("X wins")
        game_over = True
    elif winner(table) == 2:
        print_table(table)
        print("O wins")
        game_over = True
    elif o_number + x_number == 9:
        print_table(table)
        print("Draw")
        game_over = True
    else:
        print_table(table)
        print("Game not finished")
    



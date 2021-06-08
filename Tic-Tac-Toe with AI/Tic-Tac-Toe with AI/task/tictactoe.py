from winner import winner
first_table = input("Enter the cells: > ")
first_table = first_table.replace("_", " ")
x_number = 0
o_number = 0

for item in first_table:
    if item == "X":
        x_number += 1
    elif item == "O":
        o_number += 1
table = [[], [], []]
count = 0
game_over = False


def print_table(table):
    print("---------")
    for i in range(3):
        print("| " + " ".join(table[i]) + " |")
    print("---------")


for i in range(3):
    for j in range(3):
        table[i].append(first_table[count])
        count += 1

print_table(table)


while not game_over:
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
        if x_number > o_number:
            table[line - 1][row - 1] = "O"
            o_number += 1
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
    



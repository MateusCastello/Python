def winner(table):
    # Lines
    if table[0] == ["X", "X", "X"]:
        return 1
    elif table[1] == ["X", "X", "X"]:
        return 1
    elif table[2] == ["X", "X", "X"]:
        return 1
    elif table[0] == ["O", "O", "O"]:
        return 2
    elif table[1] == ["O", "O", "O"]:
        return 2
    elif table[2] == ["O", "O", "O"]:
        return 2
    # Columns
    elif table[0][0] == "X" and table[1][0] == "X" and table[2][0] == "X":
        return 1
    elif table[0][1] == "X" and table[1][1] == "X" and table[2][1] == "X":
        return 1
    elif table[0][2] == "X" and table[1][2] == "X" and table[2][2] == "X":
        return 1
    elif table[0][0] == "O" and table[1][0] == "O" and table[2][0] == "O":
        return 2
    elif table[0][1] == "O" and table[1][1] == "O" and table[2][1] == "O":
        return 2
    elif table[0][2] == "O" and table[1][2] == "O" and table[2][2] == "O":
        return 2

    # Diagonals
    elif table[0][2] == "X" and table[1][1] == "X" and table[2][0] == "X":
        return 1
    elif table[0][0] == "X" and table[1][1] == "X" and table[2][2] == "X":
        return 1
    elif table[0][2] == "O" and table[1][1] == "O" and table[2][0] == "O":
        return 2
    elif table[0][0] == "O" and table[1][1] == "O" and table[2][2] == "O":
        return 2

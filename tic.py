#!/usr/bin/python3

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True, row[0]

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True, board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True, board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True, board[0][2]

    return False, None

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    moves = 0
    while True:
        print_board(board)
        # Input validation
        while True:
            try:
                row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
                col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
                if row not in range(3) or col not in range(3):
                    print("Coordinates must be 0, 1, or 2. Try again.")
                elif board[row][col] != " ":
                    print("That spot is already taken! Try again.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter numbers only.")

        board[row][col] = player
        moves += 1

        winner, who = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {who} wins!")
            break
        elif moves == 9:
            print_board(board)
            print("It's a tie!")
            break

        player = "O" if player == "X" else "X"

# Le bloc principal est **obligatoire pour que le script fonctionne** lorsqu’on l’exécute
if __name__ == "__main__":
    tic_tac_toe()


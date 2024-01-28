import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def get_move(player, board):
    if player == 'X':
        while True:
            try:
                row = int(input(f"Player {player}, enter row (0, 1, or 2): "))
                col = int(input(f"Player {player}, enter column (0, 1, or 2): "))
                if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == ' ':
                    return row, col
                else:
                    print("Invalid input. Row and column must be between 0 and 2 and the cell must be empty.")
            except ValueError:
                print("Invalid input. Please enter integers for row and column.")
    else:  # Computer's move
        row, col = random.choice([(i, j) for i in range(3) for j in range(3) if board[i][j] == ' '])
        print(f"Computer chooses row {row} and column {col}")
        return row, col

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    current_player = 0

    while True:
        print_board(board)
        player = players[current_player]
        print(f"Player {player}'s turn.")
        row, col = get_move(player, board)

        if board[row][col] == ' ':
            board[row][col] = player

            if check_winner(board, player):
                print_board(board)
                if player == 'X':
                    print("You win!")
                else:
                    print("Computer wins!")
                return
            elif is_board_full(board):
                print_board(board)
                print("It's a tie!")
                return
            else:
                current_player = (current_player + 1) % 2
        else:
            print("Cell already occupied. Try again.")

def tic_tac_toe():
    while True:
        play_game()
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            break

if __name__ == "__main__":
    tic_tac_toe()


board = ["_", "_", "_",
         "_", "_", "_",
         "_", "_", "_"]

def display_board(): #display Tic Tac Toe board
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])

# If game is still going
game_still_going = True
# Who won? or tie?
winner = None
# Whose turn is it
current_player = "X"

def play_game():
    #display board game
    display_board()

    while game_still_going:
        handle_turn(current_player)
        check_if_game_over()
        flip_player()
    # The game has ended
    if winner == "X" or winner == "O":
        print(f"{winner} won!")
    elif winner == None:
        print("Tie.")

def handle_turn(player):

    print(player + "'s turn")
    position = input("Choose a position from 1-9: ")

    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        position = input("Invalid input. Choose a position from 1-9: ")

    position = int(position) - 1

    board[position] = player
    display_board()


def check_if_game_over():
    check_for_winner()
    # check_if_tie()

def check_for_winner():
    #set up global variables inside of the function
    global winner
    # check rows
    row_winner = check_rows()
    # check columns
    column_winner = check_columns()
    # check diagonals
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    return


# def check_if_tie():
#     global game_still_going
#
#     if "-" not in board:
#         game_still_going = False
#         return


def check_rows():
    #set up global variables
    global game_still_going
    #check if any of the rows have the same value and is not empty
    row_1 = board[0] == board[1] == board[2] != "_"
    row_2 = board[3] == board[4] == board[5] != "_"
    row_3 = board[6] == board[7] == board[8] != "_"
    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


def check_columns():
    # set up global variables
    global game_still_going
    # check if any of the columns have the same value and is not empty
    column_1 = board[0] == board[3] == board[6] != "_"
    column_2 = board[1] == board[4] == board[7] != "_"
    column_3 = board[2] == board[5] == board[8] != "_"
    if column_1 or column_2 or column_3:
        game_still_going = False
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return


def check_diagonals():
    # set up global variables
    global game_still_going
    # check if any of the diagonal have the same value and is not empty
    diagonal_1 = board[0] == board[4] == board[8] != "_"
    diagonal_2 = board[6] == board[4] == board[2] != "_"

    if diagonal_1 or diagonal_2:
        game_still_going = False
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[6]
    return


def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return


# player_input(player) #get input position from the player
# check_win() #check winner of the game
# play()

play_game()
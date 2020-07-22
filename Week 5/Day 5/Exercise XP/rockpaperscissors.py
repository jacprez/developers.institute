# class RockPaperScissors():
#
#     def evaluate_play(self, player_1_move, player_2_move):
#         if player_1_move == player_2_move:
#             return "draw"
#
#         if player_1_move == "R":
#             if player_2_move == "P":
#                 return "Player 2"
#             if player_2_move == "S":
#                 return "Player 1"
#


import random

def win():
    print("THE GAME: You win.")

def lost():
    print("THE GAME: You lost.")

def draw():
    print("THE GAME: It's a draw.")

def the_game():

    moves = ['rock', 'paper', 'scissors']
    print('THE GAME: rock, paper, scissors')
    attempts = 3
    while True:
        if attempts == 0:
            print('THE GAME: You failed to provide the correct option. Goodbye.')

            break
        player = str(input('Player: ').lower())
        if player.lower() not in moves:
            print(f"THE GAME: Invalid Option! You have {attempts} attempts left.")
            attempts -= 1

        else:
            computer = random.choice(moves)
            print(f"Computer: {computer}")

            if player == computer:
                draw()
            elif player == 'rock' and computer == 'scissors':
                win()
            elif player == 'rock' and computer == 'paper':
                lost()
            elif player == 'paper' and computer == 'rock':
                win()
            elif player == 'paper' and computer == 'scissors':
                lost()
            elif player == 'scissors' and computer == 'rock':
                lost()
            elif player == 'scissors' and computer == 'paper':
                win()
            else:
                pass

            play_again = str(input('THE GAME: Retry? (y/n): '))
            if play_again.lower() == 'y':
                the_game()
            elif play_again.lower() == 'n':
                print('THE GAME: Game over. Goodbye.')

            else:
                print('THE GAME: Invalid input. Goodbye.')

                break


if __name__=='__main__':
    the_game()
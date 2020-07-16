class RockPaperScissors():

    def evaluate_play(self, player_1_move, player_2_move):
        if player_1_move == player_2_move:
            return "draw"

        if player_1_move == "R":
            if player_2_move == "P":
                return "Player 2"
            if player_2_move == "S":
                return "Player 1"

        if
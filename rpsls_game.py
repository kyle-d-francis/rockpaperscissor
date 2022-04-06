from human import Human
from ai import Ai
from player import Player


class RLPSLS_Game:
    def __init__(self):
        self.player_one = Human
        self.player_two = ''

    def run_game(self):
        self.welcome_message()
        self.battle_phase()
        self.display_winner()

    def welcome_message(self):
        print('Welcome to Rock, Paper, Scissors, Lizard, Spock!')
        user_input = input('How many players? 1 or 2: ')
         

    def battle_phase(self):
        while player_one.score < 2 and player_two.score < 2:
            player_one.chosen_gesture
            player_two.chosen_gesture
            self.compare_gesture
            if player_one.score == 2 or player_two.score == 2:
                break 
                

    def display_winner(self):
        if player_one.score == 2:
            print('Player one is the winner!')
        else:
            player_two.score == 2
            print('Player two is the winner')

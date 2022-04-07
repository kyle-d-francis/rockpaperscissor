from human import Human
from ai import Ai



class RLPSLS_Game:
    def __init__(self):
        self.player_one = Human()
        self.player_two = ''

    def run_game(self):
        self.welcome_message()
        self.battle_phase()
        self.display_winner()

    def welcome_message(self):
        print('Welcome to Rock, Paper, Scissors, Lizard, Spock!')
        user_input = input('How many players? 1 or 2: ')
        if user_input == '2':
            self.player_two = Human()
        elif user_input == '1':
            self.player_two= Ai()
            return user_input


    def battle_phase(self):
        player_one = self.player_one
        player_two = self.player_two
        while player_one.score < 2 and player_two.score < 2:
            player_one.chose_gesture()
            player_two.chose_gesture()
            player_one.compare_gesture(player_one, player_two)
            if player_one.score == 2 or player_two.score == 2:
                break 
                

    def display_winner(self):
        player_one = self.player_one
        player_two = self.player_two
        if player_one.score == 2:
            print('Player one is the winner!')
        else:
            player_two.score == 2
            print('Player two is the winner')

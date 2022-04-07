from human import Human
from ai import Ai



class RLPSLS_Game:
    def __init__(self):
        self.player_one = Human()
        self.player_two = ''

    def run_game(self):
        self.display_welcome_message()
        self.determine_number_of_players()
        self.run_battle_phase()
        self.display_winner()

    def determine_number_of_players(self):
        user_input = input('How many players? 1 or 2: ')
        if user_input == '2':
            self.player_two = Human()
        elif user_input == '1':
            self.player_two= Ai()
            return user_input

    def display_welcome_message(self):
        print('Welcome to Rock, Paper, Scissors, Lizard, Spock!')
        

    def run_battle_phase(self):
        player_one = self.player_one
        player_two = self.player_two
        while player_one.score < 2 and player_two.score < 2:
            player_one.chose_gesture()
            player_two.chose_gesture()
            self.compare_gesture(player_one, player_two)
            if player_one.score == 2 or player_two.score == 2:
                break 
                
    def compare_gesture(self, player_one, player_two):
            if player_one.chosen_gesture == player_two.chosen_gesture:
                print('Its a tie!') 
            elif player_one.chosen_gesture == 'rock' and (player_two.chosen_gesture == 'scissors' or player_two.chosen_gesture == 'lizard'):
                player_one.score += 1
            elif player_two.chosen_gesture == 'rock' and (player_one.chosen_gesture == 'scissors' or player_one.chosen_gesture == 'lizard'):
                player_two.score += 1
            elif player_one.chosen_gesture == 'spock' and (player_two.chosen_gesture == 'rock' or player_two.chosen_gesture == 'scissors'):
                player_one.score += 1
            elif player_two.chosen_gesture == 'spock' and (player_one.chosen_gesture == 'rock' or player_one.chosen_gesture == 'scissors'):
                player_two.score += 1
            elif player_one.chosen_gesture == 'scissors' and (player_two.chosen_gesture == 'paper' or player_two.chosen_gesture == 'lizard'):
                player_one.score += 1
            elif player_two.chosen_gesture == 'scissors' and (player_one.chosen_gesture == 'paper' or player_one.chosen_gesture == 'lizard'):
                player_two.score += 1
            elif player_one.chosen_gesture == 'paper' and (player_two.chosen_gesture == 'rock' or player_two.chosen_gesture == 'spock'):
                player_one.score += 1
            elif player_two.chosen_gesture == 'paper' and (player_one.chosen_gesture == 'rock' or player_one.chosen_gesture == 'spock'):
                player_two.score += 1
            elif player_one.chosen_gesture == 'lizard' and (player_two.chosen_gesture == 'spock' or player_two.chosen_gesture == 'paper'):
                player_one.score += 1
            elif player_two.chosen_gesture == 'lizard' and (player_one.chosen_gesture == 'spock' or player_one.chosen_gesture == 'paper'):
                player_two.score += 1
            print(f'Player 1 score: {player_one.score}') 
            print(f'Player 2 score: {player_two.score}')

    def display_winner(self):
        player_one = self.player_one
        player_two = self.player_two
        if player_one.score == 2:
            print('Player one is the winner!')
        else:
            player_two.score == 2
            print('Player two is the winner')

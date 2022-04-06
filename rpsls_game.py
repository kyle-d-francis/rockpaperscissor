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
            if player_one.chosen_gesture == 'rock' and player_two.chosen_gesture == "scissors" or "lizard":
                player_one.score+= 1
            elif player_two.chosen_gesture == 'rock' and player_one.chosen_gesture == 'scissors'or 'lizard':
                player_two.score+=1
            elif player_one.chosen_gesture == 'spock' and player_two.chosen_gesture == 'rock' or 'scissors':
                player_one.score+=1
            elif player_two.chosen_gesture == 'spock' and player_one.chosen_gesture == 'rock' or 'scissor':
                player_two.score+=1
            elif player_one.chosen_gesture == 'scissors' and player_two.chosen_gesture == 'paper' or 'lizard':
                player_one.score +=1
            elif player_two.chosen_gesture == 'scissor' and player_one.chosen_gesture == 'paper' or 'lizard':
                player_two.score += 1
            elif player_one.chosen_gesture == 'paper' and player_two.chosen_gesture == 'rock'or 'spock':
                player_one.score +=1
            elif player_two.chosen_gesture == 'paper' and player_two.chosen_gesture == 'rock' or 'spock':
                player_two.score+=1
            elif player_one.chosen_gesture == 'lizard' and player_two.chosen_gesture == 'spock' or 'paper':
                player_one.score+=1
            elif player_two.chosen.gesture = 'lizard' and player_one.chosen_gesture == 'spock' or 'paper':
                player_two.score+=1
            if player_one.score == 2 or player_two.score == 2:
                break 
                

    def display_winner(self):
        if player_one.score == 2:
            print('Player one is the winner!')
        else:
            player_two.score == 2
            print('Player two is the winner')

from unicodedata import name


class Player:
    def __init__(self):
        self.name = ''
        self.score = 0  
        self.list_of_possible_gestures = ['rock', 'paper', 'scissors', 'lizard', 'spock']
        self.chosen_gesture = ''

    def chose_gesture(self):
        user_input = input('What move will you like to play?')
        self.chosen_gesture = user_input
        return user_input

    def compare_gesture(self, player_one, player_two):
            if player_one.chosen_gesture == 'rock'and player_two.chosen_gesture == 'rock':
                print('its a tie')
            elif player_one.chosen_gesture == 'spock' and player_two.chosen_gesture =='spock':
                print('its a tie')
            elif player_one.chosen_gesture == 'lizard' and player_two.chosen_gesture =='lizard':
                print('its a tie')
            elif player_one.chosen_gesture == 'scissors' and player_two.chosen_gesture =='scissors':
                print('its a tie')
            elif player_one.chosen_gesture == 'paper' and player_two.chosen_gesture =='paper':
                print('its a tie')    
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

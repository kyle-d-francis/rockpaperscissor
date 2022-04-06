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

    def compare_gesture(self):
    
        pass 
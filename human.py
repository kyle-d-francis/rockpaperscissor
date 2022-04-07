from player import Player

class Human(Player):
    def __init__(self):
        self.name = ''
        self.chosen_gesture = ''
        super().__init__()
    
    def chose_gesture(self):
        user_input = input('What move will you like to play?')
        self.chosen_gesture = user_input
        return user_input
        
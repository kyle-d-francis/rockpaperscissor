from player import Player

class Human(Player):
    def __init__(self):
        self.chosen_gesture = ''
        super().__init__()
    


    def chose_gesture(self):
        user_input = input('What move will you like to play?')
        self.chosen_gesture = user_input
        while user_input not in self.list_of_possible_gestures:
            user_input = input('Try again. What move will you like?')
            self.chosen_gesture = user_input
            if self.chosen_gesture in self.list_of_possible_gestures:
                break     
        return self.chosen_gesture


    
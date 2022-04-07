from player import Player

class Human(Player):
    def __init__(self):
        self.chosen_gesture = ''
        super().__init__()
    


    def chose_gesture(self):
        user_input = input('What move will you like to play?')
        while self.chosen_gesture in self.list_of_possible_gestures == False:
            input('Try again. What move will you like?')
            if self.chosen_gesture in self.list_of_possible_gestures == True:
                break
        self.chosen_gesture = user_input
            
        return self.chosen_gesture
    
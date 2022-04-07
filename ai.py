from player import Player
import random
class Ai(Player):
    def __init__(self):
        self.name = ''
        self.chosen_gesture = ''
        super().__init__()
        pass

    def chose_gesture(self):
        self.chosen_gesture = random.choice(self.list_of_possible_gestures)
        print(f'Ai move is {self.chosen_gesture}')
        return self.chosen_gesture
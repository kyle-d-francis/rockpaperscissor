from player import Player
import random
class Ai(Player):
    def __init__(self):
        self.chosen_gesture = random.choice(self.list_of_possible_gestures)
        super().__init__()
        pass

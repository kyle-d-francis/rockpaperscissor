from player import Player
import random
class Ai(Player):
    def __init__(self):
        self.chosen_gesture = ''
        super().__init__()
        pass

    def chose_gesture(self):
        self.chosen_gesture = random.choice(['spock','rock','paper','scissors','lizard'])
        print(self.chosen_gesture)
        return self.chosen_gesture
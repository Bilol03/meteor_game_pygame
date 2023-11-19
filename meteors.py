from gameObject import GameObject
import random
DISPLAY_WIDTH = 600
DISPLAY_HEIGHT = 400
INITIAL_METEOR_Y_LOATION = 0
INITIAL_NUMBER_OF_METEORS = 8
MAX_METEOR_SPEED = 7

class Meteors(GameObject):
    def __init__(self, game):
        self.game = game
        self.x = random.randint(0, DISPLAY_WIDTH-100)
        self.y = INITIAL_METEOR_Y_LOATION
        self.speed = random.randint(1, MAX_METEOR_SPEED)
        self.load_image('start-down.png')
        
    def move_down(self):
        self.y = self.y + self.speed
        if self.y > DISPLAY_HEIGHT:
            self.y = 5
    def __str__(self) -> str:
        return f"Meteor ({str(self.x)}, {str(self.y)})"
    
from gameObject import GameObject

DISPLAY_WIDTH = 600
DISPLAY_HEIGHT = 400
STARSHIP_SPEED = 20

class Starship(GameObject):
    def __init__(self, game):
        self.game = game
        self.x = DISPLAY_WIDTH / 2 - 30
        self.y = DISPLAY_HEIGHT - 70
        self.load_image('start-up.png')
    def move_right(self):
        self.x = self.x + STARSHIP_SPEED
        if self.x + self.width > DISPLAY_WIDTH:
            self.x = DISPLAY_WIDTH - self.width
    def move_left(self):
        self.x = self.x - STARSHIP_SPEED
        if self.x < 0:
            self.x = 0
    def move_up(self):
        self.y = self.y - STARSHIP_SPEED
        if self.y < 0:
            self.y = 0
    def move_down(self):
        self.y = self.y + STARSHIP_SPEED
        if self.y + self.width > DISPLAY_WIDTH:
            self.y = DISPLAY_WIDTH - self.width
    def __str__(self):
        return f'Starship ({str(self.x)}, {str(self.y)})'
  
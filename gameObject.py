import starship 
import pygame

class GameObject:
    def __init__(self):
        self.starship = starship.Starship(self)
    
    def load_image(self, filename):
        self.image = pygame.image.load(filename).convert()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        
    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
    
    def draw(self):
        self.game.display_surface.blit(self.image, (self.x, self.y))

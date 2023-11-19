import pygame
import random
import starship
import  meteors

FRAME_REFRESH_RATE = 30
DISPLAY_WIDTH = 600
DISPLAY_HEIGHT = 400
STARSHIP_SPEED = 20
INITIAL_METEOR_Y_LOATION = 0
INITIAL_NUMBER_OF_METEORS = 8
MAX_METEOR_SPEED = 7
NUMBER_OF_MAX_CYCLES = 1000

class Game:
    def __init__(self, level):
        print('initializing game....')
        if level == 'easy':
            INITIAL_NUMBER_OF_METEORS = 7
            meteors.MAX_METEOR_SPEED = 8
            
        elif level == 'medium':
            INITIAL_NUMBER_OF_METEORS = 10
            meteors.MAX_METEOR_SPEED = 10
            
            
        elif level == 'hard':
            INITIAL_NUMBER_OF_METEORS = 13
            meteors.MAX_METEOR_SPEED = 13

            
        pygame.init()
        self.display_surface = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
        pygame.display.set_caption("Starship Meteors")
        self.clock = pygame.time.Clock()
        self.starship = starship.Starship(self)
        self.level = level
        

               
        self.meteors = [meteors.Meteors(self) for _ in range(0, INITIAL_NUMBER_OF_METEORS)]
            
    def play(self):
        is_running  = True
        cycle_count = 0
        starship_collided = False
        while is_running and not starship_collided:
            cycle_count += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.starship.move_right()
                    elif event.key == pygame.K_LEFT:
                        self.starship.move_left()
                    elif event.key == pygame.K_UP:
                        self.starship.move_up()
                    elif event.key == pygame.K_DOWN:
                        self.starship.move_down()
                    elif event.key == pygame.K_q:
                        is_running == False
                    elif event.type == pygame.K_p:
                        self.pause()
            self.display_surface.fill((0,0,0))
            self.starship.draw()
            for meteor in self.meteors:
                meteor.draw()
            for meteor in self.meteors:
                meteor.move_down()

            if self.check_collison():
                starship_collided = True
            if cycle_count == NUMBER_OF_MAX_CYCLES:
                print('Winner...!')
                break
            elif starship_collided and cycle_count < NUMBER_OF_MAX_CYCLES:
                print("You lose...")
                print(cycle_count)
                break
            pygame.display.update()
            
            self.clock.tick(FRAME_REFRESH_RATE)
            
        pygame.quit()
        
    def check_collison(self):
        result = False
        for meteor in self.meteors:
            if self.starship.rect().colliderect(meteor.rect()):
                result = True
                break
        return result
    # def pa
 

    
            
def main(level):
    print('Starting game...')
    game = Game(level=level)
    game.play()
        
        

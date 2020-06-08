import pygame
from engine.behaviour import Behaviour

class Jetpack(Behaviour):
    def __init__(self):
        super().__init__()
        self.name = "Jetpack"

        self.thrust = 3
        
    def update(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            self.game_object.get_behaviour("Rigidbody").add_force( (0, self.thrust) )
    
    def render(self):
        pass

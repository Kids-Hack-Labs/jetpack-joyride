import pygame
from engine.behaviour import Behaviour

class Jetpack(Behaviour):
    def __init__(self):
        super().__init__()
        self.name = "Jetpack"

        self.thrust = 3
        
    def update(self):        
        
        keys = pygame.key.get_pressed()
        
        rb = self.game_object.get_behaviour("Rigidbody")
        if keys[pygame.K_SPACE]:
            rb.add_force( (0, self.thrust) )

        # flying
        if keys[pygame.K_SPACE]:
            self.game_object.get_behaviour("Animator").play(1)
        # falling
        else:
            self.game_object.get_behaviour("Animator").play(0)
        
    def render(self):
        pass

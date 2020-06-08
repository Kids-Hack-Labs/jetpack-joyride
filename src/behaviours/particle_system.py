import pygame
from engine.behaviour import Behaviour

class Particle:
    def __init__(self):
        self.lifetime = 1000

    def update(self):
        self.lifetime -= 1

class ParticleSystem(Behaviour):
    def __init__(self):
        super().__init__()
        self.name = "ParticleSystem"

        self.target_surface = pygame.display.get_surface()

        self.active_particles = []

    def update(self):
        pass

    def render(self):

        # could make all particles their own object?
        pass

        

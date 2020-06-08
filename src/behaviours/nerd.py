import pygame
from engine.behaviour import Behaviour

class Nerd(Behaviour):
    def __init__(self):
        super().__init__()
        self.name = "Nerd"

        self.target = None
        self.sight_threshold = 1000

        self.is_scared = False
        
    def update(self):
        self.is_scared = self.game_object.get_behaviour("Transform").position.distance_to(self.target.position) < self.sight_threshold

        if self.is_scared:
            self.game_object.get_behaviour("SpriteRenderer").colour = (255, 0, 0)
    
    def render(self):
        pass

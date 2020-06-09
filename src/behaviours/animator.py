import pygame
from engine.behaviour import Behaviour

from src.animation import Animation

class Animator(Behaviour):
    def __init__(self):
        super().__init__()
        self.name = "Animator"

        self.animation = Animation("./assets/running/")
        self.frame = 0

        self.time_counter = 0
        self.last_time = pygame.time.get_ticks()

    # might want to make a global delta time
    def update(self):
        current_time = pygame.time.get_ticks()
        delta_time = (current_time - self.last_time) / 1000
        self.last_time = current_time

        print(self.time_counter)
        
        self.game_object.get_behaviour("SpriteRenderer").sprite = self.animation.get_frame(self.frame)

        if self.time_counter > self.animation.fps:
            self.time_counter = 0
            self.frame += 1
            
            if self.frame > self.animation.frame_count - 1:
                self.frame = 0
        self.time_counter += delta_time
        
    def render(self):
        pass
 

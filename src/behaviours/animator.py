import pygame
from engine.behaviour import Behaviour

from src.animation import Animation

class Animator(Behaviour):
    def __init__(self):
        super().__init__()
        self.name = "Animator"

        self.animations = []
        self.frame = 0

        self.time_counter = 0
        self.last_time = pygame.time.get_ticks()

    # might want to make a global delta time
    def update(self):

        # calculate time since last frame
        current_time = pygame.time.get_ticks()
        delta_time = (current_time - self.last_time) / 1000
        self.last_time = current_time

        # change the shown sprite to the current frame
        # might want to only change if the animation was updated
        self.game_object.get_behaviour("SpriteRenderer").sprite = self.animations[0].get_frame(self.frame)

        # check if a certain amount of time has passed
        if self.time_counter > self.animations[0].fps:
            self.time_counter = 0
            self.frame += 1
            
            if self.frame > self.animations[0].frame_count - 1:
                self.frame = 0
        self.time_counter += delta_time
        
    def render(self):
        pass
 

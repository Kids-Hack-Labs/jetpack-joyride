import pygame
from engine.behaviour import Behaviour

from pygame.math import Vector2

class Rigidbody(Behaviour):
    GRAVITY = (0, -0.8)
    
    def __init__(self):
        super().__init__()
        self.name = "Rigidbody"

        self.mass = 1
        self.drag = 1

        # terminal velocity?
        self.velocity = Vector2()
        self.angular_velocity = 0

        self.experience_gravity = True

    # add_force expects a tuple as the force
    def add_force(self, force):
        # force = mass * acceleration
        # acceleration = force / mass
        # velocity += acceleration
        self.velocity += Vector2(force[0] / self.mass, force[1] / self.mass)
    
    def update(self):

        # apply gravity
        if self.experience_gravity:
            self.add_force(Rigidbody.GRAVITY)

        # apply drag
        self.velocity = Vector2(self.velocity.x * 1 / self.drag, self.velocity.y * 1 / self.drag)

        # i chose to flip the y velocity only when we need to apply a motion, this way all\
        # calculation is done using a proper cartesian plane
        inverted_velocity = Vector2(self.velocity.x, -self.velocity.y)
        # at the end of each frame, apply the calculated motion
        self.game_object.get_behaviour("Transform").position += inverted_velocity
    
    def render(self):
        pass

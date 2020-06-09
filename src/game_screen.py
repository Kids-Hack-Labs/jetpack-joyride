import pygame
#other imports go here

from engine.screen import Screen

from engine.game_object import GameObject
from src.behaviours.sprite_renderer import SpriteRenderer
from src.behaviours.animator import Animator
from src.animation import Animation
from src.behaviours.rigidbody import Rigidbody
from src.behaviours.jetpack import Jetpack
from src.behaviours.particle_system import ParticleSystem

# npcs
from src.behaviours.nerd import Nerd

class GameScreen(Screen):
    def __init__(self):
        super().__init__()
        self.bg_colour = (255, 255, 255)
        
    def start(self):

        player = GameObject()
        player.name = "Player" # this is the player gameobject

        transform = player.get_behaviour("Transform")
        transform.position.x = 100
        transform.position.y = 500

        # add a renderer to the player object so that we can see it
        renderer = SpriteRenderer()
        renderer.resize( (50, 100) ) # resize the renderer behaviour
        renderer.center = True # make the renderer center the sprite
        player.add_behaviour(renderer)

        animator = Animator()

        run_animation = Animation("./assets/running/")
        animator.animations.append(run_animation)

        player.add_behaviour(animator)

        rigidbody = Rigidbody()
        rigidbody.experience_gravity = True
        player.add_behaviour(rigidbody)

        jetpack = Jetpack()
        player.add_behaviour(jetpack)

        jetpack_particles = ParticleSystem()
        player.add_behaviour(jetpack_particles)
        
        self.add_game_object(player)

        scientist = GameObject()

        scientist.add_behaviour(SpriteRenderer())
        scientist.add_behaviour(Nerd()) # chose to call this behaviour nerd for fun
        scientist.get_behaviour("Nerd").target = transform
        
        self.add_game_object(scientist)
        
        
        super().start()

    def update(self):
        super().update()
        
    def render(self):
        screen = pygame.display.get_surface()
        screen.fill(self.bg_colour)
        
        super().render()

    def add_game_object(self, game_object):
        super().add_game_object(game_object)

    def remove_game_object(self, game_object):
        super().remove_game_object(game_object)

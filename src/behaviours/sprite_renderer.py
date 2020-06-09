import pygame
from engine.behaviour import Behaviour

class SpriteRenderer(Behaviour):
    def __init__(self):
        super().__init__()
        self.name = "SpriteRenderer"
        self.colour = (255, 0, 0)
        
        self.width = 10
        self.height = 10

        self.center = False

        self.sprite = None
        self.surf = pygame.Surface((self.width, self.height))

    def resize(self, dimensions):
        self.width = dimensions[0]
        self.height = dimensions[1]
        self.surf = pygame.Surface((self.width, self.height))
    
    def update(self):
        pass
    
    def render(self):
        screen = pygame.display.get_surface()
        t = self.game_object.get_behaviour("Transform")

        offsetX = 0
        offsetY = 0

        if self.center:
            offsetX = self.width / 2
            offsetY = self.height / 2
        #screen.blit(self.surf,(t.position.x - offsetX, t.position.y - offsetY), self.colour)

        if self.sprite != None:
            screen.blit(self.sprite,(t.position.x - offsetX, t.position.y - offsetY))

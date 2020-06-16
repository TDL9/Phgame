import pygame
from pygame.locals import *

from .. import GameObj

class Widget(GameObj.GameObj):
    ''' screen space rect, has a surface to draw
    '''
    def __init__(self, rect = None, engine = None):
        GameObj.GameObj.__init__(self, engine = engine)
        self.rect = rect
        if self.rect:
            self.surface = pygame.surface.Surface(self.rect.size)
        else:
            self.surface = None
        self.update_policy = None
        self.visible = True
        self.subobj = []
    
    def update(self):
        if self.update_policy:
            self.rect = self.update_policy[0](self.update_policy[1:])
            self.surface = pygame.surface.Surface(self.rect.size)
        else:
            print("Warning : update widget with no update policy")
        return self

    def draw_to(self, surf):
        surf.blit(self.surface, self.rect)
    
    def render(self):
        self.surface.fill((0, 0, 0))
        for obj in subobj:
            obj.draw_to(self.surfaces)
        
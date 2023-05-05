import pygame
from Interface import *
from Colors import *


class Mask(pygame.sprite.Sprite, Interface):

    def __init__(self, dims, position, color=Colors.BLACK, opacity=100):
        super().__init__()

        self.dims = dims
        self.position = position

        self.image = pygame.Surface(dims)
        self.image.fill(color)
        self.image.set_alpha(opacity)

        self.rect = pygame.Rect(dims, position)

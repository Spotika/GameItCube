import pygame
import Config
from Sprites.ImageLabel import ImageLabel
from Sprites.TextLabel import TextLabel


class HeadUpDisplay(pygame.sprite.Sprite):

    def __init__(self, dims, position):
        super().__init__()
        self.rect = pygame.Rect(position, dims)
        self.image = pygame.Surface(self.rect)
        self.label = Config.HUD_LAYER

    def update(self):
        ...

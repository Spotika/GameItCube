import pygame
from Interface import *
from Screen import *
import Config


class BackGroundSprite(pygame.sprite.Sprite, Interface):

    def __init__(self, texture_path):
        super().__init__()
        self.width = Screen.width
        self.height = Screen.height
        self.texture_path = texture_path
        self._layer = Config.BACK_GROUND_SPRITE_LAYER

        self.image = pygame.transform.scale(pygame.image.load(self.texture_path),
                                            (self.width, self.height))
        self.rect = self.image.get_rect()

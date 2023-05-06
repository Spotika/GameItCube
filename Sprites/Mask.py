import pygame
from Interface import Interface
from Colors import Colors
import Config


class Mask(Interface, pygame.sprite.Sprite):
    """Накладывает прозрачную маску цвета"""

    def __init__(self, position=(0, 0), dims=(0, 0), color=Colors.BLACK, opacity=140, layer=Config.MASK_LAYER,
                 **kwargs):
        self.width, self.height = dims
        self.position = position
        super().__init__(**kwargs)

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(color)
        self.image.set_alpha(opacity)
        self.image.convert_alpha()

        self.rect = pygame.Rect(self.position, (self.width, self.height))

        self._layer = layer


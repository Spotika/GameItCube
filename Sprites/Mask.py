import pygame
from Interface import Interface
from Colors import Colors
import Config


class Mask(pygame.sprite.Sprite, Interface):
    """Накладывает прозрачную маску цвета"""

    def __init__(self, dims, position=(0, 0), color=Colors.BLACK, opacity=140, layer=Config.MASK_LAYER):
        super().__init__()

        self.dims = dims
        self.position = position

        self.image = pygame.Surface(dims)
        self.image.fill(color)
        self.image.set_alpha(opacity)
        self.image.convert_alpha()

        self.rect = pygame.Rect(position, dims)

        self._layer = layer

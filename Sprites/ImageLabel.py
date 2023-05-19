import pygame
from Interface import Interface
from Colors import Colors
import Config
from Label import Label


class ImageLabel(Label):
    """Накладывает прозрачную маску цвета"""
    texture_path = None

    def __init__(self, position, dims=(0, 0), color=Colors.WHITE, opacity=255, texture_path=None,
                 layer=Config.MASK_LAYER):
        super().__init__(position, dims, layer)

        if texture_path is None and self.texture_path is None:
            self.get_image().fill(color)
        elif texture_path is None:
            self.set_image(pygame.transform.scale(pygame.image.load(self.texture_path),
                                                  self.dims))
        else:
            self.set_image(pygame.transform.scale(pygame.image.load(texture_path),
                                                  self.dims))
        self.get_image().set_alpha(opacity)
        self.get_image().convert_alpha()

        self.set_rect(pygame.Rect(self.position, self.dims))

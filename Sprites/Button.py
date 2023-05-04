from Interface import *
import pygame
import Config


class Button(pygame.sprite.Sprite, Interface):

    def __init__(self, dims, position, on_click, texture_path, layer=Config.BUTTON_SPRITE_LAYER):
        super().__init__()
        self._layer = layer
        self.width, self.height = dims
        self.position = position
        self.on_click = on_click
        self.texture_path = texture_path

        self.image = pygame.image.load(self.texture_path)
        self.image = pygame.transform.scale(self.image, dims)
        self.rect = pygame.Rect(*position, *dims)

        self.group_function = self.event_update



    def event_update(self, *args, **kwargs):
        ...



from Interface import *
import pygame
import Config
from EventHandler import *


class Button(Interface, pygame.sprite.Sprite):

    def __init__(self, position, dims, on_click=lambda: None, texture_path=Config.SOLID_WHITE_TEXTURE,
                 layer=Config.BUTTON_SPRITE_LAYER, **kwargs):
        self._layer = layer
        self.width, self.height = dims
        self.position = position
        self.on_click = on_click
        self.texture_path = texture_path

        super().__init__(**kwargs)

        self.image = pygame.image.load(self.texture_path)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = pygame.Rect(*self.position, self.width, self.height)

        self.group_function = self.event_update

    def event_update(self):
        """Проверка на нажатие и хитбокс"""
        for event in EventHandler.get_events():

            if event.type == pygame.MOUSEBUTTONDOWN:
                if EventHandler.get_mouse_pressed()[0]:
                    if self.rect.collidepoint(*EventHandler.get_mouse_pos()):
                        self.on_click()  # вызов целевой функции

    def set_on_click(self, function):
        self.on_click = function

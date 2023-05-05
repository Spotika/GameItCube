import pygame
from Interface import *
from Screen import *
import Config
from EventHandler import *


# FIXME
class BackGroundSprite(pygame.sprite.Sprite, Interface):

    def __init__(self, texture_path):
        super().__init__()
        self.width = Screen.width
        self.height = Screen.height
        self.texture_path = texture_path

        self._layer = Config.BACK_GROUND_SPRITE_LAYER

        self.image = pygame.transform.scale(pygame.image.load(self.texture_path),
                                            (self.width, self.height)).convert_alpha()
        self.rect = self.image.get_rect()


class BackGroundParallaxSprite(pygame.sprite.Sprite, Interface):

    def __init__(self, layers, speed_begin=1, speed_difference=0.8):
        super().__init__()
        self.width = Screen.width
        self.height = Screen.height

        self.firstLayerSpeed = speed_begin
        self.speedDiff = speed_difference

        self.renderedLayers = []
        self.layersCoordinates = [0] * len(layers)

        # инициализация пустыми поверхностями размером с экран
        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect()

        self.load_layers(layers)

        self._layer = Config.BACK_GROUND_SPRITE_LAYER

    def set_image(self):
        self.image = pygame.Surface((self.width, self.height))
        for i in range(len(self.renderedLayers) - 1, 0, -1):
            self.image.blit(self.renderedLayers[i], (self.layersCoordinates[i], 0))
            self.image.blit(self.renderedLayers[i], (self.layersCoordinates[i] - self.width, 0))
        self.image.convert_alpha()

    def load_layers(self, layers: list[str]):
        """render the layers to renderedLayers"""

        for layer in layers:
            renderedLayer = pygame.transform.scale(pygame.image.load(layer),
                                                   (self.width, self.height)).convert_alpha()
            self.renderedLayers.append(renderedLayer)

    def update(self):
        for i in range(len(self.renderedLayers)):
            self.layersCoordinates[i] -= self.firstLayerSpeed * (self.speedDiff ** i) * EventHandler.get_dt() / 1000
            self.layersCoordinates[i] = self.layersCoordinates[i] % self.width

        self.set_image()

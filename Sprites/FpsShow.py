import pygame
from EventHandler import EventHandler


class FpsShow(pygame.sprite.Sprite):
    def __init__(self, dims, position, initColor=(100, 255, 100), initFont=(None, 50)):
        self.width, self.height = dims
        self.position = position
        self.fps = EventHandler.get_fps()
        self.image = pygame.Surface((0, 0))
        self.rect = pygame.Rect(self.position, (self.width, self.height))
        self.initFont = initFont
        self.initColor = initColor

        super().__init__()

    def update(self):
        font = pygame.font.Font(*self.initFont)
        self.image = font.render(f"{round(self.fps)}", True, self.initColor)
        self.fps = EventHandler.get_fps()

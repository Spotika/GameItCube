import pygame
from Colors import Colors


class TextLabel(pygame.sprite.Sprite):

    def __init__(self, dims, position, color=Colors.WHITE, font=(None, 50)):
        super().__init__()
        self.dims = dims
        self.position = position
        self.image = pygame.Surface(dims)
        self.rect = pygame.Rect(position, dims)
        self.font = pygame.font.Font(*font)
        self.color = color

    def write(self, text) -> None:
        self.image = self.font.render(text, True, self.color)
        self.image = pygame.transform.scale(self.image, self.dims)


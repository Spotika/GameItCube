import pygame
from Colors import Colors
from Label import Label


class TextLabel(Label):

    def __init__(self, position, dims, color=Colors.WHITE, font=(None, 50), layer=50):
        super().__init__(position, dims, layer)
        self.font = pygame.font.SysFont(*font)
        self.color = color

    def write(self, text):
        text = self.font.render(str(text), True, self.color)
        transform = True
        self.set_image(text, transform=transform)
        return self

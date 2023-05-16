import pygame
from EventHandler import EventHandler
from Sprites.TextLabel import TextLabel


class FpsShow(TextLabel):

    def update(self):
        self.write(str(EventHandler.get_fps()))

import pygame
from App import *
from Screen import *
from EventHandler import *


class MainMenu(App):

    @classmethod
    def begin(cls):
        while cls.running:
            EventHandler.update()  # events update

            # Screen.render()

    @classmethod
    def end(cls):
        cls.running = False

import pygame
from App import App
from Designs.MainGameDesign import MainGameDesign
from EventHandler import EventHandler


class MainGameApp(App, MainGameDesign):
    """Сама игра"""

    @classmethod
    def loop(cls):

        cls.link_to_all_sprites()

        while cls.running:
            EventHandler.tick()

            EventHandler.update()

            cls.render()

        cls.end()

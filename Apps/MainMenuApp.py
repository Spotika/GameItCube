import pygame
from App import App
from Screen import Screen
from EventHandler import EventHandler
from Sprites.BackGrounds import BackGroundParallaxSprite
import Config
from Sprites.Button import Button
from Group import Group
from Sprites.Mask import Mask
from Designs.MainMenuDesign import MainMenuDesign


class MainMenuApp(App, MainMenuDesign):
    """
    Должен быть атрибут allSprites: pygame.sprite.LayeredUpdates

    """

    @classmethod
    def loop(cls):

        cls.link_to_all_sprites()

        while cls.running:
            """main loop of app"""

            EventHandler.tick()  # clock update

            EventHandler.update()  # events update

            cls.check_events()  # local events check

            cls.render()  # app update

    @classmethod
    def check_events(cls):
        for event in EventHandler.get_events():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    cls.end()


App.link(MainMenuApp)

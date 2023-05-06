import pygame
from App import App
from Screen import Screen
from EventHandler import EventHandler
from Sprites.BackGrounds import BackGroundParallaxSprite
import Config
from Sprites.Button import Button
from Group import Group
from Sprites.Label import Label
from Designs.MainMenuDesign import MainMenuDesign


class MainMenuApp(App, MainMenuDesign):
    """Главное меню"""

    """Ниже события кнопок"""
    @classmethod
    def exit_button(cls):
        """Выход из игры"""
        cls.end()

    @classmethod
    def enter_button(cls):
        ...

    @classmethod
    def loop(cls, *args, **kwargs):

        cls.link_function_to_button("exitButton", cls.exit_button)

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
                    cls.redirect("MainGameApp")

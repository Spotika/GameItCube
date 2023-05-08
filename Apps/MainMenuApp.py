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
import webbrowser


class MainMenuApp(App, MainMenuDesign):
    """Главное меню"""

    """Ниже события кнопок"""

    @classmethod
    def exit_button(cls):
        """Выход из игры"""
        cls.end()

    @classmethod
    def enter_button(cls):
        cls.redirect("MainGameApp")
        cls.end()

    @classmethod
    def git_button(cls):
        """редирект на страницу гита проекта"""
        webbrowser.open('https://github.com/Spotika/GameItCube', new=2)

    @classmethod
    def loop(cls, *args, **kwargs):

        cls.init_textures()

        cls.link_function_to_button("exitButton", cls.exit_button)
        cls.link_function_to_button("enterButton", cls.enter_button)
        cls.link_function_to_button("gitInfoButton", cls.git_button)

        cls.init_sprites_and_groups()

        while cls.running:
            """main loop of app"""

            EventHandler.tick()  # clock update

            EventHandler.update(cls)  # events and groups update

            cls.render()  # app update

            cls.check_events()  # local events check

    @classmethod
    def check_events(cls):
        for event in EventHandler.get_events():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    cls.end()

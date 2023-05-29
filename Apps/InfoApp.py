import pygame
from App import App
from Screen import Screen
from EventHandler import EventHandler
from Designs.InfoDesign import InfoDesign


class InfoApp(App, InfoDesign):
    """Экран окончания игры"""

    @classmethod
    def back_button(cls):
        """Выход из экрана"""
        cls.end()

    @classmethod
    def loop(cls, *args, **kwargs):

        cls.init_textures()

        cls.link_function_to_button("backButton", cls.back_button)

        cls.init_sprites_and_groups()

        while cls.running:
            """main loop of app"""

            EventHandler.tick()  # clock update

            EventHandler.update(cls)  # events and groups update

            cls.render()

            cls.check_events()  # local events check

    @classmethod
    def check_events(cls):
        for event in EventHandler.get_events():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    cls.back_button()

import pygame
from App import App
from Designs.MainGameDesign import MainGameDesign
from EventHandler import EventHandler
from QueryDeque import QueryDeque


class MainGameApp(App, MainGameDesign):
    """Сама игра"""

    @classmethod
    def loop(cls, *args, **kwargs):
        cls.init_textures()
        cls.init_sprites_and_groups()

        # FIXME cls.ELEMENTS["platform"].set_all_sprites(cls.allSprites) - костыль для платформ

        while cls.running:
            EventHandler.tick()

            EventHandler.update(cls)

            cls.check_events()

            cls.render()

        cls.end()

    @classmethod
    def check_events(cls):
        for event in EventHandler.get_events():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    cls.redirect("MainMenuApp")
                    cls.end()

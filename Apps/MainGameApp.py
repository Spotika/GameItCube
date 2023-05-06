import pygame
from App import App
from Designs.MainGameDesign import MainGameDesign
from EventHandler import EventHandler


class MainGameApp(App, MainGameDesign):
    """Сама игра"""

    @classmethod
    def loop(cls, *args, **kwargs):
        cls.link_to_all_sprites()

        cls.ELEMENTS["platform"].set_all_sprites(cls.allSprites)

        while cls.running:
            EventHandler.tick()

            EventHandler.update()

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

import pygame
from App import App
from Designs.MainGameDesign import MainGameDesign
from EventHandler import EventHandler
from QueryDeque import QueryDeque
from Sprites.Platform import PlatformGenerator
from Players.NinjaPlayer import NinjaPlayer


class MainGameApp(App, MainGameDesign):
    """Сама игра"""

    @classmethod
    def loop(cls, *args, **kwargs):
        cls.init_textures()
        cls.init_sprites_and_groups()

        cls.platformGenerator = PlatformGenerator(cls.allSprites)

        # привязка класса к игроку
        cls.get_element("player").set_app(cls)
        cls.get_element("player").add_to_collision_env_functions(
            cls.get_element("HUD").collision_function
        )

        cls.get_element("HUD").get_design("healthLabel").add_player(cls.get_element("player"))
        cls.get_element("HUD").get_design("manaLabel").add_player(cls.get_element("player"))

        while cls.running:
            EventHandler.tick()

            EventHandler.update(cls)

            cls.platformGenerator.update()

            cls.check_events()

            cls.render()

        cls.end()

    @classmethod
    def check_events(cls):
        for event in EventHandler.get_events():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    cls.redirect("MainMenuApp")
                    cls.end()

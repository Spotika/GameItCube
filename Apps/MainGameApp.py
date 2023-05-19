import pygame
from App import App
from Designs.MainGameDesign import MainGameDesign
from EventHandler import EventHandler
from QueryDeque import QueryDeque
from Sprites.Platform import PlatformGenerator
from Players.NinjaPlayer import NinjaPlayer
from Screen import Screen


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

        player = cls.get_element("player")

        # подключение трекеров
        cls.get_element("HUD").get_design("healthTracker").add_state(player.get_health)
        cls.get_element("HUD").get_design("manaTracker").add_state(player.get_mana)
        cls.get_element("HUD").get_design("strengthTracker").add_state(player.get_strength)
        cls.get_element("HUD").get_design("dexterityTracker").add_state(player.get_dexterity)
        cls.get_element("HUD").get_design("intelligenceTracker").add_state(player.get_intelligence)
        cls.get_element("HUD").get_design("moneyTracker").add_state(player.get_money)
        cls.get_element("HUD").get_design("levelTracker").add_state(player.get_level)
        cls.get_element("HUD").get_design("experienceTracker").add_state(
            lambda: f"{player.experience}/{player.experience_for_next}")

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
                    cls.redirect("PauseApp", use_deque=False, penis=Screen.display)

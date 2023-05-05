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
    Должен быть атрибут all_sprites: pygame.sprite.LayeredUpdates

    """
    @classmethod
    def loop(cls):

        backGround = BackGroundParallaxSprite(Config.BackGroundTextures.BACKGROUND_FOREST_LAYERS,
                            speed_begin=50,
                            speed_difference=0.8
                            )
        cls.allSprites.add(backGround)


        # colorMask = Mask((Screen.width, Screen.height))
        # cls.allSprites.add(colorMask)


        while cls.running:
            """main loop of app"""

            EventHandler.tick() # clock update

            EventHandler.update() # events update

            cls.check_events() # local events check

            cls.render()  # app update

    @classmethod
    def check_events(cls):
        for event in EventHandler.get_events():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    cls.end()

App.link(MainMenuApp)

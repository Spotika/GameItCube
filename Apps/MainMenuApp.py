import pygame
from App import *
from Screen import *
from EventHandler import *
from Sprites.BackGroundSprite import *
from Apps.SecondTestApp import *
import Config


class MainMenuApp(App):
    allSprites = pygame.sprite.LayeredUpdates()
    """контейнер для спрайтов"""

    @classmethod
    def begin(cls):
        cls.allSprites.add(BackGroundSprite(Config.BACK_GROUND_IMG_FILE_PATH))  # Back ground image


        while cls.running:
            """main loop of app"""
            EventHandler.update()  # events update

            cls.check_events()

            cls.update()  # app update


    @classmethod
    def check_events(cls):
        for event in EventHandler.get_events():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    cls.end()

    @classmethod
    def end(cls):
        cls.running = False
        Screen.display.fill((0, 0, 0))
        pygame.display.update()
        # redirecting to Second App
        SecondTestApp.begin()

    @classmethod
    def update(cls):
        Screen.display.fill((0, 0, 0))
        cls.allSprites.draw(Screen.display)
        pygame.display.update()

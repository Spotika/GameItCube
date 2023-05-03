import pygame
from App import *
from Screen import *
from EventHandler import *
from Sprites.BackGroundSprite import *
import Config


class SecondTestApp(App):
    allSprites = pygame.sprite.LayeredUpdates()
    """контейнер для спрайтов"""

    @classmethod
    def begin(cls):
        cls.allSprites.add(BackGroundSprite("media/img/BackGround2.jpg"))  # Background image

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


    @classmethod
    def update(cls):
        cls.allSprites.draw(Screen.display)
        pygame.display.update()

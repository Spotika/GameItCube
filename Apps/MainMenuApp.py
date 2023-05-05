import pygame
from App import *
from Screen import *
from EventHandler import *
from Sprites.BackGroundSprite import *
import Config
from Sprites.Button import *
from Group import *
from Sprites.Mask import *


class MainMenuApp(App):


    @classmethod
    def redirect_button(cls):
        cls.end()


    @classmethod
    def begin(cls):
        cls.running = True


        cls.allSprites = pygame.sprite.LayeredUpdates()
        """контейнер для спрайтов"""


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

    @classmethod
    def end(cls):
        cls.running = False
        pygame.display.update()
        Screen.display.fill((0, 0, 0))


    @classmethod
    def render(cls):
        Screen.display.fill((0, 0, 0))
        cls.allSprites.update()
        cls.allSprites.draw(Screen.display)
        pygame.display.update()

App.link(MainMenuApp)

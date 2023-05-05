import pygame
from App import *
from Screen import *
from EventHandler import *
from Sprites.BackGroundSprite import *
import Config
from Sprites.Button import *
from Group import *


class MainMenuApp(App):


    @classmethod
    def redirect_button(cls):
        cls.end()


    @classmethod
    def begin(cls):
        cls.running = True
        clock = pygame.time.Clock()
        """Часы программы"""

        cls.allSprites = pygame.sprite.LayeredUpdates()
        """контейнер для спрайтов"""


        backGround = BackGroundParallaxSprite(Config.BackGroundTextures.BACKGROUND_FOREST_LAYERS,
                            speed_begin=1.4,
                            speed_difference=0.8
                            )
        cls.allSprites.add(backGround)

        # cls.allSprites.add(pygame.Surface((Screen.width, Screen.height)).fill((0, 0, 0).set_alpha(50)))
        #
        #
        # cls.buttonGroup = Group()
        # cls.buttonGroup.add(Button((100, 100), (100, 100), lambda: print(123), Config.START_BUTTON_IMG_FILE_PATH))
        # cls.buttonGroup.link_to_sprites(cls.allSprites)

        while cls.running:
            """main loop of app"""

            clock.tick(Config.FPS) # clock tick
            print(clock.get_fps())

            EventHandler.update()  # events update

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

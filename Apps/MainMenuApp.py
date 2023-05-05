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
        cls.allSprites = pygame.sprite.LayeredUpdates()
        """контейнер для спрайтов"""


        backGround = BackGroundParallaxSprite(Config.BackGroundTextures.BACKGROUND_FOREST_LAYERS) # Back ground image
        cls.allSprites.add(backGround)
        # cls.buttonGroup = Group()
        # cls.buttonGroup.add(Button((200, 100), (100, 100), cls.redirect_button, Config.START_BUTTON_IMG_FILE_PATH))

        # cls.buttonGroup.link_to_sprites(cls.allSprites)

        while cls.running:
            """main loop of app"""
            clock.tick(Config.FPS)
            EventHandler.update()  # events update

            cls.allSprites.update()

            cls.check_events()

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
        cls.allSprites.draw(Screen.display)
        pygame.display.update()

App.link(MainMenuApp)
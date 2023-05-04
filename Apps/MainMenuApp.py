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
    def begin(cls):
        cls.running = True
        cls.allSprites = pygame.sprite.LayeredUpdates()
        """контейнер для спрайтов"""


        cls.allSprites.add(BackGroundSprite(Config.BACK_GROUND_IMG_FILE_PATH))  # Back ground image

        cls.buttonGroup = Group()
        cls.buttonGroup.add(Button((200, 100), (100, 100), lambda x: None, Config.START_BUTTON_IMG_FILE_PATH))
        cls.buttonGroup.add(Button((200, 100), (300, 200), lambda x: None, Config.START_BUTTON_IMG_FILE_PATH))
        cls.buttonGroup.add(Button((200, 100), (500, 300), lambda x: None, Config.START_BUTTON_IMG_FILE_PATH))

        cls.buttonGroup.link_to_sprites(cls.allSprites)

        while cls.running:
            """main loop of app"""
            EventHandler.update()  # events update

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
        Screen.display.fill((0, 0, 0))
        pygame.display.update()


    @classmethod
    def render(cls):
        Screen.display.fill((0, 0, 0))
        cls.allSprites.draw(Screen.display)
        pygame.display.update()

App.link(MainMenuApp)
import pygame
from Colors import Colors
from Design import Design
from Sprites.BackGrounds import BackGroundParallaxSprite
import Config
from Sprites.Button import Button
from Sprites.ImageLabel import ImageLabel
from Screen import Screen
from Group import Group


class PauseDesign(Design):

    @classmethod
    def init_textures(cls):
        cls.set_groups({
            "ButtonGroup": Group()
        })

        cls.set_elements({
            "blackoutLabel": ImageLabel((0, 0), (Screen.width, Screen.height), opacity=200,
                                        color=Colors.BLACK, layer=0),
            "enterButton": Button((576, 253), (450, 111), group=cls.get_group("ButtonGroup"),
                                  texture_path=Config.ButtonTextures.START_BUTTON_IMG_FILE_PATH),
            "exitButton": Button((576, 436), (450, 111), group=cls.get_group("ButtonGroup"),
                                 texture_path=Config.ButtonTextures.EXIT_BUTTON_IMG_FILE_PATH),
        })

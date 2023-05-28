import pygame
from Colors import Colors
from Design import Design
import Config
from Sprites.Button import Button
from Sprites.ImageLabel import ImageLabel
from Screen import Screen
from Group import Group
from Sprites.TextLabel import TextLabel


class EndDesign(Design):

    @classmethod
    def init_textures(cls):
        cls.set_groups({
            "ButtonGroup": Group()
        })

        cls.set_elements({
            "blackoutLabel": ImageLabel((0, 0), (Screen.width, Screen.height), opacity=200,
                                        color=Colors.BLACK, layer=0),
            "exitButton": Button((576, 550), (450, 111), group=cls.get_group("ButtonGroup"),
                                 texture_path=Config.ButtonTextures.EXIT_BUTTON_IMG_FILE_PATH),
            "textLabel1": TextLabel((576, 100), (450, 100)).write("Вы проиграли!"),
            "textLabel2": TextLabel((576, 200), (450, 100)).write("Ваш счет"),
            "imageLabel": ImageLabel((680 + 40, 380), (55, 27 * 2), texture_path=Config.MONEY_IMAGE_PATH),
            "textLabel3": TextLabel((750 + 40, 390), (55, 22 * 2)),
        })

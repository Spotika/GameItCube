import pygame
from Colors import Colors
from Design import Design
import Config
from Sprites.Button import Button
from Sprites.ImageLabel import ImageLabel
from Screen import Screen
from Group import Group
from Sprites.TextLabel import TextLabel


class InfoDesign(Design):

    @classmethod
    def init_textures(cls):
        cls.set_groups({
            "ButtonGroup": Group()
        })
        cls.set_elements({
            "backButton": Button((50, 66), (34 * 3, 22 * 3), group=cls.get_group("ButtonGroup"),
                                 texture_path=Config.ButtonTextures.BACK_BUTTON_FILE_PATH, layer=1000),
            "image": ImageLabel((0, 0), (Screen.width, Screen.height), texture_path=Config.INFO_IMAGE,
                                color_key=(0, 0, 0)),
        })


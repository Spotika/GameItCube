import pygame

import Config
from Design import Design

from Group import Group
from Sprites.Button import Button


class PauseDesign(Design):
    @classmethod
    def init_textures(cls):
        cls.set_groups({
            "ButtonGroup": Group()
        })

        cls.set_elements({
            "settingsButton": Button((655, 158), (34 * 3, 22 * 3), group=cls.get_group("ButtonGroup"),
                                     texture_path=Config.ButtonTextures.SETTINGS_BUTTON_IMG_FILE_PATH),
            "backButton": Button((655, 287), (34 * 3, 22 * 3), group=cls.get_group("ButtonGroup"),
                                 texture_path=Config.ButtonTextures.SETTINGS_BUTTON_IMG_FILE_PATH),
            "exitButton": Button((655, 400), (34 * 3, 22 * 3), group=cls.get_group("ButtonGroup"),
                                     texture_path=Config.ButtonTextures.SETTINGS_BUTTON_IMG_FILE_PATH)
        })
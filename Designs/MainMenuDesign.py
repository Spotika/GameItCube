import pygame
from Colors import Colors
from Design import Design
from Sprites.BackGrounds import BackGroundParallaxSprite
import Config
from Sprites.Button import Button
from Sprites.ImageLabel import ImageLabel
from Screen import Screen
from Group import Group


class MainMenuDesign(Design):

    @classmethod
    def init_textures(cls):
        cls.set_groups({
            "ButtonGroup": Group()
        })

        cls.set_elements({
            "backGround": BackGroundParallaxSprite(Config.BackGroundTextures.BACKGROUND_FOREST_LAYERS,
                                                   speed_begin=75,
                                                   speed_difference=0.8
                                                   ),

            "blackoutLabel": ImageLabel((30, 30), (Config.DESIGN_WIDTH - 60, Config.DESIGN_HEIGHT - 60), opacity=140,
                                        color=Colors.BLACK),
            "settingsButton": Button((50, 66), (34 * 3, 22 * 3), group=cls.get_group("ButtonGroup"),
                                     texture_path=Config.ButtonTextures.SETTINGS_BUTTON_IMG_FILE_PATH),
            "enterButton": Button((576, 253), (450, 111), group=cls.get_group("ButtonGroup"),
                                  texture_path=Config.ButtonTextures.START_BUTTON_IMG_FILE_PATH),
            "exitButton": Button((576, 436), (450, 111), group=cls.get_group("ButtonGroup"),
                                 texture_path=Config.ButtonTextures.EXIT_BUTTON_IMG_FILE_PATH),

            "infoLabel": ImageLabel((50, 708), (220, 32)),
            "playerLabel": ImageLabel((1159, 234), (331, 331)),
            "gameLabel": ImageLabel((489, 66), (623, 92), texture_path=Config.GAME_LOGO),
            "gitInfoButton": Button((96, 234), (331, 331), group=cls.get_group("ButtonGroup"),
                                    texture_path=Config.ButtonTextures.GIT_BUTTON),
        })

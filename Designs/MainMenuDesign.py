import pygame
from Colors import Colors
from Design import Design
from Sprites.BackGrounds import BackGroundParallaxSprite
import Config
from Sprites.Button import Button
from Sprites.Label import Label
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

            "blackoutLabel": Label((30, 30), (Config.DESIGN_WIDTH - 60, Config.DESIGN_HEIGHT - 60), opacity=140,
                                   color=Colors.BLACK),
            "settingsButton": Button((50, 66), (92, 92), group=cls.get_group("ButtonGroup")),
            "enterButton": Button((576, 253), (450, 111), group=cls.get_group("ButtonGroup")),
            "exitButton": Button((665, 436), (260, 67), group=cls.get_group("ButtonGroup")),

            "infoLabel": Label((50, 708), (220, 32)),
            "playerLabel": Label((1159, 234), (331, 331)),
            "gameLabel": Label((489, 66), (623, 92)),
            "gitInfoLabel": Label((96, 234), (331, 331)),

        })


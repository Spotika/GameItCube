import pygame

from Design import Design
from Sprites.BackGrounds import BackGroundParallaxSprite
import Config
from Sprites.Button import Button
from Sprites.Mask import Mask
from Screen import Screen
from Group import Group


class MainMenuDesign(Design):
    GROUPS = {
        "ButtonGroup": Group()
    }

    ELEMENTS = {
        "backGround": BackGroundParallaxSprite(Config.BackGroundTextures.BACKGROUND_FOREST_LAYERS,
                                               speed_begin=75,
                                               speed_difference=0.8
                                               ),

        "blackout": Mask((30, 30), (Config.DESIGN_WIDTH - 60, Config.DESIGN_HEIGHT - 60)),
        "SettingsButton": Button((50, 66), (92, 92), group=GROUPS["ButtonGroup"]),
    }

    @classmethod
    def link_function_to_button(cls, button_name, function):
        cls.ELEMENTS[button_name].set_on_click(function)

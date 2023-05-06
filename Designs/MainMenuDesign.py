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
        "BackGround": BackGroundParallaxSprite(Config.BackGroundTextures.BACKGROUND_FOREST_LAYERS,
                                               speed_begin=50,
                                               speed_difference=0.8
                                               ),
        "Mask": Mask((30, 30), (Config.DESIGN_WIDTH - 60, Config.DESIGN_HEIGHT - 60)),
        # "Button": Button((0, 0), (100, 100), group=GROUPS["ButtonGroup"]),
    }
    a = ELEMENTS["Mask"]

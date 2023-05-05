import pygame

from Design import Design
from Sprites.BackGrounds import BackGroundParallaxSprite
import Config
from Sprites.Button import Button
from Sprites.Mask import Mask
from Screen import Screen


class MainMenuDesign(Design):
    elements = {
        "BackGround": BackGroundParallaxSprite(Config.BackGroundTextures.BACKGROUND_FOREST_LAYERS,
                                               speed_begin=50,
                                               speed_difference=0.8
                                               ),
        "Mask": Mask((30, 30), (Screen.width - 60, Screen.height - 60))
    }

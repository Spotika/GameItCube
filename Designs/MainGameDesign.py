import pygame
from Design import Design
from Sprites.BackGrounds import BackGroundParallaxSprite
import Config


class MainGameDesign(Design):
    GROUPS = {}
    ELEMENTS = {
        "backGround": BackGroundParallaxSprite(Config.BackGroundTextures.BACKGROUND_JUNGLE_LAYERS,
                                               speed_begin=40,
                                               speed_difference=0.8),
    }

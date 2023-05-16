import pygame
from Design import Design
from Sprites.BackGrounds import BackGroundParallaxSprite
import Config
from Sprites.Platform import Platform, PlatformGenerator
import random
from Group import Group
from Sprites.FpsShow import FpsShow
from Players.NinjaPlayer import NinjaPlayer


class MainGameDesign(Design):

    @classmethod
    def init_textures(cls):
        cls.set_groups({
        })
        ELEMENTS = {
            "backGround": BackGroundParallaxSprite(Config.BackGroundTextures.BACKGROUND_JUNGLE_LAYERS,
                                                   speed_begin=100,
                                                   speed_difference=0.8),
            "fps": FpsShow((400, 100), (0, 0)),
            "player": NinjaPlayer((100, 100)),
        }
        cls.set_elements(ELEMENTS)

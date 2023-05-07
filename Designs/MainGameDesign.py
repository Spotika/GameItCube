import pygame
from Design import Design
from Sprites.BackGrounds import BackGroundParallaxSprite
import Config
from Sprites.Platform import Platform, PlatformGenerator
import random
from Group import Group


class MainGameDesign(Design):

    @classmethod
    def init_textures(cls):
        cls.set_groups({
        })
        ELEMENTS = {
            "backGround": BackGroundParallaxSprite(Config.BackGroundTextures.BACKGROUND_JUNGLE_LAYERS,
                                                   speed_begin=40,
                                                   speed_difference=0.8),
        }
        cls.set_elements(ELEMENTS)

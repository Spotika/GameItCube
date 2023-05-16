import pygame
from Design import Design
from Sprites.BackGrounds import BackGroundParallaxSprite
import Config
from Sprites.FpsShow import FpsShow
from Players.NinjaPlayer import NinjaPlayer
from Sprites.SpriteModules.HeadUpDisplayModule import HeadUpDisplayModule


class MainGameDesign(Design):

    @classmethod
    def init_textures(cls):
        cls.set_groups({
        })
        ELEMENTS = {
            "backGround": BackGroundParallaxSprite(Config.BackGroundTextures.BACKGROUND_JUNGLE_LAYERS,
                                                   speed_begin=100,
                                                   speed_difference=0.8),
            "fps": FpsShow((0, 0), (400, 100)),
            "player": NinjaPlayer((100, 100)),
            "HUD": HeadUpDisplayModule((0, 0), (1600, 100))
        }
        cls.set_elements(ELEMENTS)

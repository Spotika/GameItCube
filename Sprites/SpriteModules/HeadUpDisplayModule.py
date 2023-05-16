import pygame
import Config
from Sprites.ImageLabel import ImageLabel
from Sprites.TextLabel import TextLabel
from .SpriteModule import SpriteModule


class HeadUpDisplayModule(SpriteModule):

    def __init__(self, position, dims, layer=Config.HUD_LAYER):
        super().__init__(position, dims, layer)

        self.set_design(
            {

            }
        )

        self.init_design()

    def update(self):
        self.update_design()
        self.update_image_by_design()

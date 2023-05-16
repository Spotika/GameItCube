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
                "back": ImageLabel((0, 0), self.dims, color=(0, 0, 0), layer=0),
                "heart": ImageLabel((19, 7), (40, 46), texture_path=Config.HEART_IMAGE_PATH),
                "clarity": ImageLabel((190, 7), (40, 46), texture_path=Config.CLARITY_IMAGE_PATH),
            }
        )

        self.init_design()

    def update(self):
        self.update_design()
        self.update_image_by_design()

    def collision_function(self, position) -> list[bool]:
        res = [False, False, False, False]

        if position[1] < self.position[1] + self.dims[1]:
            res[0] = True

        return res

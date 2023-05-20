import pygame
import Config
from Sprites.ImageLabel import ImageLabel
from Sprites.TextLabel import TextLabel
from .SpriteModule import SpriteModule
from Sprites.SpriteModules.ModuleParts.StateTracker import StateTracker
from Colors import Colors


class HeadUpDisplayModule(SpriteModule):

    def __init__(self, position, dims, layer=Config.HUD_LAYER):
        super().__init__(position, dims, layer)

        self.set_design(
            {
                "backImage": ImageLabel((0, 0), self.dims, color=Colors.DARK_GRAY, layer=0,
                                        texture_path=Config.HUD_BACK_TEXTURE),
                "heartImage": ImageLabel((12, 10), (60, 58), texture_path=Config.HEART_IMAGE_PATH),
                "clarityImage": ImageLabel((230, 13), (50, 55), texture_path=Config.CLARITY_IMAGE_PATH),

                "healthTracker": StateTracker((93, 24), (62, 31), font=("Consolas", 50)),
                "manaTracker": StateTracker((306, 23), (62, 31), font=("Consolas", 50)),

                "strengthImage": ImageLabel((523, 2), (20, 20), texture_path=Config.STRENGTH_IMAGE_PATH),
                "dexterityImage": ImageLabel((523, 29), (20, 20), texture_path=Config.DEXTERITY_IMAGE_PATH),
                "intelligenceImage": ImageLabel((523, 54), (20, 20), texture_path=Config.INTELLIGENCE_IMAGE_PATH),

                "strengthTracker": StateTracker((553, 3), (39, 19), font=("Consolas", 50)),
                "dexterityTracker": StateTracker((553, 29), (39, 19), font=("Consolas", 50)),
                "intelligenceTracker": StateTracker((553, 55), (39, 19), font=("Consolas", 50)),

                # TODO: сделать новый класс под слоты
                "spelSlot1Image": ImageLabel((639, 8), (60, 60), texture_path=Config.SPELL_SLOT_IMAGE_PATH),
                "spelSlot2Image": ImageLabel((744, 8), (60, 60), texture_path=Config.SPELL_SLOT_IMAGE_PATH),
                "spelSlot3Image": ImageLabel((849, 8), (60, 60), texture_path=Config.SPELL_SLOT_IMAGE_PATH),

                "moneyImage": ImageLabel((955, 20), (40, 45), texture_path=Config.MONEY_IMAGE_PATH),
                "moneyTracker": StateTracker((1018, 30), (55, 27), font=("Consolas", 50)),

                "levelTracker": StateTracker((1419, 31), (27, 19), font=("Consolas", 50)),
                "levelImage": ImageLabel((1407, 15), (50, 50), texture_path=Config.LEVEL_SLOT_IMAGE_PATH, layer=10),
                "experienceTracker": StateTracker((1465, 32), (79, 14), font=("Consolas", 50))
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

import pygame
from Sprites.SpriteModules.SpriteModule import SpriteModule
import Config
from Sprites.ImageLabel import ImageLabel
from Ability import Ability


class AbilityModule(SpriteModule):
    slot_image_path = Config.SPELL_SLOT_IMAGE_PATH

    ability: Ability = None
    """Способность модуля"""

    def __init__(self, position, dims):
        super().__init__(position, dims)

        self.set_design({
            "slot": ImageLabel((0, 0), (60, 60), texture_path=self.slot_image_path)
        })

        self.init_design()

    def add_ability(self, ability: Ability):
        self.ability = ability
        self.add_design("ability", ImageLabel((0, 0), (60, 60), texture_path=ability.texture_path))

    def update(self):
        if self.ability is not None:
            self.ability.update()

        self.update_design()
        self.update_image_by_design()

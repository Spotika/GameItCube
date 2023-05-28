import pygame
from Sprites.SpriteModules.SpriteModule import SpriteModule
import Config
from Sprites.ImageLabel import ImageLabel
from Ability import Ability
from Sprites.SpriteModules.ModuleParts.TimerMask import TimerMask


class AbilityModule(SpriteModule):
    slot_image_path = Config.SPELL_SLOT_IMAGE_PATH

    ability: Ability = None
    """Способность модуля"""

    def __init__(self, position, dims):
        super().__init__(position, dims)

        self.set_design({
            "slot": ImageLabel((0, 0), (60, 60), texture_path=self.slot_image_path, layer=100),
            "timer": TimerMask((0, 0), (60, 60))
        })

        self.init_design()

    def add_ability(self, ability: Ability, player, app):
        """Добавляет способность в модуль способности и присоединяет её к игроку"""
        self.ability = ability
        self.ability.link_player(player)
        self.ability.link_app(app)
        self.ability.init()
        self.add_design("ability", ImageLabel((0, 0), (60, 60), texture_path=ability.texture_path))
        self.get_design("timer").link_timer(ability.get_time_left_in_sec)

    def update(self):
        if self.ability is not None:
            self.ability.update()

        self.update_design()
        self.update_image_by_design()

    def call(self):
        """Вызывает способоность"""
        if self.ability is not None:
            self.ability.call()

    def refresh(self):
        if self.ability is not None:
            self.ability.refresh()

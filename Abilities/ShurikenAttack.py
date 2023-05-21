from Ability import Ability
import Config
from EventHandler import EventHandler


class ShurikenAttack(Ability):
    texture_path = Config.SHURIKEN_ATTACK_SPELL_TEXTURE_PATH

    delay = 1000

    @classmethod
    def call(cls):
        super().call()

    @classmethod
    def update(cls) -> None:
        ...

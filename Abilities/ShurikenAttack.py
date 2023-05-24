from Ability import Ability
import Config
from EventHandler import EventHandler
from Sprites.Shuriken import ShurukenGenerator
from Game import Game


class ShurikenAttack(Ability):
    texture_path = Config.SHURIKEN_ATTACK_SPELL_TEXTURE_PATH

    delay = None
    shurikenGenerator: ShurukenGenerator = None

    @classmethod
    def init(cls):
        cls.delay = Game.get_delay(Game.Shuriken.delay, EventHandler.DataStash.player.get_intelligence())
        cls.shurikenGenerator = ShurukenGenerator(cls.app)
        cls.refresh()

    @classmethod
    def call(cls):
        if super().call():
            cls.shurikenGenerator.generate()

    @classmethod
    def update(cls) -> None:
        ...

from Ability import Ability
import Config
from EventHandler import EventHandler
from Game import Game


class MagicSpell(Ability):
    """Ульта"""
    texture_path = Config.MAGIC_SPELL_TEXTURE

    delay = None

    @classmethod
    def init(cls):
        cls.delay = Game.get_delay(Game.MagicSpell.delay, EventHandler.DataStash.player.get_intelligence())
        cls.refresh()

    @classmethod
    def call(cls):
        if EventHandler.DataStash.player.check_mana(Game.MagicSpell.mana):
            if super().call():
                # TODO: Добавить отображение уровня ульты
                EventHandler.DataStash.player.decrease_mana(Game.MagicSpell.mana)
                Game.MagicSpell.increase_spell_level()

from Ability import Ability
import Config
from EventHandler import EventHandler
from Game import Game


class DodgeSpell(Ability):
    texture_path = Config.DODGE_SPELL_TEXTURE_PATH

    delay = None

    @classmethod
    def init(cls):
        cls.delay = Game.get_delay(Game.DodgeSpell.delay, EventHandler.DataStash.player.get_intelligence())
        cls.refresh()

    @classmethod
    def call(cls):
        if EventHandler.DataStash.player.check_mana(Game.DodgeSpell.mana):
            if super().call():
                EventHandler.DataStash.player.decrease_mana(Game.DodgeSpell.mana)
                EventHandler.DataStash.player.playerSpeedVector *= EventHandler.DataStash.player.get_dexterity() * \
                                                                   Game.DodgeSpell.scale_by_dexterity
                EventHandler.DataStash.player.playerSpeedVector.y = \
                    min(0, EventHandler.DataStash.player.playerSpeedVector.y)

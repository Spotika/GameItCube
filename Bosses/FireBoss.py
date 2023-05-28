from .Boss import Boss
import Config
from Animation import Animation
from EventHandler import EventHandler
from Sprites.Meteor import MeteorGenerator
from Game import Game


class FireBoss(Boss):
    idling_textures = Config.Boss.FireBoss.IDLING_TESTURES
    preparing_textures = Config.Boss.FireBoss.PREPARING_TEXTURES

    IDLING_DIMS = Config.Boss.FireBoss.IDLING_DIMS

    PREPARING_DIMS = Config.Boss.FireBoss.PREPARING_DIMS

    CASTING_TIME = 2000

    WAIT_AFTER_MOVE = 3000

    WAIT_AFTER_SHOW = 2000

    def __init__(self):
        super().__init__(self.IDLING_DIMS)

        self.animations["idling"] = Animation(textures_file_path=self.idling_textures, frame_rate=100,
                                              dims=self.IDLING_DIMS)
        self.animations["preparing"] = Animation(textures_file_path=self.preparing_textures,
                                                 frame_rate=70, dims=self.PREPARING_DIMS,
                                                 animation_time=self.CASTING_TIME)

        self.set_animation_state("idling")

        self.generator = MeteorGenerator()

    def cast(self):
        super().cast()
        self.generator.generate()

    def death(self):
        super().death()
        Game.MagicSpell.spellLevel //= 2
        EventHandler.DataStash.player.level += 2

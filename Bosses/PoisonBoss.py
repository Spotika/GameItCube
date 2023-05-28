from .Boss import Boss
import Config
from Animation import Animation
from Sprites.PoisonAttack import PoisonAttackGenerator
from EventHandler import EventHandler
from Game import Game


class PoisonBoss(Boss):
    idling_textures = Config.Boss.PoisonBoss.IDLING_TESTURES
    preparing_textures = Config.Boss.PoisonBoss.PREPARING_TEXTURES

    IDLING_DIMS = Config.Boss.PoisonBoss.IDLING_DIMS

    PREPARING_DIMS = Config.Boss.PoisonBoss.PREPARING_DIMS

    CASTING_TIME = 2000

    WAIT_AFTER_MOVE = 3000

    WAIT_AFTER_SHOW = 2000

    def __init__(self):
        super().__init__(self.IDLING_DIMS)

        self.animations["idling"] = Animation(textures_file_path=self.idling_textures, frame_rate=100,
                                              dims=self.IDLING_DIMS)
        self.animations["preparing"] = Animation(textures_file_path=self.preparing_textures,
                                                 frame_rate=70, dims=self.PREPARING_DIMS,
                                                 animation_time=Game.get_delay(self.CASTING_TIME,
                                                                               Game.EnvStats.get_any_attr()))

        self.animationFix["idling-preparing"] = (-23 * 3, -25 * 3)  # магические числа, они связаны с масштабом текстур

        self.set_animation_state("idling")

        self.attackGenerator = PoisonAttackGenerator()

        self.prev_level = EventHandler.DataStash.player.level

    def cast(self):
        super().cast()
        self.attackGenerator.generate((self.position[0] + self.dims[0] / 2,
                                       self.position[1] + self.dims[1] / 2))

    def death(self):
        super().death()
        EventHandler.DataStash.player.level = self.prev_level
        EventHandler.DataStash.app.refresh()
        EventHandler.DataStash.player.recover()

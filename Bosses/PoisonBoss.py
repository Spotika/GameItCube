from .Boss import Boss
import Config
from Animation import Animation


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
                                                 animation_time=self.CASTING_TIME)

        self.animationFix["idling-preparing"] = (-23 * 3, -25 * 3)  # магические числа, они связаны с масштабом текстур

        self.set_animation_state("idling")

import random

import pygame
from Entity import Entity
import Config
from Animation import Animation
from Game import Game


class WildBoarMob(Entity):
    @staticmethod
    def calculate_speed_left(speed_right):
        return 2 * Game.Platforms.speed + speed_right

    platform = None

    """Полатформа, к которой привязан моб"""

    BASE_SPEED_MODULE_RIGHT = Game.Mob.speed

    SPEED_MODULE_RIGHT_DIFF_PRECENT = 0.2

    PLATFORM_BORDER_OFFSET = Game.Mob.diff

    speedRight: int
    speedLeft: int

    def __init__(self, platform, player):
        self.platform = platform
        self.player = player
        super().__init__(self.calculate_position(), Config.BOAR_DIMS)

        self.animations["casual"] = Animation(Config.Animations.BoarMob.CASUAL_TEXTURES,
                                              dims=Config.BOAR_DIMS,
                                              frame_rate=50)
        self.set_animation_state("casual")

        self.speedRight = self.get_random_speed_right()
        self.speedLeft = self.calculate_speed_left(self.speedRight)

    def calculate_position(self):
        return [self.platform.position[0], self.platform.position[1] - Config.BOAR_DIMS[1]]

    def calculate_behavior(self):
        if self.platform.position[0] + self.PLATFORM_BORDER_OFFSET > self.position[0]:
            self.speedVector.x = self.speedRight
            self.set_state_by_name("direction", "right")
        if self.platform.position[0] + self.platform.width - self.PLATFORM_BORDER_OFFSET - self.dims[0] < \
                self.position[0]:
            self.speedVector.x = -self.speedLeft
            self.set_state_by_name("direction", "left")

    def get_random_speed_right(self):
        return random.randint(self.BASE_SPEED_MODULE_RIGHT * (1 - self.SPEED_MODULE_RIGHT_DIFF_PRECENT),
                              self.BASE_SPEED_MODULE_RIGHT * (1 + self.SPEED_MODULE_RIGHT_DIFF_PRECENT))

    def update(self):
        self.calculate_behavior()
        self.move_by_vector()
        self.update_rect_by_pos()
        self.render_image()

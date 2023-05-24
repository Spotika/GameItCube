import random
import math

import Scripts
from Entity import Entity
import Config
from Animation import Animation
from Game import Game
from EventHandler import EventHandler
from Vector2D import Vector2D


class WildBoarMob(Entity):
    pushing_speed_module = Game.Mob.push_speed

    @staticmethod
    def calculate_speed_left(speed_right):
        return 2 * Game.get_speed(Game.Platforms.speed, Game.EnvStats.get_any_attr()) + speed_right

    platform = None

    """Полатформа, к которой привязан моб"""

    BASE_SPEED_MODULE_RIGHT = Game.Mob.speed

    SPEED_MODULE_RIGHT_DIFF_PRECENT = 0.2

    PLATFORM_BORDER_OFFSET = Game.Mob.diff

    speedRight: int
    speedLeft: int

    def __init__(self, platform):
        self.platform = platform
        self.player = EventHandler.DataStash.player
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
        s = random.randint(self.BASE_SPEED_MODULE_RIGHT * (1 - self.SPEED_MODULE_RIGHT_DIFF_PRECENT),
                           self.BASE_SPEED_MODULE_RIGHT * (1 + self.SPEED_MODULE_RIGHT_DIFF_PRECENT))
        return Game.get_speed(s, Game.EnvStats.get_any_attr())

    def get_exp(self):
        return random.randint(Game.Mob.min_exp, Game.Mob.max_exp)

    def update(self):
        super().update()
        self.calculate_behavior()
        self.move_by_vector()
        self.update_rect_by_pos()
        self.render_image()

        # TODO сделать коллизии с кабанчиками и добавить урон

        if self.rect.colliderect(EventHandler.DataStash.player.rect):
            teta = Scripts.get_angle_between_points(self.rect.center, EventHandler.DataStash.player.rect.center)

            push = Vector2D.from_polar(teta=math.pi - teta, r=Game.get_speed(self.pushing_speed_module,
                                                                             Game.EnvStats.get_any_attr()))
            EventHandler.DataStash.player.playerSpeedVector = push
            EventHandler.DataStash.player.damage(Game.get_damage(Game.Mob.damage, Game.EnvStats.get_any_attr()))

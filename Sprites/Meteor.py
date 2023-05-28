import pygame

from Entity import Entity
import Config
from Animation import Animation
from Vector2D import Vector2D
from Game import Game
import random
from Screen import Screen
from EventHandler import EventHandler

import math


class Meteor(Entity):
    currentAnimationState = "casual"

    did_damage = False

    def __init__(self, position, direction):
        super().__init__(position, Config.Meteor.METEOR_DIMS)

        self.animations["casual"] = Animation(textures_file_path=Config.Meteor.TYPE_TEXTURES[direction],
                                              frame_rate=80)
        r = Config.Meteor.speed
        self.direction = direction
        self.speedVector.zero()
        tetha = 0
        match direction:
            case "L":
                tetha = math.radians(180)
            case "R":
                tetha = 0
            case "RD":
                tetha = math.radians(330)
            case "LD":
                tetha = math.radians(210)
            case "D":
                tetha = math.radians(270)
        self.speedVector = Vector2D.from_polar(tetha=tetha, r=r)

        self._mask = pygame.mask.from_surface(self.image, threshold=200)

    def update(self) -> None:
        self.check_delete()
        self.check_collide()
        self.move_by_vector()
        self.update_rect_by_pos()
        self.render_image()

    def check_collide(self):
        # столкновение с игроком
        if not self.did_damage:
            if pygame.sprite.collide_mask(self, EventHandler.DataStash.player) is not None:
                # Урон игроку
                player = EventHandler.DataStash.player
                player.damage(player.get_max_health() * (Game.Meteor.damage_precent))
                self.did_damage = True

        # столкновение с платформой
        # TODO: оптимизировать проверку коллизий. Слишком долго работает
        platformGroup = EventHandler.DataStash.platformGenerator.platformGroup
        for platform in platformGroup:
            if pygame.sprite.collide_mask(self, platform):
                if random.random() < Game.get_chance(Game.Meteor.chance_to_destroy):
                    # Уничтожение
                    if not random.random() < Game.get_chance(Game.Meteor.chance_to_save):
                        self.kill()
                    # Уничтожение платформы
                    platform.destroy()

    def check_delete(self):
        delete = False

        match self.direction:
            case "L":
                delete = self.rect.x + self.dims[0] < 0
            case "R":
                delete = self.rect.x > Screen.width
            case "RD":
                delete = self.rect.x > Screen.width or self.rect.y > Screen.height
            case "LD":
                delete = self.rect.x + self.dims[0] < 0 or self.rect.y > Screen.height
            case "D":
                delete = self.rect.y > Screen.height

        if delete:
            self.kill()


class MeteorGenerator:
    meteorGroup = None

    # FIXME подправить значения
    SPAWN_LIM = {
        "RD": ((-Screen.width // 2, Screen.width // 2), (-Config.Meteor.METEOR_DIMS[1], -Config.Meteor.METEOR_DIMS[1])),

        "LD": ((Screen.width // 2, Screen.width // 2 + Screen.width),
               (-Config.Meteor.METEOR_DIMS[1], -Config.Meteor.METEOR_DIMS[1])),

        "D": ((0, Screen.width - Config.Meteor.METEOR_DIMS[0]),
              (-Config.Meteor.METEOR_DIMS[1], -Config.Meteor.METEOR_DIMS[1])),

        "R": ((-Config.Meteor.METEOR_DIMS[0], -Config.Meteor.METEOR_DIMS[0]),
              (Config.HUD_HEIGHT, Screen.height - Config.Meteor.METEOR_DIMS[1])),

        "L": ((Screen.width + Config.Meteor.METEOR_DIMS[0], Screen.width + Config.Meteor.METEOR_DIMS[0]),
              (Config.HUD_HEIGHT, Screen.height - Config.Meteor.METEOR_DIMS[1])),
    }

    def __init__(self) -> None:
        self.meteorGroup = pygame.sprite.Group()

    def generate(self) -> None:
        for i in range(1):
            direction = self.get_direction()
            newMeteor = Meteor(self.get_pos_by_direction(direction), direction)
            self.meteorGroup.add(newMeteor)
            EventHandler.DataStash.app.allSprites.add(newMeteor)

    @classmethod
    def get_pos_by_direction(cls, direction):
        lim = cls.SPAWN_LIM[direction]
        return [random.randint(lim[0][0], lim[0][1]), random.randint(lim[1][0], lim[1][1])]

    @staticmethod
    def get_direction() -> str:
        """Возвращает случайное направление"""
        return random.choice(["L", "R", "D", "LD", "RD"])

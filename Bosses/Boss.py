import random

import Config
from Screen import Screen
from Entity import Entity
import pygame
from Animation import Animation
from Game import Game
from EventHandler import EventHandler
import Scripts
from Vector2D import Vector2D


class Boss(Entity):
    idling_textures: str
    preparing_textures: str

    WAIT_AFTER_MOVE = 0
    """Время ожидания между передвижениями"""
    WAIT_AFTER_SHOW = 0
    """Время ожидания после показа"""
    CASTING_TIME = 0
    """Время каста заклинания"""

    def __init__(self, dims):
        super().__init__([0, 0], dims)

        self.layer = 10000

        self.health = Game.Boss.attack_for_beat * Game.get_damage(Game.Shuriken.damage,
                                                                  EventHandler.DataStash.player.strength)
        self.max_health = self.health

        self.casted = 0

        self.position = self.get_random_pos_for_spawn()

        self.STATE_NAMES = [
            ("showing", True),
            ("being", False),
            ("hiding", False),
            ("isLiving", True),
            ("moving", True),
            ("moveWait", False),
        ]

        self.animations = {
            "idling": Animation(),
            "preparing": Animation()
        }

        self.load_states_from_names()

        self.targetPoint = (0, 0)

        self.alpha = None

        self.DIFF = 0

        self.nowTime = None

    def calculate_behavior(self) -> None:
        """Вычисляет поведение босса"""
        if self.get_state_by_name("moveWait"):
            if not self.wait(Game.Boss.get_time_wait(self.WAIT_AFTER_MOVE)):
                return
            self.set_state_by_name("moveWait", False)

        if self.get_state_by_name("showing"):
            # показ босса
            if self.position[0] > Screen.width - self.dims[0]:
                self.speedVector.x = -3 * Game.Boss.showingSpeed
            else:
                self.speedVector.zero()
                if not self.wait(Game.Boss.get_time_wait(self.WAIT_AFTER_SHOW)):
                    return
                self.set_state_by_name("showing", False)
                self.set_state_by_name("being", True)
                self.set_state_by_name("moving", True)
                self.targetPoint = self.get_moving_target()

        if self.casted >= Game.Boss.max_casts and self.get_state_by_name("being"):
            # проверка на уход
            self.set_state_by_name("being", False)
            self.set_state_by_name("hiding", True)

        elif self.get_state_by_name("hiding"):
            # уход босса за экран
            self.speedVector.y = Game.get_speed(2 * Game.Boss.showingSpeed, Game.EnvStats.get_any_attr())
            if self.position[1] + self.dims[1] <= 0:
                self.kill()
                EventHandler.DataStash.numOfBosses -= 1

        if self.get_state_by_name("being"):
            # передвижение босса и каст
            if self.get_state_by_name("moving"):
                self.move_to_target()
            else:
                if self.cast_preparing():
                    self.targetPoint = self.get_moving_target()
                    self.set_state_by_name("moving", True)
                    self.set_state_by_name("moveWait", True)

    def update(self) -> None:
        self.calculate_behavior()
        self.move_by_vector()
        self.update_rect_by_pos()
        self.render_image()

        if self.isLiving:
            self.blit_image_by_health()

    def get_random_pos_for_spawn(self) -> list[int, int]:
        return [Screen.width, random.randint(Config.HUD_HEIGHT, round(Screen.height - self.dims[1]))]

    def death(self):
        self.set_state_by_name("isLiving", False)
        self.kill()
        EventHandler.DataStash.numOfBosses -= 1

    def get_moving_target(self) -> list[int, int]:
        """Возвращает случайную точку карты для передвижения туда"""
        return [random.randint(0, round(Screen.width - self.dims[0])),
                random.randint(Config.HUD_HEIGHT, round(Screen.height - self.dims[1]))]

    def move_to_target(self):
        """Перемещает босса в точку"""
        if self.rect.colliderect((self.targetPoint[0], self.targetPoint[1]),
                                 (self.targetPoint[0] * (1 + self.DIFF), self.targetPoint[1] * (1 + self.DIFF))):
            self.set_state_by_name("moving", False)
            self.alpha = None
            self.speedVector.zero()
            return
        else:
            if self.alpha is None:
                # Эта шляпа вроде работает и перемещает босса в целевую точку
                self.alpha = Scripts.get_angle_between_points(self.targetPoint, self.position)
                self.speedVector = Vector2D.from_polar(teta=self.alpha, r=Game.get_speed(Game.Boss.showingSpeed,
                                                                                         Game.EnvStats.get_any_attr()))
                self.speedVector.x = self.speedVector.x

    def wait(self, time):
        if self.nowTime is None:
            self.nowTime = EventHandler.get_ticks()
        else:
            if EventHandler.get_ticks() - self.nowTime >= time:
                self.nowTime = None
                return True
        return False

    def cast_preparing(self) -> bool:
        """Готовится каставать заклинание"""
        if self.get_animation_state() == "idling":
            self.set_animation_state("preparing")
        else:
            if (anim := self.get_animation_by_current_state()).is_end():
                self.casted += 1
                self.set_animation_state("idling")
                self.cast()
                return True
            else:
                anim.next_sprite()
        return False

    def cast(self):
        """Кастует заклинание"""
        print("casted")

    def __str__(self):
        return "Boss"

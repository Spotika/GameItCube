import random

import pygame
from Label import Label
from Vector2D import Vector2D
from typing import Any
from Animation import Animation
from App import App
from EventHandler import EventHandler
from Screen import Screen
from Game import Game
import Scripts


class Entity(Label):
    """Базовый класс существа"""

    max_exp, min_exp = 0, 0

    """Статы моба"""
    health: int

    isLiving: bool = True

    STATE_NAMES: list[tuple[str, Any]] = None
    """все возможные имена состояний игрока и их значения по умолчанию (<имя>, <значение>)"""

    states: dict[str, Any]
    """состояния игрока в JSON формате"""

    currentAnimationState: str = "idling"
    """текущее состояние анимации игрока"""

    animations: dict[str, Animation] = None
    """анимации, присущие каждому состоянию"""

    animationFix: dict[str, tuple[float, float]]
    """Хранит поправки на координаты анимаций вида {'animationName1-animationName2' : (offsetX, offsetY)}"""

    speedVector: Vector2D
    """Вектор скорости"""

    app: App = None

    damage_senders: set

    def __init__(self, position, dims):
        super().__init__(position, dims)
        self.speedVector = Vector2D()
        self.STATE_NAMES = [
            ("direction", "right"),  # направление взгляда существа
        ]
        self.states = {}
        self.load_states_from_names()
        self.animations = {}
        self.animationFix = {}
        self.app = EventHandler.DataStash.app
        self.damage_senders = set()
        self.health = Game.get_health_max(Game.Mob.healthBase, Game.EnvStats.get_any_attr())
        self.max_health = self.health

    def set_animation_state(self, state: str) -> None:
        self.get_animation_by_current_state().reset()
        # поправки в координатах между переходами
        prev_state = self.get_animation_state()
        if f"{prev_state}-{state}" in self.animationFix.keys():
            offset = self.animationFix[f"{prev_state}-{state}"]
            self.move(offset[0], offset[1])

        elif f"{state}-{prev_state}" in self.animationFix.keys():
            offset = self.animationFix[f"{state}-{prev_state}"]
            self.move(-offset[0], -offset[1])

        self.currentAnimationState = state
        self.set_dims(self.get_animation_by_current_state().dims)

    def get_animation_state(self) -> str:
        return self.currentAnimationState

    def get_animation_by_current_state(self) -> Animation:
        return self.animations[self.currentAnimationState]

    def get_animation_by_state(self, state) -> Animation:
        return self.animations[state]

    def set_image(self, image, transform=True) -> None:
        if self.get_state_by_name("direction") == "left":
            image = pygame.transform.flip(image, True, False)

        super().set_image(image, transform)

    def load_states_from_names(self):
        """Загружает в локальный атрибут states значения из STATE_NAMES"""
        for name in self.STATE_NAMES:
            self.states[name[0]] = name[1]

    def get_state_by_name(self, name: str) -> Any:
        """Возвращает состояние из states по имени"""
        if name not in self.states.keys():
            raise ValueError(f"Нет состояния с именем {name}")
        return self.states[name]

    def set_state_by_name(self, name: str, state: Any) -> None:
        self.states[name] = state

    def extend_state_names(self, names: tuple[str, Any] | list[tuple[str, Any]]):
        """Добавляет в атрибут STATE_NAMES другие имена и их значения"""
        if isinstance(names, tuple):
            self.STATE_NAMES.append(names)
        else:
            self.STATE_NAMES.extend(names)

    """Перемещение моба"""

    def move_by_vector(self):
        dt = EventHandler.get_dt() / 1000
        self.move(self.speedVector.x * dt, -self.speedVector.y * dt)

    def render_image(self):
        """Устанавливает изображение"""
        self.set_image(self.get_animation_by_current_state().next_sprite())

    def update(self) -> None:
        if self.out_of_screen():
            self.kill()

    def blit_image_by_health(self):

        image = Scripts.blit_color_by_precent(self.get_image(), 1 - (self.health / self.max_health))
        # костыль
        if self.get_state_by_name("direction") == "left":
            image = pygame.transform.flip(image, True, False)
        self.set_image(image)

    def out_of_screen(self):
        return self.position[0] + self.dims[0] + 1 < 0

    def get_exp(self):
        return random.randint(self.min_exp, self.max_exp)

    def damage(self, value):
        """Наносит урон"""
        self.health -= value
        if self.health <= 0:
            self.death()

    def death(self):
        """Вызывается при естесственной смерти"""
        EventHandler.DataStash.player.add_exp(self.get_exp())
        self.kill()

    def damage_from(self, sender, damage):
        if sender not in self.damage_senders:
            print(damage, self)
            self.damage(damage)
            self.damage_senders.add(sender)

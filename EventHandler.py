import pygame
from Screen import Screen
import Config


class EventHandler:
    _events = None
    _mousePressed = None
    _mousePos = None

    groups = []

    clock = pygame.time.Clock()

    dt = 0
    """Время между тиками в милисекундах"""

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def update(cls, instance):
        cls._events = pygame.event.get()
        cls._mousePressed = pygame.mouse.get_pressed(3)
        cls._mousePos = pygame.mouse.get_pos()
        """обновление состояний"""

        """Обновление групп в конкретном приложении"""
        for group in instance.GROUPS.values():
            # group.link_to_sprites(instance.allSprites)
            group.call()

        for event in cls._events:
            """ТУТ ОБЩАЯ ОБРАБОТКА ЭВЕНТОВ"""

            if event.type == pygame.QUIT:
                exit(0)  # выход

    @classmethod
    def get_events(cls):
        return cls._events

    @classmethod
    def get_mouse_pressed(cls):
        return cls._mousePressed

    @classmethod
    def get_mouse_pos(cls):
        return cls._mousePos

    @classmethod
    def tick(cls):
        cls.dt = cls.clock.tick(Config.FPS)

    @classmethod
    def get_dt(cls):
        return cls.dt

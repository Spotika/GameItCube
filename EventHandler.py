import pygame
import Config
from collections import deque
from typing import Any


class EventHandler:
    _events = None
    _mousePressed = None
    _mousePos = None

    groups = []

    clock = pygame.time.Clock()

    dt = 0
    """Время между тиками в милисекундах"""

    eventStream: dict["str", deque[tuple["str", Any]]] = {}
    """Штука позволяющая обмениваться событиями игры во всём приложении
    Работает так: 
    существует класс событий, каждое событие делится на тип и данные (любые)
    """

    @classmethod
    def push_to_stream(cls, event_class: str, event_type: str, event_data: Any) -> None:
        """Создает событие по данным и добавляет в поток
            Если нет класса событий, то создает его"""
        if event_class not in cls.eventStream.keys():
            cls.add_event_class(event_class)

        cls.eventStream[event_class].append((event_type, event_data))

    @classmethod
    def get_from_stream(cls, event_class: str, delete: bool = True) -> tuple[str, Any] | None:
        """Возврашает первое в очереди событие и удаляет его если delete = True
        Если событий данного класса нет, то возвращает None.
        Если нет класса событий, то создает его
        """
        if event_class not in cls.eventStream.keys():
            cls.add_event_class(event_class)
            return None

        if len(cls.eventStream[event_class]) == 0:
            return None

        if delete:
            data = cls.eventStream[event_class].pop()
        else:
            data = cls.eventStream[event_class][0]

        return data

    @classmethod
    def add_event_class(cls, event_class: str) -> None:
        """Создаёт класс события"""
        cls.eventStream[event_class] = deque()

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def update(cls, instance):
        cls._events = pygame.event.get()
        cls._mousePressed = pygame.mouse.get_pressed(3)
        cls._mousePos = pygame.mouse.get_pos()
        cls._keysPressed = pygame.key.get_pressed()
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
    def get_events(cls) -> list[pygame.event.Event]:
        return cls._events

    @classmethod
    def get_mouse_pressed(cls):
        return cls._mousePressed

    @classmethod
    def get_key_pressed(cls):
        return cls.get_key_pressed

    @classmethod
    def get_mouse_pos(cls):
        return cls._mousePos

    @classmethod
    def tick(cls):
        cls.dt = cls.clock.tick(Config.FPS)

    @classmethod
    def get_dt(cls):
        """Возвращает милисекунды"""
        return cls.dt

    @classmethod
    def get_fps(cls) -> float:
        """Возвращает кол во фпс"""
        return cls.clock.get_fps()

    @classmethod
    def get_ticks(cls) -> int:
        """Возвращает то, что возвращает pygame.time.get_ticks()"""
        return pygame.time.get_ticks()

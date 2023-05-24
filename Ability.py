import pygame
from EventHandler import EventHandler


class Ability:
    texture_path: str
    """Путь до текстуры способности"""

    player = None
    """Игрок"""

    delay: int = 100
    """Задержка между приминениями способности"""

    nowTime: int = 0
    """Количество тиков с прошлого применения"""

    app = None

    @classmethod
    def link_player(cls, player) -> None:
        """Присоединение игрока к способности"""
        cls.player = player

    @classmethod
    def link_app(cls, app):
        cls.app = app

    @classmethod
    def update(cls) -> None:
        """Обновление способности"""
        ...

    @classmethod
    def call(cls):
        """Активация способности"""

        # простая проверка на время
        if (ticks := EventHandler.get_ticks()) - cls.nowTime >= cls.delay:
            # активация
            cls.nowTime = ticks
            return True
        else:
            return False

    @classmethod
    def get_time_left_in_sec(cls):
        """Возвращает время до отката кд способности"""
        t = max(0, (cls.delay - (EventHandler.get_ticks() - cls.nowTime)) / 1000)

        return round(t, 1)

    @classmethod
    def init(cls):
        ...

    @classmethod
    def refresh(cls):
        cls.nowTime = EventHandler.get_ticks() - cls.delay

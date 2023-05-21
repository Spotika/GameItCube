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

    @classmethod
    def link_player(cls, player) -> None:
        """Присоединение игрока к способности"""
        cls.player = player

    @classmethod
    def update(cls) -> None:
        """Обновление способности"""
        ...

    @classmethod
    def call(cls) -> None:
        """Активация способности"""

        # простая проверка на время
        if (ticks := EventHandler.get_ticks()) - cls.nowTime >= cls.delay:
            # активация
            cls.nowTime = ticks

    @classmethod
    def get_time_left_in_sec(cls) -> int:
        """Возвращает время до отката кд способности"""
        return max(0, (cls.delay - (EventHandler.get_ticks() - cls.nowTime - 999)) // 1000)

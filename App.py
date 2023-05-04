import pygame
from Screen import *


class App:
    running: bool = True

    instances: dict = {}

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def link(cls, instance):
        cls.instances[str(instance.__name__)] = instance

    @classmethod
    def begin(cls):
        """Старт работы и инициализация всех переменных"""

    @classmethod
    def end(cls):
        """Окончание работы"""

    @classmethod
    def render(cls):
        """Отрисовка экрана"""
        ...

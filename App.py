import pygame
from Screen import *


class App:
    """
    Должен быть атрибут allSprites: pygame.sprite.LayeredUpdates \n
    каждый потомок должен линкаться в файле определения
    """

    running: bool = True

    instances: dict = {}

    allSprites: pygame.sprite.LayeredUpdates()
    """контейнер для спрайтов"""

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def link(cls, instance):
        cls.instances[str(instance.__name__)] = instance

    @classmethod
    def begin(cls, *args, **kwargs):
        """Старт работы и инициализация всех переменных"""
        cls.running = True
        cls.allSprites = pygame.sprite.LayeredUpdates()
        cls.loop(*args, **kwargs)

    @classmethod
    def loop(cls, *args, **kwargs):
        """Основной движок приложения"""
        cls.end(*args, **kwargs)

    @classmethod
    def end(cls, *args, **kwargs):
        """Окончание работы"""
        cls.running = False
        pygame.display.update()
        Screen.display.fill((0, 0, 0))

    @classmethod
    def render(cls):
        """Отрисовка экрана"""
        Screen.display.fill((0, 0, 0))
        cls.allSprites.update()
        cls.allSprites.draw(Screen.display)
        pygame.display.update()

    @classmethod
    def check_events(cls):
        """Обработка локальных эвентов"""

    @classmethod
    def redirect(cls, app_name):
        if app_name not in cls.instances.keys():
            raise ValueError("Не подключено приложение " + str(app_name))
            return
        cls.instances[app_name].begin()

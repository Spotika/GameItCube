import pygame
from Screen import *
from QueryDeque import QueryDeque

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
        Screen.update_display()

    @classmethod
    def check_events(cls):
        """Обработка локальных эвентов"""

    @classmethod
    def redirect(cls, app_name: str, use_deque=True, *args, **kwargs):
        """Отправляет запрос на переключение приложения в очередь при этом приложение должно завершиться.\n\n
        Если требуется прервать приложение на работу другого, а потом вернуться, например пауза, то аргумент
        *use_deque* должен равняться False, однако ВАЖНО: при использовании значения False следует опасаться рекурсии
        """
        """проверка на подключенность"""
        if app_name not in cls.instances.keys():
            raise ValueError("Не подключено приложение " + str(app_name))
            return

        if use_deque:
            QueryDeque.add(cls.instances[app_name], *args, **kwargs)
        else:
            cls.instances[app_name].begin(*args, **kwargs)

import pygame


class EventHandler:
    _events = None
    _mousePressed = None
    _mousePos = None

    groups = []

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def update(cls):
        cls._events = pygame.event.get()
        cls._mousePressed = pygame.mouse.get_pressed(3)
        cls._mousePos = pygame.mouse.get_pos()

        """обновление групп"""
        for group in cls.groups:
            group.call()

        for event in cls._events:
            """ТУТ ОБРАБОТКА ЭВЕНТОВ"""

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
    def add_group(cls, group):
        cls.groups.append(group)

    @classmethod
    def del_group(cls, group):
        cls.groups.remove(group)

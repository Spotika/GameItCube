import pygame


class EventHandler:
    _events = None

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def update(cls):
        cls._events = pygame.event.get()

        for event in cls._events:
            """ТУТ ОБРАБОТКА ЭВЕНТОВ"""

            if event.type == pygame.QUIT:
                exit(0)

    @classmethod
    def get_events(cls):
        return cls._events

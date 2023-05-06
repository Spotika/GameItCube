import pygame


class Screen:
    width: int = 1600 # 1600

    height: int = 800 # 1000

    display: pygame.Surface

    title: str = "Game"

    allSprites = pygame.sprite.LayeredUpdates()

    def __new__(cls, *args, **kwargs):
        # Нельзя создать объект этого класса
        return None

    @classmethod
    def begin(cls):
        """init display and other"""
        cls.display = pygame.display.set_mode((cls.width, cls.height), )
        pygame.display.set_caption(cls.title)
        cls.update()

    @classmethod
    def update(cls):
        """обновление размера экрана"""
        cls.width, cls.height = cls.display.get_width(), cls.display.get_height()

import pygame


class Screen:
    width: int = 1600 // 2 # 1600

    height: int = 1000 // 2 # 1000

    display: pygame.Surface

    title: str = "Game"

    allSprites = pygame.sprite.LayeredUpdates()

    def __new__(cls, *args, **kwargs):
        # Нельзя создать объект этого класса
        return None

    @classmethod
    def begin(cls):
        """init display and other"""
        cls.display = pygame.display.set_mode((cls.width, cls.height))
        pygame.display.set_caption(cls.title)


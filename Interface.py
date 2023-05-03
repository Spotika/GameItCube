import pygame


class Interface:
    height: int = 0
    width: int = 0

    position: tuple[int, int] = (0, 0)

    texture_path: str = ""

    layer: int = 0

    def get_data_for_blit(self):
        """returns a tuple of surface and position for blitting"""
        return pygame.Surface((0, 0))

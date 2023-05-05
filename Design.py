import pygame
from App import App


class Design:
    """
    Наследовать он него только классы Apps
    """
    elements: dict

    @classmethod
    def link_to_all_sprites(cls):
        for elem in cls.elements.values():
            cls.allSprites.add(elem)

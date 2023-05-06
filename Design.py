import pygame
from App import App
from Group import Group


class Design:
    """
    Наследовать он него только классы Apps
    Дизайны пишутся для экрана размером 1600 800
    """
    WIDTH = 1600
    HEIGHT = 1000

    ELEMENTS: dict
    GROUPS: dict

    @classmethod
    def init_sprites_and_groups(cls):
        """Добавляет все элементы и группы в allSprites
        """
        for elem in cls.ELEMENTS.values():
            cls.allSprites.add(elem)

    @classmethod
    def link_function_to_button(cls, button_name, function):
        if button_name not in cls.ELEMENTS.keys():
            return
        cls.ELEMENTS[button_name].set_on_click(function)

import pygame
from App import App
from Group import Group

class Design:
    """
    Наследовать он него только классы Apps
    Дизайгы пишутся для экрана размером 1600 800
    """
    WIDTH = 1600
    HEIGHT = 1000

    ELEMENTS: dict
    GROUPS: dict

    @classmethod
    def link_to_all_sprites(cls):
        for elem in cls.ELEMENTS.values():
            cls.allSprites.add(elem)
        for elem in cls.GROUPS.values():
            elem.link_to_sprites(cls.allSprites)

    @classmethod
    def link_function_to_button(cls, button_name, function):
        if button_name not in cls.ELEMENTS.keys():
            return
        cls.ELEMENTS[button_name].set_on_click(function)


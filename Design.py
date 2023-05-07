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
    def init_textures(cls):
        """инициализирует GROUPS и ELEMENTS"""

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

    @classmethod
    def get_group(cls, name: str):
        if name not in cls.GROUPS.keys():
            raise ValueError(f"Группы с именем {name} не существует\n Все имена: {', '.join(cls.GROUPS.keys())}")
        return cls.GROUPS[name]

    @classmethod
    def get_element(cls, name: str):
        if name not in cls.ELEMENTS.keys():
            raise ValueError(f"Элемента с именем {name} не существует\n Все имена: {', '.join(cls.ELEMENTS.keys())}")
        return cls.ELEMENTS[name]

    @classmethod
    def set_elements(cls, elements: dict):
        cls.ELEMENTS = elements

    @classmethod
    def set_groups(cls, groups: dict):
        cls.GROUPS = groups


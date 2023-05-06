import pygame
from EventHandler import *


class Group:
    """Хрень которая объеденяет объекты в группы и позволяет с помощью EventHandler обновлять их состояние"""

    def __init__(self):
        self.objects = []
        EventHandler.add_group(self)  # добавление новой группы в обработку

    def add(self, obj: object | list):
        if isinstance(obj, list):
            self.objects.extend(obj)
            return self
        self.objects.append(obj)
        return self

    def link_to_sprites(self, sprites):
        for obj in self.objects:
            sprites.add(obj)

    def call(self, *args, **kwargs):
        for obj in self.objects:
            obj.group_function(*args, **kwargs)

    def __del__(self):
        EventHandler.del_group(self)

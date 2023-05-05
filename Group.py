import pygame
from EventHandler import *


class Group:
    """Хрень которая объеденяет объекты в группы и позволяет с помощью EventHandler обновлять из состояние"""

    def __init__(self):
        self.objects = []
        EventHandler.add_group(self)  # добавление новой группы в обработку

    def add(self, obj):
        self.objects.append(obj)

    def link_to_sprites(self, sprites):
        for obj in self.objects:
            sprites.add(obj)

    def call(self, *args, **kwargs):
        for obj in self.objects:
            obj.group_function(*args, **kwargs)

    def __del__(self):
        EventHandler.del_group(self)

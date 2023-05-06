import pygame
from EventHandler import EventHandler


class Group:
    """Хрень которая объеденяет объекты в группы и позволяет с помощью приложения обновлять их состояние"""

    def __init__(self):
        self.objects = []

    def add(self, obj: object | list):
        """Добавляет в группу объект или список объектов"""
        if isinstance(obj, list):
            self.objects.extend(obj)
            return self
        self.objects.append(obj)
        return self

    def link_to_sprites(self, sprites):
        """Каждый объект в группе подгружает в allsprites приложения"""
        for obj in self.objects:
            sprites.add(obj)

    def call(self, *args, **kwargs):
        """Вызывает групповую функцию у участников группы"""
        for obj in self.objects:
            obj.group_function(*args, **kwargs)

import pygame


class Group:
    

    def __init__(self):
        self.objects = []

    def add(self, obj):
        self.objects.append(obj)

    def link_to_sprites(self, sprites):
        for obj in self.objects:
            sprites.add(obj)

    def call(self, *args, **kwargs):
        for obj in self.objects:
            obj.group_function(*args, **kwargs)
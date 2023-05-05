import pygame


class Design:
    elements: list[pygame.sprite.Sprite]

    @classmethod
    def link_to_all_sprites(cls, all_sprites):
        for elem in cls.elements:
            all_sprites.add(elem)


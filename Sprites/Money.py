import pygame
from .ImageLabel import ImageLabel


class Coin(ImageLabel):

    def collision_function(self, position):
        return self.rect.collidepoint(*position)


class MoneyGenerator:
    HEIGHT_ABOVE_PLATFORM = 10
    """Высота монеток над платформой"""

    coinGroup: pygame.sprite.Group[Coin]
    """Список монет"""

    allSprites: pygame.sprite.LayeredUpdates
    """аллспрайтс проиложения"""

    def __init__(self, all_sprites, platform_generator, player):
        self.allSprites = all_sprites
        self.platformGenerator = platform_generator
        self.player = player



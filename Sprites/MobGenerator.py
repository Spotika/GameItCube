import random

import pygame
from EventHandler import EventHandler
from Mobs.WildBoarMob import WildBoarMob


class MobGenerator:
    mobGroup: pygame.sprite.Group

    allSprites: pygame.sprite.LayeredUpdates

    mobTypeList: list
    """Список типов мобов"""

    def __init__(self, all_sprites, player):
        self.mobTypeList = [WildBoarMob]
        self.mobGroup = pygame.sprite.Group()
        self.allSprites = all_sprites
        self.player = player

    def add_mob_to_group(self, coin):
        self.mobGroup.add(coin)

    def add_mob_to_sprites(self, coin):
        self.allSprites.add(coin)

    def generate_mob(self, platform):
        newMob = self.get_random_mob()(platform, self.player)
        self.add_mob_to_sprites(newMob)
        self.add_mob_to_group(newMob)

    def get_random_mob(self):
        return random.choice(self.mobTypeList)

    def update(self):
        if (platform := EventHandler.get_from_stream("MoneyGenerator")) is not None:
            if platform[0] == "platform_for_mob":
                self.generate_mob(platform[1])

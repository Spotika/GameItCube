import pygame
from EventHandler import EventHandler
from Bosses.PoisonBoss import PoisonBoss
import random
from Game import Game
from Bosses.Boss import Boss


class BossGenerator:
    bossTypeList: list
    """список типов боссов"""

    bossGroup: pygame.sprite.Group

    def __init__(self):
        self.bossTypeList = [PoisonBoss]
        self.bossGroup = pygame.sprite.Group()
        EventHandler.DataStash.numOfBosses = 0

    def update(self):
        if EventHandler.DataStash.numOfBosses < Game.Boss.max_bosses:
            if EventHandler.get_from_stream("Player", "level_up") is not None:
                if random.random() < Game.get_chance(Game.Boss.chanceToSpawn):
                    self.generate()

    def get_random_boss(self):
        return random.choice(self.bossTypeList)

    def generate(self):
        newBoss: Boss = self.get_random_boss()()

        EventHandler.DataStash.app.allSprites.add(newBoss)
        self.bossGroup.add(newBoss)
        EventHandler.DataStash.numOfBosses += 1

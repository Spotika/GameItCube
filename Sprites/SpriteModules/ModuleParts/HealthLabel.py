import pygame
from Sprites.TextLabel import TextLabel


class HealthLabel(TextLabel):
    player = None

    def add_player(self, player):
        self.player = player
        return self

    def update(self):
        health = self.player.get_health()

        self.write(health)

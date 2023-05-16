import pygame
from Sprites.TextLabel import TextLabel


class ManaLabel(TextLabel):
    player = None

    def add_player(self, player):
        self.player = player
        return self

    def update(self):
        mana = self.player.get_mana()

        self.write(mana)

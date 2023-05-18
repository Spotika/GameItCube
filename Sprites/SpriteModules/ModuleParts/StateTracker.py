import pygame
from Sprites.TextLabel import TextLabel


class StateTracker(TextLabel):
    get_state = None

    def add_state(self, get_state):
        self.get_state = get_state
        return self

    def update(self):
        data = self.get_state()

        self.write(data)

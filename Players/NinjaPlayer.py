import Config
from Animation import Animation
from Player import Player
from Screen import Screen
import pygame
from EventHandler import EventHandler


class NinjaPlayer(Player):
    """Первый игрок в игре, дочерний класс"""

    def __init__(self, position: tuple[int, int] = (0, 0),
                 dims: tuple[int, int] = Config.PLAYER_DIMS):
        super().__init__(position, dims)
        self.playerAnimations["moving"] = Animation(Config.Animations.NinjaPlayer.MOVING_TEXTURES,
                                                    dims=dims,
                                                    frame_rate=50)
        self.playerAnimations["idling"] = Animation(Config.Animations.NinjaPlayer.IDLING_TEXTURES,
                                                    dims=dims,
                                                    frame_rate=100)
        self.set_animation_state("idling")

    def update(self):
        super().update()

    def check_events(self):
        super().check_events()


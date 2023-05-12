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
        self.set_direction("right")
        self.set_state("idling")

    def update(self):
        super().update()

    def check_events(self):
        super().check_events()
        # print(123)
        ...
        # for event in EventHandler.get_events():
        #     if event.type == pygame.KEYDOWN:
        #         if event.key == pygame.K_LEFT:
        #             self.set_direction("left")
        #             self.set_state("moving")
        #             # self.rect.move(-EventHandler.get_dt() * self.playerSpeed, 0)
        #             self.motion = "left"
        #         elif event.key == pygame.K_RIGHT:
        #
        #             self.set_direction("right")
        #             self.set_state("moving")
        #             # self.rect.move(EventHandler.get_dt() * self.playerSpeed, 0)
        #             self.motion = "right"
        #     elif event.type == pygame.KEYUP:
        #         self.motion = "none"
        #         self.set_state("idling")
        #
        # if self.motion == "left":
        #     self.rect.x += -EventHandler.get_dt() * self.playerSpeed / 1000
        # elif self.motion == "right":
        #     self.rect.x += EventHandler.get_dt() * self.playerSpeed / 1000
        # else:
        #     ...
        ...

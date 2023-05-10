import Config
from Animation import Animation
from Player import Player
from Screen import Screen
import pygame
from EventHandler import EventHandler


class NinjaPlayer(Player):
    """первый игрок в игре, дочерний класс"""

    # блять я заебался писать, поэтому пишу хуёво, рефакторить буду потом

    def __init__(self, position: tuple[int, int] = (0, 0),
                 dims: tuple[int, int] = Config.PLAYER_DIMS):
        super().__init__(position, dims)
        self.playerAnimations["mooving"] = Animation(Config.Animations.NinjaPlayer.MOOVING_TEXTURES,
                                                     dims=dims,
                                                     frame_rate=100)
        self.set_direction("left")
        self.set_state("mooving")
        self.motion = "none"

    def update(self):
        prevState = self.currentState
        self.check_events()

        if self.currentState != prevState:
            self.get_animation_by_state(prevState).reset()

        self.set_image(self.get_animation_by_current_state().next_sprite())

    def check_events(self):
        # for event in EventHandler.get_events():
        #     if event.type == pygame.KEYDOWN:
        #         if event.key == pygame.K_LEFT:
        #             self.set_direction("left")
        #             self.set_state("mooving")
        #             # self.rect.move(-EventHandler.get_dt() * self.playerSpeed, 0)
        #             self.motion = "left"
        #         elif event.key == pygame.K_RIGHT:
        #
        #             self.set_direction("right")
        #             self.set_state("mooving")
        #             # self.rect.move(EventHandler.get_dt() * self.playerSpeed, 0)
        #             self.motion = "right"
        #     elif event.type == pygame.KEYUP:
        #         self.motion = "none"
        #
        # if self.motion == "left":
        #     self.rect.x += -EventHandler.get_dt() * self.playerSpeed / 1000
        # elif self.motion == "right":
        #     self.rect.x += EventHandler.get_dt() * self.playerSpeed / 1000
        # else:
        #     ...
        ...

import pygame
import Config
from Screen import Screen


class Interface:
    height: int = 0
    width: int = 0

    position: tuple[int, int] = (0, 0)

    texture_path: str = ""

    layer: int = 0

    group_function = lambda: None

    group = None

    normalize = Config.NORMALIZE

    def __init__(self, group=None):
        if self.normalize:
            self.do_normalize()

        # дальше вызов всех родительских инитов, ВАЖНО
        super().__init__()

    def do_normalize(self):
        self.width = (Screen.width / Config.DESIGN_WIDTH) * self.width
        self.height = (Screen.height / Config.DESIGN_HEIGHT) * self.height
        self.position = (Screen.width / Config.DESIGN_WIDTH) * self.position[0], \
            (Screen.height / Config.DESIGN_HEIGHT) * self.position[1]


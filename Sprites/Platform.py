import pygame
import random

from Group import Group
from Interface import Interface
from EventHandler import EventHandler
from Screen import Screen
from collections import deque
from Game import Game
from Colors import Colors


# ! платформы не маштабируются

# FIXME блять сука нахуй рефакторить это говно надо иниче игре пизда

class Platform(Interface, pygame.sprite.Sprite):
    # global x

    normalize = True

    def __init__(self, rand_pos: tuple[int, int], platform_rand_lenth: int, textures: dict[str, pygame.Surface]):
        self.platformLength = platform_rand_lenth
        """кол во центральных элементов в платформе"""

        self.textures = textures
        self.width, self.height = self.calculate_dims()
        self.position = rand_pos
        self.image = self.generate_platform_image()
        self.rect = pygame.Rect(self.position, (self.width, self.height))
        self.image.set_colorkey(Colors.BLACK)  # важная штука, которая убирает черный фон у платформ

        super().__init__()

    def calculate_dims(self) -> tuple[int, int]:
        """считает размеры платформы через длину текстур и платформы"""
        return ((self.textures["leftCorner"].get_size()[0] +
                 self.textures["rightCorner"].get_size()[0] +
                 self.textures["center"].get_size()[0] * self.platformLength),
                self.textures["center"].get_size()[1])

    def generate_platform_image(self) -> pygame.Surface:
        image = pygame.Surface((self.width, self.height))

        # отрисовка текстур в image

        image.blit(self.textures["leftCorner"], (0, 0))  # leftCorner
        image.blit(self.textures["rightCorner"],
                   (self.width - self.textures["rightCorner"].get_size()[0], 0))  # rightCorner

        for coordinates in range(
                self.textures["leftCorner"].get_size()[0],

                self.width - self.textures["center"].get_size()[0] - self.textures["rightCorner"].get_size()[0] + 1,

                self.textures["center"].get_size()[0]):  # center

            image.blit(self.textures["center"], (coordinates, 0))
        return image.convert_alpha()

    def update(self):
        """перемещение платформы"""
        self.rect.x -= EventHandler.get_dt() * Game.Platforms.speed / 1000
        self.position = (self.rect.x, self.rect.y)

    def out_of_screen(self) -> bool:
        """если платформа за экраном, то возвращает True"""
        return self.position[0] + self.width + 1 < 0


class PlatformGenerator(Interface):
    SIZE_SCALE = 4
    PLATFORM_CENTER_IMAGE = pygame.image.load('media/img/platformCenter.png')  # 25
    PLATFORM_LEFT_CORNER_IMAGE = pygame.image.load('media/img/platformLeftCorner.png')  # 6
    PLATFORM_RIGHT_CORNER_IMAGE = pygame.image.load('media/img/platformRightCorner.png')  # 6

    TIME_DELAY_MAX = 1000  # милисекунды
    TIME_DELAY_MIN = 500

    # подгрузка текстур и их увеличение
    PLATFORM_LEFT_CORNER_IMAGE = pygame.transform.scale(
        PLATFORM_LEFT_CORNER_IMAGE,
        (PLATFORM_LEFT_CORNER_IMAGE.get_size()[0] * SIZE_SCALE,
         PLATFORM_LEFT_CORNER_IMAGE.get_size()[1] * SIZE_SCALE,)
    ).convert_alpha()
    PLATFORM_CENTER_IMAGE = pygame.transform.scale(
        PLATFORM_CENTER_IMAGE,
        (PLATFORM_CENTER_IMAGE.get_size()[0] * SIZE_SCALE,
         PLATFORM_CENTER_IMAGE.get_size()[1] * SIZE_SCALE,)
    ).convert_alpha()
    PLATFORM_RIGHT_CORNER_IMAGE = pygame.transform.scale(
        PLATFORM_RIGHT_CORNER_IMAGE,
        (PLATFORM_RIGHT_CORNER_IMAGE.get_size()[0] * SIZE_SCALE,
         PLATFORM_RIGHT_CORNER_IMAGE.get_size()[1] * SIZE_SCALE,)
    ).convert_alpha()

    def __init__(self, all_sprites: pygame.sprite.LayeredUpdates):
        self.width = Screen.width
        self.height = Screen.height
        self.allSprites = all_sprites
        self.clock = pygame.time.Clock()
        self.platformGroup = pygame.sprite.Group()
        self.platformDeque: deque[Platform] = deque()
        self.delay = 0
        self.timer = 0

        super().__init__()

    def update(self):
        self.platformGroup.update()
        self.check_for_delete()
        self.tick()

        if self.timer >= self.delay:
            self.timer = 0
            self.set_delay()
            self.generate()

        # print(len(self.platformDeque))

    def generate(self):
        newPlatform = Platform((self.width, random.randint(0, self.height)), platform_rand_lenth=1, textures={
            "leftCorner": self.PLATFORM_LEFT_CORNER_IMAGE,
            "rightCorner": self.PLATFORM_RIGHT_CORNER_IMAGE,
            "center": self.PLATFORM_CENTER_IMAGE,
        })  # FIXME

        self.platformDeque.append(newPlatform)
        self.platformGroup.add(newPlatform)
        self.allSprites.add(self.platformGroup)

    def check_for_delete(self):
        """проверяет стоит ли удалять платформу"""

        while len(self.platformDeque) != 0 and (lastPlatform := self.platformDeque[0]).out_of_screen():
            lastPlatform.kill()
            self.platformDeque.popleft()

    def tick(self):
        self.timer += self.clock.tick()

    def set_delay(self):
        self.delay = random.randint(self.TIME_DELAY_MIN, self.TIME_DELAY_MAX)

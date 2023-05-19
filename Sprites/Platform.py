import pygame
import random

import Config
from Interface import Interface
from EventHandler import EventHandler
from Screen import Screen
from collections import deque
from Game import Game
from Colors import Colors


class Platform(Interface, pygame.sprite.Sprite):
    normalize = True

    def __init__(self, rand_pos: tuple[int, int], platform_rand_lentgh: int, textures: dict[str, pygame.Surface]):
        self.length = platform_rand_lentgh
        """кол во центральных элементов в платформе"""

        self.textures = textures
        self.width, self.height = self.calculate_dims()
        self.position = list(rand_pos)
        self.image = self.generate_platform_image()
        self.rect = pygame.Rect(self.position, (self.width, self.height))
        self.image.set_colorkey(Colors.BLACK)  # важная штука, которая убирает черный фон у платформ

        super().__init__()

    def calculate_dims(self) -> tuple[int, int]:
        """Считает размеры платформы через длину текстур и платформы"""
        return ((self.textures["leftCorner"].get_size()[0] +
                 self.textures["rightCorner"].get_size()[0] +
                 self.textures["center"].get_size()[0] * self.length),
                self.textures["center"].get_size()[1])

    def generate_platform_image(self) -> pygame.Surface:
        """Генерирует изображение платформы"""
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
        """Перемещение платформы"""
        self.position[0] -= EventHandler.get_dt() * Game.Platforms.speed / 1000
        self.rect.x, self.rect.y = self.position

    def out_of_screen(self) -> bool:
        """Если платформа за экраном, то возвращает True"""
        return self.position[0] + self.width + 1 < 0

    def intersect_left_border(self):
        """Пересекает ли платформа левую границу экрана"""
        return self.position[0] + self.width > Screen.width


class PlatformStream:
    nextPlatformDistance: int = 0
    """дистанция от экрана, до последней платформы"""

    platformDeque: deque[Platform]
    parentPlatform: Platform

    def __init__(self, gen_instance) -> None:
        self.genInstance = gen_instance
        self.update_next_platform_distance()
        self.platformDeque = deque()

        platform = self.genInstance.generate_platform(random.randint(
            self.genInstance.PLATFORM_Y_MIN,
            self.genInstance.PLATFORM_Y_MAX
        ), 4)  # FIXME бананы, это костыль
        self.genInstance.add_platform_to_intersection(platform)
        self.genInstance.add_platform_to_group(platform)
        self.genInstance.add_platform_to_sprites(platform)
        self.platformDeque.append(platform)
        self.parentPlatform = platform

    def update_next_platform_distance(self) -> None:
        self.nextPlatformDistance = Screen.width - random.randint(self.genInstance.MIN_DIST_BETWEEN_PLATFORM_OX,
                                                                  self.genInstance.MAX_DIST_BETWEEN_PLATFORM_OX)

    def update(self):
        self.generate()
        self.check_for_delete()

    def check_for_generate(self) -> bool:
        platform = self.platformDeque[-1]
        return platform.position[0] + platform.width <= self.nextPlatformDistance

    def get_parent_platform(self):
        return self.parentPlatform

    def add_parent_platform(self, platform):
        self.parentPlatform = platform

    def generate(self) -> None:
        if not self.check_for_generate():
            return

        i = 0
        while not self.genInstance.check_intersection((platform := self.genInstance.generate_platform(
                random.randint(
                    max(self.genInstance.PLATFORM_Y_MIN,
                        self.get_parent_platform().position[1] - self.genInstance.MAX_PLATFORM_OY_DIFF),
                    min(self.genInstance.PLATFORM_Y_MAX,
                        self.get_parent_platform().position[1] + self.genInstance.MAX_PLATFORM_OY_DIFF)
                ),
                self.genInstance.get_random_length(),
        ))) and i < self.genInstance.NUM_OF_GENERATIONS:
            i += 1

        if i == self.genInstance.NUM_OF_GENERATIONS:
            self.add_parent_platform(platform)
        else:
            self.genInstance.add_platform_to_intersection(platform)
            self.genInstance.add_platform_to_group(platform)
            self.genInstance.add_platform_to_sprites(platform)
            self.platformDeque.append(platform)

            EventHandler.push_to_stream("Platform", "generate", platform)
            # отправка события о создании

        self.update_next_platform_distance()

    def check_for_delete(self) -> None:
        """Проверяет, стоит ли удалять платформу"""
        while len(self.platformDeque) != 0 and (lastPlatform := self.platformDeque[0]).out_of_screen():
            lastPlatform.kill()
            self.platformDeque.popleft()


class PlatformGenerator(Interface):
    """Генератор платформ"""
    SIZE_SCALE = 4
    PLATFORM_CENTER_IMAGE = pygame.image.load('media/img/platformCenter.png')  # 25
    PLATFORM_LEFT_CORNER_IMAGE = pygame.image.load('media/img/platformLeftCorner.png')  # 6
    PLATFORM_RIGHT_CORNER_IMAGE = pygame.image.load('media/img/platformRightCorner.png')  # 6

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

    """Ограничение платформ по Oy в зависимости от размера игрока"""
    PLATFORM_Y_MIN = Config.PLAYER_DIMS[1] * 1.5 + Config.HUD_HEIGHT
    PLATFORM_Y_MAX = Screen.height - Config.PLAYER_DIMS[1] * 1.5

    """Ограничение длины платформ"""
    PLATFORM_LENGTH_MAX = 8
    PLATFORM_LENGTH_MIN = 2

    MIN_DIST_BETWEEN_PLATFORM_OY = Config.PLAYER_DIMS[1] * 2
    """Минимальная дистанция между сгенерированными платформами по Oy"""

    """Ограничение дистанции генерации по Ox"""
    MIN_DIST_BETWEEN_PLATFORM_OX = 100
    MAX_DIST_BETWEEN_PLATFORM_OX = 300

    """Ограничение разброса платформ"""
    MAX_PLATFORM_OY_DIFF = 500

    NUM_OF_GENERATIONS = 3
    """Количество попыток сгенерировать платформу"""

    platformStreams = []

    intersectLeftBorderPlatforms: list[Platform]

    def __init__(self, all_sprites: pygame.sprite.LayeredUpdates):
        self.allSprites = all_sprites
        self.clock = pygame.time.Clock()
        self.platformGroup = pygame.sprite.Group()
        self.intersectLeftBorderPlatforms = list()
        self.platformStreams = [PlatformStream(self), PlatformStream(self), PlatformStream(self)]

        super().__init__()

    def add_platform_to_intersection(self, platform: Platform) -> None:
        """Добавляет платформу в пересечение"""
        self.intersectLeftBorderPlatforms.append(platform)

    def update_intersection(self) -> None:
        """Обновляет пересечение"""
        self.intersectLeftBorderPlatforms = list(filter(lambda platform: platform.intersect_left_border(),
                                                        self.intersectLeftBorderPlatforms))

    def check_intersection(self, platform) -> bool:
        """Можно ли заспавнить эту платформу"""
        for xPlatform in self.intersectLeftBorderPlatforms:
            if xPlatform.rect.colliderect(
                    pygame.Rect(platform.rect.x, platform.rect.y - self.MIN_DIST_BETWEEN_PLATFORM_OY,
                                platform.rect.width, platform.rect.height + 2 * self.MIN_DIST_BETWEEN_PLATFORM_OY)):
                return False
        return True

    def get_random_length(self) -> int:
        return random.randint(self.PLATFORM_LENGTH_MIN, self.PLATFORM_LENGTH_MAX)

    def update(self) -> None:
        # обновление потоков
        for stream in self.platformStreams:
            stream.update()

        self.update_intersection()

    def generate_platform(self, y_cord, platform_length) -> Platform:
        """Генерирует платформу по заданной Y координате и длине"""
        newPlatform = Platform((Screen.width, y_cord), platform_rand_lentgh=platform_length, textures={
            "leftCorner": self.PLATFORM_LEFT_CORNER_IMAGE,
            "rightCorner": self.PLATFORM_RIGHT_CORNER_IMAGE,
            "center": self.PLATFORM_CENTER_IMAGE,
        })
        return newPlatform

    def add_platform_to_group(self, platform):
        """Добавление платформы в группу"""
        self.platformGroup.add(platform)

    def add_platform_to_sprites(self, platform):
        """Добавление платформы в спрайты"""
        self.allSprites.add(platform)

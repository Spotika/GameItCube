import pygame
import random

import Config
from Interface import Interface
from EventHandler import EventHandler
from Screen import Screen
from collections import deque
from Game import Game
from Colors import Colors


# FIXME платформы не маштабируются

class Platform(Interface, pygame.sprite.Sprite):
    normalize = True

    def __init__(self, rand_pos: tuple[int, int], platform_rand_lentgh: int, textures: dict[str, pygame.Surface]):
        self.platformLength = platform_rand_lentgh
        """кол во центральных элементов в платформе"""

        self.textures = textures
        self.width, self.height = self.calculate_dims()
        self.position = rand_pos
        self.image = self.generate_platform_image()
        self.rect = pygame.Rect(self.position, (self.width, self.height))
        self.image.set_colorkey(Colors.BLACK)  # важная штука, которая убирает черный фон у платформ

        super().__init__()

    def calculate_dims(self) -> tuple[int, int]:
        """Считает размеры платформы через длину текстур и платформы"""
        return ((self.textures["leftCorner"].get_size()[0] +
                 self.textures["rightCorner"].get_size()[0] +
                 self.textures["center"].get_size()[0] * self.platformLength),
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
        self.rect.x -= EventHandler.get_dt() * Game.Platforms.speed / 1000
        self.position = (self.rect.x, self.rect.y)

    def out_of_screen(self) -> bool:
        """Если платформа за экраном, то возвращает True"""
        return self.position[0] + self.width + 1 < 0


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
    PLATFORM_Y_MIN = Config.PLAYER_DIMS[1] * 1.5
    PLATFORM_Y_MAX = Screen.height - Config.PLAYER_DIMS[1] * 1.5

    """Ограничение длины платформ"""
    PLATFORM_LENGTH_MAX = 4
    PLATFORM_LENGTH_MIN = 1

    NEXT_PLATFORM_CHANCE = 0.5
    """Шанс на каждую последующую платформу"""

    MIN_DIST_BETWEEN_PLATFORM_OY = 100
    """Минимальная дистанция между сгенерированными платформами по Oy"""

    """Ограничение дистанции по Ox"""
    MIN_DIST_BETWEEN_PLATFORM_OX = 100
    MAX_DIST_BETWEEN_PLATFORM_OX = 300

    """Ограничение разброса платформ"""
    MIN_PLATFORM_OY_DIFF = 200
    MAX_PLATFORM_OY_DIFF = 400

    MAX_NUM_OF_PLATFORMS = 5
    """Максимальное количество платформ, которое может сгенерироваться единовременно"""

    nextPlatformDistance = 0
    """Расстояние до следующей сгенерируемой платформы"""

    parentPlatform = None
    """Родительская платформа"""

    def __init__(self, all_sprites: pygame.sprite.LayeredUpdates):
        self.allSprites = all_sprites
        self.clock = pygame.time.Clock()
        self.platformGroup = pygame.sprite.Group()
        self.platformDeque: deque[Platform] = deque()

        self.parentPlatform = self.generate_platform(random.randint(self.PLATFORM_Y_MIN,
                                                                    self.PLATFORM_Y_MAX), self.get_random_lenght())
        self.update_next_platform_distance()

        super().__init__()

    def update_next_platform_distance(self):
        """Обновляет nextPlatformDistance"""
        self.nextPlatformDistance = Screen.width - random.randint(self.MIN_DIST_BETWEEN_PLATFORM_OX,
                                                                  self.MAX_DIST_BETWEEN_PLATFORM_OX)

    def get_random_lenght(self):
        return random.randint(self.PLATFORM_LENGTH_MIN, self.PLATFORM_LENGTH_MAX)

    def update(self) -> None:
        self.platformGroup.update()
        self.check_for_delete()

        self.generate_platform_batch()

    def generate_platform_batch(self):
        """Генерирует группу платформ хитрым алгритмом"""
        if not self.check_for_generate():  # стоит ли генерировать
            return

        newPlatforms = []  # список новых пар для генерации (<координата> <длина>)

        """генерация случайного числа платформ с экспоненциальной вероятностью"""
        numOfPlatforms = 1  # количество сгенерированых платформ единовременно
        while numOfPlatforms < self.MAX_NUM_OF_PLATFORMS and random.random() <= self.NEXT_PLATFORM_CHANCE:
            numOfPlatforms += 1

        """тут погнали переменные для алгоритма"""
        d = random.randint(self.MIN_PLATFORM_OY_DIFF, self.MAX_PLATFORM_OY_DIFF)
        # минимальная дистанция между родительской и одной из сгенерированых платформ
        h = self.PLATFORM_Y_MAX - self.PLATFORM_Y_MIN
        # высота области генерации
        n = numOfPlatforms
        # количество сгенерированых платформ единовременно
        x = h // self.MAX_NUM_OF_PLATFORMS  # self.MIN_DIST_BETWEEN_PLATFORM_OY, можно заменять
        # минимальное расстояние между платформами
        k = random.randint((h - n * x) // (2 * n), (h - n * x) // n)
        # диапазон генерации платформы

        borderLine = self.parentPlatform.position[1]
        # линия генерации

        """две равновероятные ситуации генерации"""
        if random.random() <= 0.5:  # генерация сверху
            """Установка максимальной границы сверху"""
            c = 0  # просто счётчик
            while borderLine - d >= self.PLATFORM_Y_MIN and c < n:
                borderLine -= d
                c += 1

            """тут просто генерация и сдвиг границы вниз"""
            while n > 0 and borderLine + x <= self.PLATFORM_Y_MAX:
                newPlatforms.append(
                    (min(self.PLATFORM_Y_MAX, random.randint(borderLine - k, borderLine)), self.get_random_lenght())
                )
                n -= 1
                borderLine = newPlatforms[-1][0] + x
        else:  # генерация снизу
            """Установка максимальной границы снизу"""
            c = 0  # просто счётчик
            while borderLine + d <= self.PLATFORM_Y_MAX and c < n:
                borderLine += d
                c += 1

            """тут просто генерация и сдвиг границы вверх"""
            while n > 0 and borderLine >= self.PLATFORM_Y_MIN:
                newPlatforms.append(
                    (max(self.PLATFORM_Y_MIN, random.randint(borderLine, borderLine + k)), self.get_random_lenght())
                )
                n -= 1
                borderLine = newPlatforms[-1][0] - x

        nextParentPlatformNum = random.randint(0, len(newPlatforms))
        for i in range(len(newPlatforms)):
            newPlatform = self.generate_platform(*newPlatforms[i])
            if i == nextParentPlatformNum:
                self.parentPlatform = newPlatform

        self.update_next_platform_distance()

    def check_for_generate(self):
        """Проверка, стоит ли генерировать"""
        platform = self.platformDeque[-1]
        return platform.position[0] + platform.width <= self.nextPlatformDistance

    def generate_platform(self, y_cord, platform_length) -> Platform:
        """Генерирует платформу по заданной Y координате и длине"""
        newPlatform = Platform((Screen.width, y_cord), platform_rand_lentgh=platform_length,
                               textures={
                                   "leftCorner": self.PLATFORM_LEFT_CORNER_IMAGE,
                                   "rightCorner": self.PLATFORM_RIGHT_CORNER_IMAGE,
                                   "center": self.PLATFORM_CENTER_IMAGE,
                               })

        self.platformDeque.append(newPlatform)
        self.platformGroup.add(newPlatform)
        self.allSprites.add(self.platformGroup)
        return newPlatform

    def check_for_delete(self):
        """Проверяет, стоит ли удалять платформу"""
        while len(self.platformDeque) != 0 and (lastPlatform := self.platformDeque[0]).out_of_screen():
            lastPlatform.kill()
            self.platformDeque.popleft()

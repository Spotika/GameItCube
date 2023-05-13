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

class Platform(Interface, pygame.sprite.Sprite):
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
        """Считает размеры платформы через длину текстур и платформы"""
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
        """Перемещение платформы"""
        self.rect.x -= EventHandler.get_dt() * Game.Platforms.speed / 1000
        self.position = (self.rect.x, self.rect.y)

    def out_of_screen(self) -> bool:
        """Если платформа за экраном, то возвращает True"""
        return self.position[0] + self.width + 1 < 0


class PlatformGenerator(Interface):
    SIZE_SCALE = 4
    PLATFORM_CENTER_IMAGE = pygame.image.load('media/img/platformCenter.png')  # 25
    PLATFORM_LEFT_CORNER_IMAGE = pygame.image.load('media/img/platformLeftCorner.png')  # 6
    PLATFORM_RIGHT_CORNER_IMAGE = pygame.image.load('media/img/platformRightCorner.png')  # 6

    TIME_DELAY_MAX = 500  # милисекунды
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

    def update(self) -> None:
        """"""
        # TODO антону
        """
        придумай и реализуя нормальную генерацию платформ
        
        Требования к коду: 
        1) Пиши коментарии к каждому методу, который создаешь
        
        2) желательно пиши методы, функция self.update() не должна быть сложной, она лишь только собирает весь 
        функционал во едино
            
        3) если переменная константа или что-то фундаментальное пиши заглавными буквами
        
        4) если не очень ясно из названия переменной что конкретно она делает и для чего нужна, то пиши под ней 
        комментарий, состоящий из тройных скобочек, в котором объясни значение переменной в коде
        Пример:
        K_MAX = None
        '''что то о переменной'''
        
        Требования по задаче:
        0) Платформы должны генерироваться по случайной координате Y от MIN_Y_GEN до MAX_Y_GEN, X - ширина экрана.
        MIN_Y_GEN и MAX_Y_GEN - атрибуты класса которые нужно создать 
        
        1) платформы разной случайной длины, должны быть атрибуты, задающие макс и мин длину
        
        2) следующая платформа должна генерироваться только если её конец находится на каком-то случайном расстоянии от
        края экрана в диапозоне от MIN_GEN_DIST до MAX_GEN_DIST - атрибуты класса, которое нужно создать
        
        3) Назовём родительнской платформой ту которая на момент события генерации является последней
        (имеет наибольшую координату X), тогда первая, сгенерированная платформа не должна отличаться от
        родительской по координате Y больше чем на MAX_PARENT_Y_DIFF (атрибут класса), но быть
        
        4) Когда происходит событие генерации со 100% вероятностью генерируется 1 платформа, далее каждая платформа 
        может сгенерироваться с вероянтостью GEN_NEXT_PLATFORM_CHANCE. Каждая сгенерированая в одно событие генерации
        платформа не должна быть ближе к другим платформам чем на (MAX_Y_GEN - MIN_Y_GEN) / кол-во сгенерированых 
        платформ. 
        ^
        4.1) То есть тебе нужно сначала сгенерировать первую платформу по правилим пункта 3, затем
        определить кол-во платформ которые сгенерятся дополнительно, а потом как-то хитро распределить координаты между 
        ними так чтоб пункт 4 выполнилсяп
        
        
        Ну и некоторые полезные функции:
        1) Ты сам видел, что в классе Platform есть нужные тебе атрибуты, так что пользуйся ими
        2) В классе PlatformGenerator есть атрибут platformDeque - это очередь платформ, так вот что бы получить
        последнюю сгенерированую (родительскую) платформу напиши self.platformDeque[-1], если есть вопросы по ней
        загугли 'collections.deque python'
        
        ну тут вроде всё, а сам в ахуе, сколько написал, если что задавай вопросы в дс, тг, или ватсап 
        (дс не желательно, тк могу не ответить в срок)
        
        !если не получется то переходи по следующим ссылкам, они тебе обязательно помогут)))!
        1) https://youtu.be/bDHk0gwymqk
        2) https://www.youtube.com/watch?v=xvFZjo5PgG0
        
        """
        self.platformGroup.update()
        self.check_for_delete()
        self.tick()

        if self.timer >= self.delay:
            self.timer = 0
            self.set_delay()
            self.generate_platform()

    def generate_platform(self):
        newPlatform = Platform((self.width, random.randint(0, self.height)), platform_rand_lenth=random.randint(1, 3),
                               textures={
                                   "leftCorner": self.PLATFORM_LEFT_CORNER_IMAGE,
                                   "rightCorner": self.PLATFORM_RIGHT_CORNER_IMAGE,
                                   "center": self.PLATFORM_CENTER_IMAGE,
                               })  # FIXME тут переделай длину платформы

        self.platformDeque.append(newPlatform)
        self.platformGroup.add(newPlatform)
        self.allSprites.add(self.platformGroup)

    def check_for_delete(self):
        """Проверяет, стоит ли удалять платформу"""

        while len(self.platformDeque) != 0 and (lastPlatform := self.platformDeque[0]).out_of_screen():
            lastPlatform.kill()
            self.platformDeque.popleft()

    def tick(self):
        self.timer += self.clock.tick()

    def set_delay(self):
        self.delay = random.randint(self.TIME_DELAY_MIN, self.TIME_DELAY_MAX)

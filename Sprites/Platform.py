import pygame
import random
from Interface import Interface
from EventHandler import EventHandler
from Screen import Screen
# global x
# x = 0


class Platform(Interface, pygame.sprite.Sprite):
    # global x

    def __init__(self, randlen):
        self.len = randlen
        self.gran = 500
        self.image1 = pygame.image.load('media/img/platformCenter.png')  # 25
        self.image2 = pygame.image.load('media/img/platformLeftCorner.png')  # 6
        self.image3 = pygame.image.load('media/img/platformRightCorner.png')  # 6
        self.platformCord = 6
        self.surf = 12 + 25 * self.len, 6
        self.image = pygame.Surface(self.surf)
        self.image.blit(self.image2, (0, 0))
        for i in range(self.len):
            self.image.blit(self.image1, (self.platformCord, 0))  # создаёт платформу рандомной длинны
            self.platformCord += 25
        self.image.blit(self.image3, (self.platformCord, 0))
        self.image = pygame.transform.scale(self.image, (37 * 4 + self.platformCord, 6 * 4))
        self.rect = self.image.get_rect()
        self.x = 1600
        self.y = random.randint(self.gran - 100, self.gran + 100)
        self.rect.x = self.x
        self.rect.y = self.y
        self.flag = True
        self.width, self.height = Screen.width, Screen.height

        self.all_sprites = None

        super().__init__()

    def update(self):
        self.rect = self.rect.move(-(EventHandler.get_dt() * 0.2), 0)
        if self.rect.x < -list(self.surf)[0] * 3:
            self.all_sprites.remove(self)
        if self.rect.x < 1200 and self.flag:
            self.all_sprites.add(Platform(random.randint(1, 5)).set_all_sprites(self.all_sprites))
            self.gran = self.y
            if self.gran > 900:  # self.gran это граница чтобы можно было перепрыгнуть с плаьформы на платформу
                self.gran -= 100  # условие ограначевает эту границу
            if self.gran < 100:
                self.gran += 100
            self.flag = False

    def set_all_sprites(self, sprites):
        self.all_sprites = sprites
        return self

    def __del__(self):
        print('я ненавижу андрея')

#
#
# platforms = pygame.sprite.Group
# all_sprites = pygame.sprite.Group()
#
#
#
#
# Platform(random.randint(1, 5))

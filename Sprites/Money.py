import pygame
from .ImageLabel import ImageLabel
from EventHandler import EventHandler
import random
import Config
from Game import Game
from collections import deque


class Coin(ImageLabel):
    width = 24
    height = 27

    def __init__(self, position, platform, dims=(24, 27), texture_path=Config.COIN_IMAGE_PATH,
                 layer=40, player=None):
        self.player = player
        self.platform = platform
        super().__init__(position, dims, texture_path=texture_path, layer=layer)

    def collision_function(self, position):
        return self.rect.collidepoint(*position)

    def update(self):
        # перемещение монеты
        self.position[0] -= EventHandler.get_dt() * max(Game.Platforms.speed,
                                                        (Game.get_speed(Game.Platforms.speed,
                                                                        Game.EnvStats.get_any_attr()))) / 1000
        if self.platform.destroyed:
            self.kill()

        # коллизия с игроком
        if self.rect.colliderect(self.player.rect):
            self.kill()
            self.player.money += 1 * Game.MagicSpell.get_money_increase()

        if self.out_of_screen():
            self.kill()

        self.update_rect_by_pos()

    def out_of_screen(self):
        return self.position[0] + self.width + 1 < 0


class MoneyGenerator:
    HEIGHT_ABOVE_PLATFORM = 10
    """Высота монеток над платформой"""

    coinGroup: pygame.sprite.Group
    """Список монет"""

    allSprites: pygame.sprite.LayeredUpdates
    """аллспрайтс проиложения"""

    GENERATE_COIN_GROUP_CHANCE = 0.6
    """Шанс на генерацию монет на платформе"""

    GENERATE_NEXT_COIN_CHANCE = 0.8
    """Шанс сгенерировать следующую монету"""

    MAX_COINS_ON_DIST = 2
    """Макс монет на длигну платформы"""

    def __init__(self, all_sprites, platform_generator, player):
        self.coinGroup = pygame.sprite.Group()
        self.allSprites = all_sprites
        self.platformGenerator = platform_generator
        self.player = player

    def add_coin_to_group(self, coin):
        self.coinGroup.add(coin)

    def add_coin_to_sprites(self, coin):
        self.allSprites.add(coin)

    def generate_coin(self, position, platform):
        newCoin = Coin(position, platform, player=self.player)
        self.add_coin_to_sprites(newCoin)
        self.add_coin_to_group(newCoin)

    def generate(self, platform):

        if random.random() > self.GENERATE_COIN_GROUP_CHANCE:
            EventHandler.push_to_stream("MoneyGenerator", "platform_for_mob", platform)
            return

        numOfCoins = self.get_num_of_coins(platform.length)
        dx = platform.width / (numOfCoins + 1)
        xStart = platform.position[0] + dx
        for i in range(numOfCoins):
            self.generate_coin([xStart, platform.position[1] - self.HEIGHT_ABOVE_PLATFORM - Coin.height], platform)
            xStart += dx

    def get_num_of_coins(self, dist) -> int:
        """Возвращает случайное количество монет"""
        i = 1
        while random.random() < self.GENERATE_NEXT_COIN_CHANCE and i < (self.MAX_COINS_ON_DIST * dist):
            i += 1
        return i

    def update(self) -> None:
        """Обновляет генератор"""

        platform = EventHandler.get_from_stream("Platform", "generate")
        if platform is None:
            return

        self.generate(platform)

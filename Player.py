import pygame

from Animation import Animation
import Config
from Screen import Screen
from EventHandler import EventHandler
from Vector2D import Vector2D
import math


class Player(pygame.sprite.Sprite):
    """базовый класс игрока"""

    playerStates: list[str] = [
        "idling",
        "moving",
        "falling"
    ]
    """состояние игрока, например idling - простой, moving - движение"""

    playerDirection: str = "left"
    """ориентация модельки игрока"""

    currentState: str = "idling"
    """текущее состояние игрока"""

    playerAnimations: dict[str, Animation] = {
        "idling": Animation(),
        "moving": Animation(),
        "falling": Animation(),
    }
    """анимации, присущие каждому состоянию"""

    isLiving: bool = True
    """жив ли персонаж"""

    rect: pygame.Rect = pygame.Rect(0, 0, 0, 0)
    """объект рект персонажа"""

    image: pygame.Surface = pygame.Surface((0, 0))
    """объект image персонажа"""

    # тут векторные или физические величины для перемещения
    gravitationAcceleration = Vector2D(0, Config.G_CONSTANT)

    playerBaseAccelerationModule = Config.PLAYER_BASE_ACCELERATION_MODULE
    """базовое ускорение игрока"""

    playerBaseSpeedModule = Config.PLAYER_BASE_SPEED_MODULE
    """базовая скорость игрока"""

    playerSpeedVector: Vector2D = Vector2D()
    """вектор полной скорости персонажа"""

    playerAccelerationVector: Vector2D = Vector2D(0, 0) + gravitationAcceleration
    """вектор частичного ускорения персонажа"""

    MAX_PLAYER_SPEED_MODULE_X: float = Config.MAX_PLAYER_SPEED_MODULE_X
    """максимальный модуль скорости OX"""

    MAX_PLAYER_SPEED_MODULE_Y: float = Config.MAX_PLAYER_SPEED_MODULE_Y
    """максимальный модуль скорости OY"""

    MAX_PLAYER_ACCELERATION_MODULE_X: float = Config.MAX_PLAYER_ACCELERATION_MODULE_X
    """максимальный модуль ускорения OX"""

    MAX_PLAYER_ACCELERATION_MODULE_Y: float = Config.MAX_PLAYER_ACCELERATION_MODULE_Y
    """максимальный модуль ускорения OY"""

    currentmovingKey: int = None
    """текущая нажатая кнопка"""

    collisions: list[bool, bool, bool, bool]

    lastState = "idling"

    def __init__(self, position: tuple[int, int] = (0, 0), dims: tuple[int, int] = Config.PLAYER_DIMS) -> None:
        super().__init__()
        self.collisions = [False, False, False, False]
        self.do_normalize()
        self.rect = pygame.Rect(position, dims)

    def set_pos(self, x=None, y=None) -> None:
        if x is not None:
            self.rect.x = x
        if y is not None:
            self.rect.y = y

    def get_pos(self) -> tuple[int, int]:
        return self.rect.x, self.rect.y

    def get_dims(self) -> tuple[int, int]:
        return self.rect.width, self.rect.height

    def set_dims(self, dims: tuple[int, int]) -> None:
        self.rect.width, self.rect.height = dims

    def set_state(self, state: str) -> None:
        self.currentState = state

    def get_state(self) -> str:
        return self.currentState

    def set_direction(self, direction) -> None:
        self.playerDirection = direction

    def get_direction(self) -> str:
        return self.playerDirection

    def set_image(self, image):
        if self.get_direction() == "left":
            self.image = pygame.transform.flip(image, True, False)
        else:
            self.image = image
        self.set_dims(self.image.get_size())

    def get_rect(self) -> pygame.Rect:
        return self.rect

    def set_rect(self, rect) -> None:
        self.rect = rect

    def get_image(self) -> pygame.Surface:
        return self.image

    def do_normalize(self):
        """нормализует размерности игрока под экран"""
        self.rect.width = (Screen.width / Config.DESIGN_WIDTH) * self.rect.width
        self.rect.height = (Screen.height / Config.DESIGN_HEIGHT) * self.rect.height
        self.rect.x, self.rect.y = (Screen.width / Config.DESIGN_WIDTH) * self.rect.x, \
                                   (Screen.height / Config.DESIGN_HEIGHT) * self.rect.y

    def get_animation_by_current_state(self) -> Animation:
        return self.playerAnimations[self.currentState]

    def get_animation_by_state(self, state) -> Animation:
        return self.playerAnimations[state]

    def set_current_moving_key(self, key) -> None:
        self.currentmovingKey = key

    def get_current_moving_key(self) -> int:
        return self.currentmovingKey

    def update_animations(self) -> None:
        """TODO обновляет некоторые анимации по необходимости. Например изменяет фрейм рейт анимации"""

    def auto_set_state(self) -> str:
        """TODO автоматически обновляет состояние на основе координат, ускорений и скоростей.
        Возвращает предыдущее состояние"""
        ...

    def move(self, x=0, y=0):
        """сдвигает персонажа на какое то расстояние по Oy и Ox"""
        self.set_rect(self.rect.move(x, y))

    def calculate_vectors(self) -> None:
        """высчитывает вектора"""

        # TODO в рот я ебал баги короче не работает обработка переполнения
        # TODO сделать адекватную силу трения иначе перс как на катке

        # воздействие ускорения на скорость
        self.playerSpeedVector += self.playerAccelerationVector * (EventHandler.get_dt() / 1000)

        # обработка переполнения
        self.playerSpeedVector.x = min(self.MAX_PLAYER_SPEED_MODULE_X, self.playerSpeedVector.x)
        self.playerSpeedVector.y = min(self.MAX_PLAYER_SPEED_MODULE_X, self.playerSpeedVector.y)

        """если столкновения"""

        # c полом или потолком
        if self.collisions[2] or self.collisions[0]:
            self.playerAccelerationVector.y = 0
            self.playerSpeedVector.y = 0

    def move_by_vectors(self) -> None:
        """сдвиг персонажа"""
        # TODO персонаж не хочет двигаться на нецелое количество координат, поэтому нужно объявить атрибут позиции и через него всё сделать
        self.move(
            self.playerSpeedVector.x * EventHandler.get_dt() / 1000,
            self.playerSpeedVector.y * EventHandler.get_dt() / 1000
        )

    def check_collisions(self) -> list[bool, bool, bool, bool]:
        """проверяет столкновения и возвращает список где каждый элемент которого
        отвечает за сторону. Начало с верхней, дальше по часовой"""

        res = [False, False, False, False]

        """проверка коллизий с экраном"""
        """я не знаю, работает ли то, что если ты вышел за хитбокс, тебя отшвыривает обратно, поэтому:"""
        # TODO: добавить адекватную систему коллизий, которая работает не в тупую
        # верх
        res[0] = self.get_pos()[1] < 0
        if res[0]:
            self.set_pos(y=0)
        # низ
        res[2] = self.get_pos()[1] + self.get_dims()[1] > Screen.height
        if res[2]:
            self.set_pos(y=Screen.height - self.get_dims()[1])
        # лево
        res[3] = self.get_pos()[0] < 0
        if res[3]:
            self.set_pos(x=0)
        # право
        res[1] = self.get_pos()[0] + self.get_dims()[0] > Screen.width
        if res[1]:
            self.set_pos(x=Screen.width - self.get_dims()[0])

        return res

    def render_image(self) -> None:
        """устанавливает изображение"""
        self.set_image(self.get_animation_by_current_state().next_sprite())

    def update(self) -> None:
        """обновление для спрайта. если хочется переопределить, то вызывайте super"""

        print(self.playerSpeedVector)

        self.check_events()

        self.collisions = self.check_collisions()
        self.lastState = self.auto_set_state()

        self.calculate_vectors()
        self.move_by_vectors()

        self.update_animations()
        self.render_image()

    def check_events(self) -> None:
        """проверка событий, установка векторов. если хочется переопределить, то вызывайте super"""

        # TODO короче я уверен, что тут есть баги так что дебажить

        """пока только такое управление, можно добавить через K_DOWN соскальзывание с платформ"""
        for event in EventHandler.get_events():
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_UP:
                        # self.set_current_moving_key(pygame.K_UP)
                        self.playerSpeedVector += Vector2D(0, -2 * self.playerBaseSpeedModule)
                        self.playerAccelerationVector.y = self.gravitationAcceleration.y
                    case pygame.K_LEFT:
                        self.set_current_moving_key(pygame.K_LEFT)
                        self.set_direction("left")
                        self.set_state("moving")
                        self.playerAccelerationVector = Vector2D.from_polar(
                            math.pi,
                            self.playerBaseAccelerationModule) + self.gravitationAcceleration

                    case pygame.K_RIGHT:
                        self.set_current_moving_key(pygame.K_RIGHT)
                        self.set_direction("right")
                        self.set_state("moving")
                        self.playerAccelerationVector = Vector2D.from_polar(
                            0,
                            self.playerBaseAccelerationModule) + self.gravitationAcceleration

            elif event.type == pygame.KEYUP and event.key == self.get_current_moving_key():
                # остановка движения
                self.set_state("idling")
                print("stop")
                self.playerAccelerationVector.x = 0
        self.playerAccelerationVector.y = self.gravitationAcceleration.y

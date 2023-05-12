import pygame

from Animation import Animation
import Config
from App import App
from Screen import Screen
from EventHandler import EventHandler
from Vector2D import Vector2D
import math
import Scripts


class Player(pygame.sprite.Sprite):
    """Базовый класс игрока"""

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

    position: list[float, float]

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

    currentMovingKey: int = None
    """текущая нажатая кнопка"""

    collisionsWithEnv: list[bool, bool, bool, bool]
    """столкновение персонажа с окружающей средой по сторонам"""

    lastState = "idling"
    """предыдущее состояние"""

    app: App = None
    """ссылка на класс приложения, в котором игрок"""

    def __init__(self, position: tuple[int, int] = (0, 0), dims: tuple[int, int] = Config.PLAYER_DIMS) -> None:
        super().__init__()
        self.collisionsWithEnv = [False, False, False, False]
        self.do_normalize()
        self.rect = pygame.Rect(position, dims)
        self.position = list(position)

    def set_pos(self, x=None, y=None) -> None:
        if x is not None:
            self.position[0] = x
        if y is not None:
            self.position[1] = y

    def update_rect_position(self):
        """Обновляет координаты rect игрока"""
        self.rect.x, self.rect.y = self.position

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

    def get_image(self) -> pygame.Surface:
        return self.image

    def get_rect(self) -> pygame.Rect:
        return self.rect

    def set_rect(self, rect) -> None:
        self.rect = rect

    def get_app(self) -> App:
        return self.app

    def set_app(self, app) -> None:
        self.app = app

    def do_normalize(self):
        """Нормализует размерности игрока под экран"""
        self.rect.width = (Screen.width / Config.DESIGN_WIDTH) * self.rect.width
        self.rect.height = (Screen.height / Config.DESIGN_HEIGHT) * self.rect.height
        self.rect.x, self.rect.y = (Screen.width / Config.DESIGN_WIDTH) * self.rect.x, \
                                   (Screen.height / Config.DESIGN_HEIGHT) * self.rect.y

    def get_animation_by_current_state(self) -> Animation:
        return self.playerAnimations[self.currentState]

    def get_animation_by_state(self, state) -> Animation:
        return self.playerAnimations[state]

    def set_current_moving_key(self, key) -> None:
        self.currentMovingKey = key

    def get_current_moving_key(self) -> int:
        return self.currentMovingKey

    def update_animations(self) -> None:
        """TODO обновляет некоторые анимации по необходимости. Например изменяет фрейм рейт анимации"""

    def auto_set_state(self) -> str:
        """TODO автоматически обновляет состояние на основе координат, ускорений и скоростей.
        Возвращает предыдущее состояние"""
        ...

    def move(self, x: float = 0, y: float = 0):
        """сдвигает position на какое то расстояние по Oy и Ox"""
        self.position[0] += x
        self.position[1] += y

    def calculate_vectors(self) -> None:
        """Высчитывает вектора"""

        # TODO сделать адекватную силу трения иначе перс как на катке

        # воздействие ускорения на скорость
        self.playerSpeedVector += self.playerAccelerationVector * (EventHandler.get_dt() / 1000)

        # обработка переполнения
        self.playerSpeedVector.x = min(self.MAX_PLAYER_SPEED_MODULE_X,
                                       abs(self.playerSpeedVector.x)) * Scripts.sign(self.playerSpeedVector.x)
        self.playerSpeedVector.y = min(self.MAX_PLAYER_SPEED_MODULE_Y,
                                       abs(self.playerSpeedVector.y)) * Scripts.sign(self.playerSpeedVector.y)

        # """если модуль проекции меньше порогового значения, то он равен 0"""
        # if abs(self.playerSpeedVector.x) <= Config.MIN_SPEED_LIMIT:
        #     self.playerSpeedVector.x = 0
        # if abs(self.playerSpeedVector.y) <= Config.MIN_SPEED_LIMIT:
        #     self.playerSpeedVector.y = 0

    def move_by_vectors(self) -> None:
        """Сдвиг персонажа"""
        self.move(
            self.playerSpeedVector.x * EventHandler.get_dt() / 1000,
            self.playerSpeedVector.y * EventHandler.get_dt() / 1000
        )

        while any(collisions := self.check_env_collisions(self.position)):
            if collisions[0]:
                self.move(y=0.2)
                self.playerSpeedVector.y = 0
                self.playerAccelerationVector.y = 0
            if collisions[1]:
                self.move(x=-0.2)
                self.playerSpeedVector.x = 0
                self.playerAccelerationVector.x = 0
            if collisions[2]:
                self.move(y=-0.2)
                self.playerSpeedVector.y = 0
                self.playerAccelerationVector.y = 0
            if collisions[3]:
                self.move(x=0.2)
                self.playerSpeedVector.x = 0
                self.playerAccelerationVector.x = 0
        self.update_rect_position()

    # def check_position(self) -> bool:
    #     """Проверяет локальный атрибут position на соответствие условиям коллизий и иных ограничений"""
    #     # игрок не должен иметь коллизии с чем либо из среды
    #     return not any(self.check_env_collisions(self.position))  # [False, False, False, False]

    def render_image(self) -> None:
        """Устанавливает изображение"""
        self.set_image(self.get_animation_by_current_state().next_sprite())

    def check_env_collisions(self, position=None) -> list[bool, bool, bool, bool]:
        """Проверка коллизий с окружающей средой"""
        if position is None:
            position = self.get_pos()

        collisions = [False, False, False, False]

        """проверка коллизий с экраном"""
        # верх
        collisions[0] = position[1] < 0

        # низ
        collisions[2] = position[1] + self.get_dims()[1] > Screen.height

        # лево
        collisions[3] = position[0] < 0

        # право
        collisions[1] = position[0] + self.get_dims()[0] > Screen.width

        # FIXME Ну это прям дичь полная, но немного работает
        # TODO - починить
        platformGroup = self.get_app().platformGenerator.platformGroup

        for platform in platformGroup:
            platformRect = platform.rect
            if pygame.Rect(position, self.get_dims()).colliderect(platformRect):
                collisions[2] = True

        return collisions

    def generate_vectors_by_state(self):
        match self.get_state():

            case "moving":

                match self.get_direction():

                    case "left":
                        self.playerAccelerationVector = Vector2D.from_polar(
                            math.pi,
                            self.playerBaseAccelerationModule) + self.gravitationAcceleration
                    case "right":
                        self.playerAccelerationVector = Vector2D.from_polar(
                            0,
                            self.playerBaseAccelerationModule) + self.gravitationAcceleration

            case "idling":
                if abs(self.playerSpeedVector.x) <= Config.MIN_SPEED_LIM:
                    self.playerSpeedVector.x = 0
                    self.playerAccelerationVector.x = 0
                else:
                    self.playerAccelerationVector.x = -self.playerSpeedVector.x * Config.FRICTION_COEFFICIENT
        self.playerAccelerationVector.y = self.gravitationAcceleration.y

    def update(self) -> None:
        """Обновление для спрайта. Если хочется переопределить, то вызывайте super"""

        self.lastState = self.auto_set_state()

        self.check_events()
        self.generate_vectors_by_state()
        self.calculate_vectors()
        self.move_by_vectors()

        self.update_animations()
        self.render_image()

    def check_events(self) -> None:
        """Проверка событий, установка векторов. Если хочется переопределить, то вызывайте super"""

        """пока только такое управление, можно добавить через K_DOWN соскальзывание с платформ"""
        for event in EventHandler.get_events():
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_UP:
                        self.playerSpeedVector += Vector2D(0, -2 * self.playerBaseSpeedModule)

                    case pygame.K_LEFT:
                        self.set_current_moving_key(pygame.K_LEFT)
                        self.set_direction("left")
                        self.set_state("moving")

                    case pygame.K_RIGHT:
                        self.set_current_moving_key(pygame.K_RIGHT)
                        self.set_direction("right")
                        self.set_state("moving")

            elif event.type == pygame.KEYUP and event.key == self.get_current_moving_key():
                # остановка движения
                self.set_state("idling")

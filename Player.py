import pygame

from Animation import Animation
import Config
from Screen import Screen
from EventHandler import EventHandler
from Vector2D import Vector2D


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
    playerBaseAccelerationModule = Config.PLAYER_BASE_ACCELERATION_MODULE
    """базовое ускорение игрока"""

    playerBaseSpeedModule = Config.PLAYER_BASE_SPEED_MODULE
    """базовая скорость игрока"""

    playerSpeedVector: Vector2D = Vector2D()
    """вектор полной скорости персонажа"""

    playerAccelerationVector: Vector2D = Vector2D()
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

    def __init__(self, position: tuple[int, int] = (0, 0), dims: tuple[int, int] = Config.PLAYER_DIMS) -> None:
        super().__init__()
        self.do_normalize()
        self.rect = pygame.Rect(position, dims)

    def set_pos(self, position) -> None:
        self.rect.x, self.rect.y = position

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

    def update(self) -> None:
        """обновление для спрайта. если хочется переопределить, то вызывайте super"""
        self.check_events()
        self.move_by_vectors()

    def update_animations(self) -> None:
        """обновляет некоторые анимации по необходимости. Например изменяет фрейм рейт анимации"""

    def auto_set_state(self) -> bool:
        """автоматически обновляет состояние на основе координат, ускорений и скоростей. Возвращает True, если
        состояние изменилось"""
        ...

    def calculate_vectors(self) -> None:
        """высчитывает вектора"""

    def move_by_vectors(self) -> None:
        """сдвиг персонажа"""
        ...

    def check_events(self) -> None:
        """проверка событий, установка векторов. если хочется переопределить, то вызывайте super"""

        """пока только такое управление, можно добавить через K_DOWN соскальзывание с платформ"""
        for event in EventHandler.get_events():
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_UP:
                        # self.set_current_moving_key(pygame.K_UP)
                        ...
                    case pygame.K_LEFT:
                        self.set_current_moving_key(pygame.K_LEFT)
                        self.set_direction("left")
                    case pygame.K_RIGHT:
                        self.set_current_moving_key(pygame.K_RIGHT)
                        self.set_direction("right")
            elif event.type == pygame.KEYUP and event.key == self.get_current_moving_key():
                # остановка движения
                print("stop")

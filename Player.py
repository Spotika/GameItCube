import pygame

from Animation import Animation
import Config
from Screen import Screen
from EventHandler import EventHandler


class Player(pygame.sprite.Sprite):
    """базовый класс игрока"""

    playerStates: list[str] = [
        "idling",
        "mooving",
        "falling"
    ]
    """состояние игрока, например idling - простой, mooving - движение"""

    playerDirection: str = "left"
    """ориентация модельки игрока"""

    currentState: str = "idling"
    """текущее состояние игрока"""

    playerAnimations: dict[str, Animation] = {
        "idling": Animation(),
        "mooving": Animation(),
        "falling": Animation(),
    }
    """анимации, присущие каждому состоянию"""

    isLiving: bool = True
    """жив ли персонаж"""

    rect: pygame.Rect = pygame.Rect(0, 0, 0, 0)
    """объект рект персонажа"""

    image: pygame.Surface = pygame.Surface((0, 0))
    """объект image персонажа"""

    playerSpeed = 400
    """скорость игрока"""

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


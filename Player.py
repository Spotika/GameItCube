import pygame

from Animation import Animation
import Config


class Player(pygame.sprite.Sprite):
    playerStates: list[str] = []
    """состояние игрока, например idling - простой, mooving - движение"""

    playerDirection: str = "left"
    """ориентация модельки игрока"""

    currentState: str = None
    """текущее состояние игрока"""

    playerAnimations: dict[str, Animation] = {}
    """анимации, присущие каждому состоянию"""

    isLiving: bool = True
    """жив ли персонаж"""

    playerRect: pygame.Rect = pygame.Rect(0, 0, 0, 0)
    """объект рект персонажа"""

    def __init__(self, position: tuple[int, int] = (0, 0), dims: tuple[int, int] = Config.PLAYER_DIMS) -> None:
        super().__init__()
        self.playerRect = pygame.Rect(position, dims)

    def set_pos(self, position) -> None:
        self.playerRect.x, self.playerRect.y = position

    def get_pos(self) -> tuple[int, int]:
        return self.playerRect.x, self.playerRect.y

    def get_dims(self) -> tuple[int, int]:
        return self.playerRect.width, self.playerRect.height

    def set_dims(self, dims: tuple[int, int]) -> None:
        self.playerRect.width, self.playerRect.height = dims

    def set_state(self, state: str) -> None:
        self.currentState = state

    def get_state(self) -> str:
        return self.currentState

    def set_direction(self, direction) -> None:
        self.playerDirection = direction

    def get_direction(self) -> str:
        return self.playerDirection

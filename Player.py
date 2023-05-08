import pygame
import Config


class Player:
    """класс игрока как персонажа, объекты этого класса не создаются, тк в игре только 1 персонаж"""
    _PLAYER_STATES: list[str] = [
        "idling",  # игрок просто стоит на месте
        "falling",  # игрок находится в падении (не стоит на земле, но он может передвигаться по Ox без анимации)
        "mooving",  # игрок стоит на земле и передвигается по Ox
    ]
    """все возможные состояния игроки"""

    _DIRECTION: str = "left"
    """если 'left', то персонаж смотрит влево, 'right' - вправо"""

    _CURRENT_STATE: str = "idling"
    """текущее состояние игрока"""

    _PLAYER_SPRITES = None
    """анимации для каждого состояния из _PLAYER_STATES. устанавливается в дочернем классе"""

    living: bool = True
    """живой ли персонаж"""

    playerRect: pygame.Rect
    """объект pygame.Rect персонажа для отрисовки и провеки коллизий
    это основной атрибут игрока, так как здесь содержится информация о размере модельки и её положении
    получить размеры и позицию или изменить их можно с помощью методов `get_pos`, `set_pos`, `get_dims`, `set_dims`
    """

    @classmethod
    def init_player(cls, position: tuple[int, int] = (0, 0), dims: tuple[int, int] = Config.PLAYER_DIMS) -> None:
        cls.set_dims(dims)
        cls.set_pos(position)

    @classmethod
    def set_state(cls, state: str) -> None:
        """устанавлевает текущее состояние игрока, если такого состояние нет в
        списке состояний вызывает исключение"""
        if state not in cls._PLAYER_STATES:
            raise ValueError(f"Состояние {state} отсутствует в списке состояний игрока.\nВсе состояния: \
{', '.join(cls._PLAYER_STATES)}")
        else:
            cls._CURRENT_STATE = state

    @classmethod
    def get_state(cls) -> str:
        """возвращает текущее состояние игрока"""
        return cls._CURRENT_STATE

    @classmethod
    def get_pos(cls) -> tuple[int, int]:
        return cls.playerRect.x, cls.playerRect.y

    @classmethod
    def set_pos(cls, pos: tuple[int, int]) -> None:
        cls.playerRect.x, cls.playerRect.y = pos

    @classmethod
    def get_dims(cls) -> tuple[int, int]:
        return cls.playerRect.width, cls.playerRect.height

    @classmethod
    def set_dims(cls, dims: tuple[int, int]) -> None:
        cls.playerRect.width, cls.playerRect.height = dims

    @classmethod
    def get_direction(cls) -> str:
        """возвращает ориентацию персонажа"""
        return cls._DIRECTION

    @classmethod
    def set_direction(cls, direction) -> str:
        """возвращает ориентацию персонажа"""
        if direction in ["left", "right"]:
            cls._DIRECTION = direction
        else:
            raise ValueError("Неверный агрумент")

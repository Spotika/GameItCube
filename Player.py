import pygame

from Animation import Animation
import Config
from App import App
from Screen import Screen
from EventHandler import EventHandler
from Vector2D import Vector2D
import math
import Scripts
from typing import Any
from Game import Game


class Player(pygame.sprite.Sprite):
    """Базовый класс игрока"""

    """Статы игрока"""
    playerHealth: int = Config.PLAYER_MAX_HEALTH
    """Здоровье игрока"""
    playerMana: int = Config.PLAYER_MAX_MANA
    """Мана игрока"""

    """Дальше полная дичь"""

    PLAYER_STATE_NAMES: list[tuple[str, Any]] = None
    """все возможные имена состояний игрока и их значения по умолчанию (<имя>, <значение>)"""

    playerStates: dict[str, Any]
    """состояния игрока в JSON формате"""

    currentAnimationState: str = "idling"
    """текущее состояние анимации игрока"""

    playerAnimations: dict[str, Animation] = None
    """анимации, присущие каждому состоянию"""

    rect: pygame.Rect = pygame.Rect(0, 0, 0, 0)
    """объект рект персонажа"""

    image: pygame.Surface = pygame.Surface((0, 0))
    """объект image персонажа"""

    position: list[float, float]
    """позиция игрока"""

    # тут векторные или физические величины для перемещения
    gravitationAcceleration = Vector2D(0, Config.G_CONSTANT)

    playerBaseAccelerationModule = Config.PLAYER_BASE_ACCELERATION_MODULE
    """базовое ускорение игрока"""

    playerBaseSpeedModule = Config.PLAYER_BASE_SPEED_MODULE
    """базовая скорость игрока"""

    playerSpeedVector: Vector2D = Vector2D()
    """вектор скорости самого персонажа, которая не превышат определённых значений"""

    playerAdditionalSpeedVector: Vector2D = Vector2D()
    """вектор дополнительной скорости, которая может быть любой в отличие от playerSpeedVector"""

    playerAccelerationVector: Vector2D = Vector2D(0, 0) + gravitationAcceleration
    """вектор частичного ускорения персонажа"""

    MAX_PLAYER_SPEED_MODULE_X: float = Config.MAX_PLAYER_SPEED_MODULE_X
    """максимальный модуль скорости OX"""

    MAX_PLAYER_SPEED_MODULE_Y: float = Config.MAX_PLAYER_SPEED_MODULE_Y
    """максимальный модуль скорости OY"""

    collisionsWithEnv: list[bool, bool, bool, bool]
    """столкновение персонажа с окружающей средой по сторонам"""

    lastAnimationState = "idling"
    """предыдущее состояние анимации"""

    app: App = None
    """ссылка на класс приложения, в котором игрок"""

    collisionEnvFunctions: list
    """Список функций, обрабатывающйх столкновения"""

    def __init__(self, position: tuple[int, int] = (0, 0), dims: tuple[int, int] = Config.PLAYER_DIMS) -> None:
        super().__init__()
        self.rect = pygame.Rect(position, dims)
        self.do_normalize()

        """тут инициализация всех локальных ссылочных атрибутов атрибутов"""
        self.collisionsWithEnv = [False, False, False, False]
        self.position = list(position)
        self.playerAnimations = {
            "idling": Animation(),
            "moving": Animation(),
            "falling": Animation(),
        }
        # инициализация состояний
        self.PLAYER_STATE_NAMES = [
            ("direction", "right"),  # направление взгляда персонажа
            ("isLiving", True),  # жив ли персонаж
            ("currentMovingKey", None),  # текущая нажатая кнопка
            ("onPlatform", False),  # на платформе ли персонаж
        ]

        self.playerStates = {}
        self.load_states_from_names()
        self.layer = Config.PLAYER_LAYER
        self.collisionEnvFunctions = []

    def get_health(self) -> int:
        return self.playerHealth

    def get_mana(self) -> int:
        return self.playerMana

    # FIXME
    def update_mana(self, mana) -> None:
        self.playerMana += mana
        self.playerMana = min(self.playerMana, Config.PLAYER_MAX_MANA)
        self.playerMana = max(0, self.playerMana)

    def update_health(self, health) -> None:
        self.playerHealth += health
        self.playerHealth = min(self.playerHealth, Config.PLAYER_MAX_MANA)
        self.playerHealth = max(0, self.playerHealth)

    def add_to_collision_env_functions(self, function) -> None:
        """Добавляет функцию в список функций"""
        self.collisionEnvFunctions.append(function)

    def load_states_from_names(self):
        """Загружает в локальный атрибут playerStates значения из PLAYER_STATE_NAMES"""
        for name in self.PLAYER_STATE_NAMES:
            self.playerStates[name[0]] = name[1]

    def get_state_by_name(self, name: str) -> Any:
        """Возвращает состояние из playerStates по имени"""
        if name not in self.playerStates.keys():
            raise ValueError(f"Нет состояния с именем {name}")
        return self.playerStates[name]

    def set_state_by_name(self, name: str, state: Any) -> None:
        self.playerStates[name] = state

    def extend_state_names(self, names: tuple[str, Any] | list[tuple[str, Any]]):
        """Добавляет в атрибут PLAYER_STATE_NAMES другие имена и их значения"""
        if isinstance(names, tuple):
            self.PLAYER_STATE_NAMES.append(names)
        else:
            self.PLAYER_STATE_NAMES.extend(names)

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

    def set_animation_state(self, state: str) -> None:
        self.currentAnimationState = state

    def get_animation_state(self) -> str:
        return self.currentAnimationState

    def set_image(self, image):
        if self.get_state_by_name("direction") == "left":
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
        return self.playerAnimations[self.currentAnimationState]

    def get_animation_by_state(self, state) -> Animation:
        return self.playerAnimations[state]

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

        # воздействие ускорения на скорость
        self.playerSpeedVector += self.playerAccelerationVector * (EventHandler.get_dt() / 1000)

        # обработка переполнения
        self.playerSpeedVector.x = min(self.MAX_PLAYER_SPEED_MODULE_X,
                                       abs(self.playerSpeedVector.x)) * Scripts.sign(self.playerSpeedVector.x)
        self.playerSpeedVector.y = min(self.MAX_PLAYER_SPEED_MODULE_Y,
                                       abs(self.playerSpeedVector.y)) * Scripts.sign(self.playerSpeedVector.y)

        self.playerSpeedVector += self.playerAdditionalSpeedVector

    def move_by_vectors(self) -> None:
        """Сдвиг персонажа в соответствии с коллизиями"""
        self.move(
            self.playerSpeedVector.x * EventHandler.get_dt() / 1000,
            self.playerSpeedVector.y * EventHandler.get_dt() / 1000
        )

        self.playerSpeedVector -= self.playerAdditionalSpeedVector

        """
        Суть этой штуки в том, что если персонаж имеет столкновение с какой либо из сторон своего хит бокса,
        пока не перестанет существовать коллизий его будет сдвигать на 0.2 (значени взято с потолка, но оно
        должно быть < 1, так как могут появиться подёргивания) в противоположную от коллизий сторону. 
        Вроде работает
        """
        # TODO если это будет лагать, то нужно переделать на бин поиск
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
        # тут обновление позиции игрока
        self.update_rect_position()

    def render_image(self) -> None:
        """Устанавливает изображение"""
        self.set_image(self.get_animation_by_current_state().next_sprite())

    def check_env_collisions(self, position=None) -> list[bool, bool, bool, bool]:
        """Проверка коллизий с окружающей средой, тут все физические объекты"""
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

        """столкновения с платформами
        Идея такая: 
        1) если игрок имеет положительную по оси Oy скорость, то с платформой от столкнуться не может,
        2) если нижняя часть персонажа ниже верхней части платформы, то так же персонаж не может с ней столкнуться
        """
        platformGroup = self.get_app().platformGenerator.platformGroup  # получение группу платформ

        self.set_state_by_name("onPlatform", False)  # по умолчанию перс не на платформе

        for platform in platformGroup:  # цикл при переборе платформ
            platformRect = platform.rect  # рект платформы для проверки коллизий
            if self.playerSpeedVector.y >= 0 and position[1] < platformRect.y and \
                    position[1] + self.get_dims()[1] < platformRect.y + \
                    Config.PLAYER_DIFF_DIFF:  # Config.PLAYER_DIFF_DIFF - погрешность коллизий

                # проверка коллизий для состояния onPlatform
                """эта штука временно расширяет хитбокс персонажа на Config.PLAYER_DIFF_DIFF по оси Oy
                и проеверяет коллизию, если коллизия есть - перс на платформе
                """
                if pygame.Rect(position, (self.get_dims()[0],
                                          self.get_dims()[1] + Config.PLAYER_DIFF_DIFF)).colliderect(platformRect):
                    self.set_state_by_name("onPlatform", True)

                # проверка истинной коллизии
                if pygame.Rect(position, self.get_dims()).colliderect(platformRect):
                    collisions[2] = True
                    break

        """Проверка коллизий из списка"""
        for func in self.collisionEnvFunctions:
            collisions = Scripts.merge_collisions(collisions, func(position))

        return collisions

    def generate_vectors_by_state(self):
        """Генерирует векторы скоростей в зависимости от состояния"""
        self.playerAccelerationVector.y = self.gravitationAcceleration.y
        self.playerAdditionalSpeedVector.zero()
        match self.get_animation_state():

            case "moving":

                match self.get_state_by_name("direction"):

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

        # если перс на платформе, то в дополнительную скорость добавляется скорость платформ
        if self.get_state_by_name("onPlatform"):
            self.playerAdditionalSpeedVector.x = -Game.Platforms.speed  # не понимаю почему так, но так надо

    def update(self) -> None:
        """Обновление для спрайта. Если хочется переопределить, то вызывайте super"""

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
                        self.playerSpeedVector -= Vector2D(0, 2 * self.playerBaseSpeedModule)

                    case pygame.K_LEFT:
                        self.set_state_by_name("currentMovingKey", pygame.K_LEFT)
                        self.set_state_by_name("direction", "left")
                        self.set_animation_state("moving")

                    case pygame.K_RIGHT:
                        self.set_state_by_name("currentMovingKey", pygame.K_RIGHT)
                        self.set_state_by_name("direction", "right")
                        self.set_animation_state("moving")

                    case pygame.K_DOWN:
                        """соскальзывание с платформы"""
                        if self.get_state_by_name("onPlatform"):
                            self.position[1] += Config.PLAYER_DIFF_DIFF
                            self.playerSpeedVector += Vector2D(0, self.playerBaseSpeedModule // 2)

            elif event.type == pygame.KEYUP and event.key == self.get_state_by_name("currentMovingKey"):
                # остановка движения
                self.set_animation_state("idling")

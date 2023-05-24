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

    DAMAGE_DELAY = 100
    """Задержка между уроном"""
    damageTimer = 0

    """Свойства и переменные для игрока"""

    BASE_MANA: int = 0
    BASE_HEALTH: int = 100
    MAX_LEVEL: int = 30
    BASE_MANA_REGEN: int = 0.5
    BASE_HEALTH_REGEN: int = 0.1
    experience_for_next: int = Config.BASE_EXP_FOR_NEXT
    money: int = 0

    dexterity: int = 13
    strength: int = 17
    intelligence: int = 25

    dexterity_inc: int = 2
    strength_inc: int = 2
    intelligence_inc: int = 2

    mana: int = BASE_MANA
    health: int = 1
    level: int = 1
    experience: int = 0

    def get_max_jumps(self):
        return self.get_dexterity() * Config.DEXT_FOR_JUMP

    def update_stats(self):
        mm, mh = Game.get_mana_max(self.BASE_MANA, self.get_intelligence()), \
            Game.get_health_max(self.BASE_HEALTH, self.get_strength())

        self.mana = min(mm, self.mana + EventHandler.get_dt() / 1000 * Game.get_mana_regen(self.BASE_MANA_REGEN,
                                                                                           self.get_intelligence()))
        self.health = min(mh, self.health + EventHandler.get_dt() / 1000 * Game.get_health_regen(self.BASE_HEALTH_REGEN,
                                                                                                 self.get_strength()))

    def get_dexterity(self):
        return self.dexterity + self.get_level() * self.dexterity_inc

    def get_strength(self):
        return self.strength + self.get_level() * self.strength_inc

    def get_intelligence(self):
        return self.intelligence + self.get_level() * self.intelligence_inc

    def get_mana(self) -> int:
        return round(self.mana)

    def set_mana(self, value):
        self.mana = value

    def get_health(self) -> int:
        return round(self.health)

    def set_health(self, value):
        self.health = value

    def get_level(self) -> int:
        return self.level

    def set_level(self, value):
        self.level = value

    def get_money(self):
        return self.money

    """Ниже передвижение коллизии и визуал"""

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

    playerAdditionalSpeedVectors: dict[str, tuple[Vector2D, bool]]
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
        mm, mh = Game.get_mana_max(self.BASE_MANA, self.get_intelligence()), \
            Game.get_health_max(self.BASE_HEALTH, self.get_strength())
        self.mana = mm
        self.health = mh
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
            ("canJump", self.get_max_jumps())  # может ли прыгать
        ]
        self.playerAdditionalSpeedVectors = {}
        self.playerStates = {}
        self.load_states_from_names()
        self.layer = Config.PLAYER_LAYER
        self.collisionEnvFunctions = []
        self.add_speed("platform")

    def increase_level(self):
        self.level += 1

    def add_exp(self, exp):
        self.experience += exp

    def update_exp(self):
        if self.experience >= self.experience_for_next:
            self.experience %= self.experience_for_next
            self.increase_level()
            self.experience_for_next = Game.get_next_exp_for_lvl()

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

    def move(self, x: float = 0, y: float = 0):
        """сдвигает position на какое то расстояние по Oy и Ox"""
        self.position[0] += x
        self.position[1] += y

    def calculate_vectors(self) -> None:
        """Высчитывает вектора"""

        # обработка переполнения
        # воздействие ускорения на скорость
        """Теперь у героя нет полного ограничения на скорость, однако при привышении лимита
        ускорение перестаёт увеличивать скорость по модулю"""

        max_x = Game.get_speed(self.MAX_PLAYER_SPEED_MODULE_X, self.get_dexterity())

        self.playerSpeedVector.y += self.playerAccelerationVector.y * (EventHandler.get_dt() / 1000)
        self.playerSpeedVector.y = min(abs(self.MAX_PLAYER_SPEED_MODULE_Y),
                                       abs(self.playerSpeedVector.y)) * Scripts.sign(
            self.playerSpeedVector.y
        )
        # self.playerSpeedVector += self.playerAccelerationVector * (EventHandler.get_dt() / 1000)
        if abs(self.playerSpeedVector.x) > max_x:
            if Scripts.sign(self.playerSpeedVector.x) != Scripts.sign(self.playerAccelerationVector.x):
                self.playerSpeedVector.x += self.playerAccelerationVector.x * (EventHandler.get_dt() / 1000)
        else:
            self.playerSpeedVector.x += self.playerAccelerationVector.x * (EventHandler.get_dt() / 1000)

        self.playerSpeedVector.x = min(Config.REALY_MAX_BASE_SPEED,
                                       abs(self.playerSpeedVector.x)) * Scripts.sign(
            self.playerSpeedVector.x
        )

        # self.merge_speed_vectors()

    def move_by_vectors(self) -> None:
        """Сдвиг персонажа в соответствии с коллизиями"""
        self.move(
            (self.playerSpeedVector.x + self.get_speed_by_name("platform").x) * EventHandler.get_dt() / 1000,
            self.playerSpeedVector.y * EventHandler.get_dt() / 1000
        )

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

        # лево
        collisions[3] = position[0] < 0

        # право
        collisions[1] = position[0] + self.get_dims()[0] > Screen.width

        # проверка падения
        if position[1] > Screen.height:
            self.set_state_by_name("isLiving", False)

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
            self.set_state_by_name("canJump", self.get_max_jumps())
            self.add_speed("platform", x=-Game.get_speed(Game.Platforms.speed, Game.EnvStats.get_any_attr()))
        else:
            self.playerSpeedVector.x += self.get_speed_by_name("platform").x
            self.add_speed("platform")

    def update(self) -> None:
        """Обновление для спрайта. Если хочется переопределить, то вызывайте super"""
        if self.health < 1:
            # проверка смерти
            self.set_state_by_name("isLiving", False)

        self.update_exp()

        self.update_stats()
        self.check_events()
        self.generate_vectors_by_state()
        self.calculate_vectors()
        self.move_by_vectors()

        self.render_image()

    def check_events(self) -> None:
        """Проверка событий, установка векторов. Если хочется переопределить, то вызывайте super"""

        """пока только такое управление, можно добавить через K_DOWN соскальзывание с платформ"""
        for event in EventHandler.get_events():
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_UP:
                        if self.get_state_by_name("canJump") > 0:
                            self.playerSpeedVector -= Vector2D(0, 2 * (min(Config.REALY_MAX_BASE_SPEED,
                                                                           Game.get_speed(self.playerBaseSpeedModule,
                                                                                          self.get_dexterity()))))
                            d = 1
                            if self.get_state_by_name("onPlatform"):
                                d += 1
                            self.set_state_by_name("canJump", self.get_state_by_name("canJump") - d)

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

    def add_speed(self, name, x=0, y=0, merge=True) -> None:
        self.playerAdditionalSpeedVectors[name] = (Vector2D(x, y), merge)

    def get_speed_by_name(self, name) -> Vector2D:
        return self.playerAdditionalSpeedVectors[name][0]

    def merge_speed_vectors(self) -> None:
        """Сливает все векторы скоростей во едино и удаляет оставшиеся"""
        for speed in self.playerAdditionalSpeedVectors.values():
            if speed[1]:
                self.playerSpeedVector += speed[0]

        self.playerAdditionalSpeedVectors.clear()

    def get_full_speed(self) -> Vector2D:
        sp = Vector2D(*self.playerSpeedVector())
        for speed in self.playerAdditionalSpeedVectors.values():
            sp += speed[0]
        return sp

    def damage(self, value) -> None:
        """Наносит урон игроку"""
        if (ticks := EventHandler.get_ticks()) - self.damageTimer > self.DAMAGE_DELAY:
            self.health = max(0, self.health - value)
            self.damageTimer = ticks

    def merge_single_speed(self, speed: Vector2D):
        self.playerSpeedVector += speed

    def check_mana(self, mana):
        if self.mana < mana:
            return False
        self.mana -= mana
        return True

import pygame


class Label(pygame.sprite.Sprite):
    position: list[float, float]
    dims: list[float, float]
    _image: pygame.Surface
    rect: pygame.Rect

    isShow = True

    @property
    def image(self) -> pygame.Surface:
        """В зависимости от isShow может выдать обычное или пустое изобрвжение"""
        if self.isShow:
            return self._image
        return pygame.Surface((0, 0))

    @image.setter
    def image(self, value):
        self._image = value

    def __init__(self, position, dims, layer=50):
        super().__init__()
        self.position = list(position)
        self.dims = dims
        self.image = pygame.Surface(dims)
        self.rect = pygame.Rect(position, dims)
        self.layer = layer

    def set_image(self, image, transform=True) -> None:
        """Устанавливает image и маштабирует по необходимости"""
        if transform:
            self.image = pygame.transform.scale(image, self.dims)
        else:
            self.image = image
        self.image = self.image.convert_alpha()

    def set_rect(self, position) -> None:
        """Устанавливает rect x, y"""
        self.rect.x = position[0]
        self.rect.y = position[1]

    def update_rect_by_pos(self) -> None:
        """Обновляет rect позицией"""
        self.set_rect(self.position)

    def get_image(self) -> pygame.Surface:
        return self.image

    def get_rect(self) -> pygame.Rect:
        return self.rect

    def get_for_blit(self) -> tuple[pygame.Surface, pygame.Rect]:
        """Возвращает данные для блита на поверхность"""
        return self.get_image(), self.get_rect()

    def collision_function(self, position):
        """Проверка коллизий игрока с собой"""

    def set_pos(self, x=None, y=None) -> None:
        if x is not None:
            self.position[0] = x
        if y is not None:
            self.position[1] = y

    def set_dims(self, dims):
        self.dims = dims

    def move(self, x: float = 0, y: float = 0):
        """сдвигает position на какое то расстояние по Oy и Ox"""
        self.position[0] += x
        self.position[1] += y

    def update(self) -> None:
        ...

    def hide(self):
        """Скрывает лейбл"""
        self.isShow = False
        return self

    def show(self):
        """Показывает лейбл"""
        self.isShow = True
        return self


import pygame


class Label(pygame.sprite.Sprite):
    position: list[float, float]
    dims: list[float, float]
    image: pygame.Surface
    rect: pygame.Rect

    def __init__(self, position, dims, layer=50):
        super().__init__()
        self.position = position
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

    def set_rect(self, rect) -> None:
        """Устанавливает rect"""
        self.rect = rect

    def get_image(self) -> pygame.Surface:
        return self.image

    def get_rect(self) -> pygame.Rect:
        return self.rect

    def get_for_blit(self) -> tuple[pygame.Surface, pygame.Rect]:
        """Возвращает данные для блита на поверхность"""
        return self.get_image(), self.get_rect()

    def collision_function(self, position) -> list[bool]:
        """Проверка коллизий с собой"""

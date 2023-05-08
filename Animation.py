import pygame
from EventHandler import EventHandler


class Animation:
    """Класс для структурирывания и создания анимированых спрайтов на основе коллекции изображений"""

    SPRITES: list[pygame.Surface] = []
    """Список поверхностей анимации"""

    CURRENT_SPRITE = 0
    """Текущий номер спрайта анимации"""

    dims = None

    FRAME_RATE = 60
    """Скорость анимации в милисекундах"""

    now = EventHandler.get_ticks()
    """текущее кол во тиков"""

    def __init__(self, textures_file_path, dims=None, frame_rate=60):
        """инициализация текстурами"""
        self.FRAME_RATE = frame_rate
        for texture_path in textures_file_path:
            texture = pygame.image.load(texture_path).convert_alpha()  # тут подгрузка
            if dims is not None:
                texture = pygame.transform.scale(dims)
            self.SPRITES.append(texture)

    def next_sprite(self) -> pygame.Surface:
        """Возвращает спрайт и обновляет по времени счётчик спрайтов"""

        resImage = self.SPRITES[self.CURRENT_SPRITE]

        # если кол во прошедших тиков больше атрибута FRAME_RATE, то происходит шаг анимации
        if (ticks := EventHandler.get_ticks()) - self.now > self.FRAME_RATE:
            self.now = ticks
            self.CURRENT_SPRITE += 1  # увеличение счетчика
            self.CURRENT_SPRITE = self.CURRENT_SPRITE % len(self.SPRITES)  # взятие счетчика по модулю кол во спрайтов
        return resImage

    def reset(self) -> None:
        """обнуляет счетчик спрайтов"""
        self.CURRENT_SPRITE = 0

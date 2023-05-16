import pygame
from Label import Label


class SpriteModule(Label):
    design: dict[Label]
    """Дизайн модуля писать"""

    _layeredUpdates: pygame.sprite.LayeredUpdates
    """Для работы со слоями"""

    def set_design(self, design: dict) -> None:
        self.design = design
        self._layeredUpdates = pygame.sprite.LayeredUpdates()

    def add_to_layer_updates(self, sprite):
        self._layeredUpdates.add(sprite)

    def init_design(self) -> None:
        """Добавляет дизайн в _layeredUpdates"""
        for item in self.design.values():
            self.add_to_layer_updates(item)

    def update_image_by_design(self) -> None:
        """Обновляет изображение по дизайну"""
        self._layeredUpdates.draw(self.get_image())

    def update_design(self) -> None:
        """Обновляет дизайны"""
        self._layeredUpdates.update()

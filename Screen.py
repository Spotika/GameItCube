import pygame


class Screen:
    """базовые параметры ширины и высоты экрана, дальше изображение само будет подстраиваться под высоту"""
    # теперь 2 дисплея, на одном display рисуется обычная картинка под 1600 на 800
    # на другом все в конце отрисовывается и масштабируется

    displayDisplay = None
    width: int = 1600  # 1600

    height: int = 800  # 800

    displayWidth, displayHeight = 1600, 800

    display: pygame.Surface

    title: str = "GAY SEX 2: THE RETURN OF -=WAR THUNDER=-"

    allSprites = pygame.sprite.LayeredUpdates()

    def __new__(cls, *args, **kwargs):
        # Нельзя создать объект этого класса
        return None

    @classmethod
    def begin(cls):
        """init display and other"""
        cls.displayDisplay = pygame.display.set_mode((cls.displayWidth, cls.displayHeight), pygame.RESIZABLE)
        cls.display = pygame.Surface((cls.width, cls.height))
        pygame.display.set_caption(cls.title)

    @classmethod
    def update_display_dims(cls):
        cls.displayWidth = cls.displayDisplay.get_width()
        cls.displayHeight = cls.displayDisplay.get_height()

    @classmethod
    def update_display(cls):
        # FIXME
        cls.update_display_dims()
        cls.displayDisplay.fill((0, 0, 0))
        # cls.displayDisplay.blit(pygame.transform.scale(cls.display, (cls.displayWidth, cls.displayHeight)), (0, 0))
        cls.displayDisplay.blit(cls.display, (0, 0))
        pygame.display.update()

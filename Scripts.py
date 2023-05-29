import Config
from App import App
import importlib
import pygame
import math
from Colors import Colors


def link_apps_to_app():
    """Подключает все приложения из Config.INSTALLED_APPS"""
    for app_s in Config.INSTALLED_APPS:
        app = importlib.import_module(app_s)
        App.link(getattr(app, app_s.split(".")[-1]))


def sign(num):
    if num >= 0:
        return 1
    return -1


def scale_rect(rect: pygame.Rect, kx, ky) -> pygame.rect:
    return pygame.Rect((rect.x * kx, rect.y * ky), (rect.width * kx, rect.height * ky))


def merge_collisions(collision1: list[bool],
                     collision2: list[bool]) -> list[bool]:
    """Сливает два массива коллизий по принипу или"""
    res = []

    for i in range(len(collision1)):
        res.append((collision1[i] or collision2[i]))
    return res


def get_angle_between_points(pos1: tuple[float, float], pos2: tuple[float, float]) -> float:
    a = pos2[1] - pos1[1]
    b = -pos2[0] + pos1[0]
    if b == 0 or a == 0:
        return 0

    alpha = math.atan(a / b)
    if b < 0 and a < 0:
        alpha += math.pi
    elif b < 0:
        alpha += math.pi
    elif a < 0:
        alpha += math.pi * 2
    return alpha


def blit_color_by_precent(surface: pygame.Surface, precent: float, color=Colors.RED, opacity=100) -> pygame.Surface:
    """Заливает поверхность цветом на определённый процент"""

    precent = min(precent, 1)

    y = (1 - precent) * surface.get_height()

    chopRect = pygame.Rect((0, y), (surface.get_width(), surface.get_height() - y))
    # chopSurface = pygame.transform.chop(surface, chopRect)

    tSurface = surface.subsurface(chopRect).copy()
    tSurface.fill(color)
    tSurface.set_alpha(opacity)
    tSurface.convert_alpha()

    resSurface = surface.copy()
    resSurface.blit(tSurface, (0, y))
    resSurface.set_colorkey(color)

    return resSurface

import Config
from App import App
import importlib
import pygame
import math


def link_apps_to_app():
    """Подключает все приложения из Config.INSTALLED_APPS"""
    for app_s in Config.INSTALLED_APPS:
        app = importlib.import_module(app_s)
        App.link(getattr(app, app_s.split(".")[-1]))


def sign(num):
    if num >= 0:
        return 1
    return -1


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

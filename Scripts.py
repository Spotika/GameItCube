import Config
from App import App
import importlib


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

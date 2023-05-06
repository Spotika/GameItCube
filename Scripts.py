import Config
from App import App
import importlib


def link_apps_to_app():
    """Подключает все приложения из Config.INSTALLED_APPS"""
    for app_s in Config.INSTALLED_APPS:
        app = importlib.import_module(app_s)
        App.link(getattr(app, app_s.split(".")[-1]))

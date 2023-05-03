import pygame
from Screen import *


class App:
    running: bool = True

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def begin(cls):
        ...

    @classmethod
    def end(cls):
        ...

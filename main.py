import pygame
pygame.init()

from Screen import Screen
Screen.begin() # для инициализации видео системы

from Interface import Interface
from App import App
from Apps.MainMenuApp import MainMenuApp
import Scripts
from Game import Game
import time
from QueryDeque import QueryDeque

def main():
    pygame.mixer.music.set_volume(Game.Audio.volume) # установка громкости
    Scripts.link_apps_to_app() # прикрепление приложений к из родителю

    beginApp = MainMenuApp # тут приложение с которого стартуем
    QueryDeque.add(beginApp)
    while not QueryDeque.is_empty():
        QueryDeque.do_next()


if __name__ == '__main__':
    main()
    time.sleep(0.2)
    exit(0)

import pygame
pygame.init()

from Screen import Screen
Screen.begin() # for init video sustem

from Interface import Interface
from App import App
from Apps.MainMenuApp import MainMenuApp
import Scripts
from Game import Game
import time

def main():

    pygame.mixer.music.set_volume(Game.Audio.volume)
    Scripts.link_apps_to_app()
    MainMenuApp.begin()


if __name__ == '__main__':
    main()
    exit(0)

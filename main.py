import pygame
from Screen import Screen
Screen.begin() # for init video sustem

from Interface import Interface
from App import App
from Apps.MainMenuApp import MainMenuApp
import Scripts

def main():
    Scripts.link_apps_to_app()
    MainMenuApp.begin()


if __name__ == '__main__':
    main()
    exit(0)

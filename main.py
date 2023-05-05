import pygame
from Interface import Interface
from App import App
from Screen import Screen
from Apps.MainMenuApp import MainMenuApp


def main():
    Screen.begin()  # init
    MainMenuApp.begin()


if __name__ == '__main__':
    main()
    exit(0)

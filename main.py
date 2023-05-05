import pygame
from Interface import *
from App import *
from Screen import *
from Apps.MainMenuApp import *



def main():
    Screen.begin()  # init
    MainMenuApp.begin()


if __name__ == '__main__':
    main()
    exit(0)

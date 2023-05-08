# files
BACK_GROUND_IMG_FILE_PATH = "media/img/BackGround.png"
PLATFORM_LEFT_CORNER = "media/img/platformLeftCorner.png"
PLATFORM_RIGHT_CORNER = "media/img/platformRightCorner.png"
PLATFORM_CENTER = "media/img/platformCenter.png"
SOLID_WHITE_TEXTURE = "media/img/solidWhite.png"
GAME_LOGO = "media/img/gameLogo.png"

# Layers
BACK_GROUND_SPRITE_LAYER = -50
BUTTON_SPRITE_LAYER = 50
MASK_LAYER = 100


# misc
FPS = 60
DESIGN_WIDTH = 1600
"""ширина дизайна"""
DESIGN_HEIGHT = 800
"""высота дизайна"""


NORMALIZE = True
"""будут ли элементы маштабироваться"""


INSTALLED_APPS = [
    "Apps.MainGameApp",
    "Apps.MainMenuApp"
]
"""Добавбь сюда свое приложение и оно будет доступно для редиректа в него \n(!) сувать путь до модуля относительно
main.py"""

PLAYER_DIMS = (20, 45)


class BackGroundTextures:
    BACKGROUND_JUNGLE_LAYERS = [
        "media/img/background/jungle/plx-5.png",
        "media/img/background/jungle/plx-4.png",
        "media/img/background/jungle/plx-3.png",
        "media/img/background/jungle/plx-2.png",
        "media/img/background/jungle/plx-1.png",
    ]
    BACKGROUND_FOREST_LAYERS = [
        "media/img/background/forest/Layer_0000_9.png",
        "media/img/background/forest/Layer_0001_8.png",
        "media/img/background/forest/Layer_0002_7.png",
        "media/img/background/forest/Layer_0003_6.png",
        "media/img/background/forest/Layer_0004_Lights.png",
        "media/img/background/forest/Layer_0005_5.png",
        "media/img/background/forest/Layer_0006_4.png",
        "media/img/background/forest/Layer_0007_Lights.png",
        "media/img/background/forest/Layer_0008_3.png",
        "media/img/background/forest/Layer_0009_2.png",
        "media/img/background/forest/Layer_0010_1.png",
        "media/img/background/forest/Layer_0011_0.png"
    ]


class Audio:
    BUTTON_CLICKED_SFX = "media/audio/minecraftButtonSfx.mp3"


class ButtonTextures:
    START_BUTTON_IMG_FILE_PATH = "media/img/buttonTextures/startButton.png"
    EXIT_BUTTON_IMG_FILE_PATH = "media/img/buttonTextures/exitButton.png"
    SETTINGS_BUTTON_IMG_FILE_PATH = "media/img/buttonTextures/settingsButton.png"
    GIT_BUTTON = "media/img/buttonTextures/gitButton.png"


class PlayerTextures:
    PLAYER1_TEXTURE = "media/img/playerTextures/playerTexture1.png"

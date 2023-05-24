# files
BACK_GROUND_IMG_FILE_PATH = "media/img/BackGround.png"
PLATFORM_LEFT_CORNER = "media/img/platformLeftCorner.png"
PLATFORM_RIGHT_CORNER = "media/img/platformRightCorner.png"
PLATFORM_CENTER = "media/img/platformCenter.png"
SOLID_WHITE_TEXTURE = "media/img/solidWhite.png"
GAME_LOGO = "media/img/gameLogo.png"
HEART_IMAGE_PATH = "media/img/heart.png"
CLARITY_IMAGE_PATH = "media/img/clarity.png"
STRENGTH_IMAGE_PATH = "media/img/interface/strength.png"
DEXTERITY_IMAGE_PATH = "media/img/interface/dexterity.png"
INTELLIGENCE_IMAGE_PATH = "media/img/interface/intelligence.png"
PLAYER_MAX_HEALTH = 100
PLAYER_MAX_MANA = 50
SPELL_SLOT_IMAGE_PATH = "media/img/interface/spell_slot.png"
MONEY_IMAGE_PATH = "media/img/interface/money.png"
LEVEL_SLOT_IMAGE_PATH = "media/img/interface/level_slot.png"
COIN_IMAGE_PATH = "media/img/interface/coin.png"

# Layers
BACK_GROUND_SPRITE_LAYER = -50
BUTTON_SPRITE_LAYER = 50
MASK_LAYER = 100
PLAYER_LAYER = 60
PLAYER_DIFF_DIFF = 10
HUD_LAYER = 99
HUD_HEIGHT = 80
HUD_BACK_TEXTURE = "media/img/interface/HudBack.png"

# misc
FPS = 120
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

PLAYER_DIMS = (34, 48)


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


# TODO: подкоректировать эти штуки
FRICTION_COEFFICIENT = 4
"""нормальный коеэффициент трения"""
MAX_PLAYER_SPEED_MODULE_X: float = 50
MAX_PLAYER_SPEED_MODULE_Y: float = 600
MAX_PLAYER_ACCELERATION_MODULE_X: float = 1000
MAX_PLAYER_ACCELERATION_MODULE_Y: float = 1000
PLAYER_BASE_ACCELERATION_MODULE: float = 10000
PLAYER_BASE_SPEED_MODULE: float = 150
REALY_MAX_BASE_SPEED = 1000
G_CONSTANT: float = 800
MIN_SPEED_LIM: float = 20

BASE_EXP_FOR_NEXT = 50

STATE_BY_MONEY = 0.07
"""атрибут за монету"""


class Audio:
    BUTTON_CLICKED_SFX = "media/audio/minecraftButtonSfx.mp3"


class ButtonTextures:
    START_BUTTON_IMG_FILE_PATH = "media/img/buttonTextures/startButton.png"
    EXIT_BUTTON_IMG_FILE_PATH = "media/img/buttonTextures/exitButton.png"
    SETTINGS_BUTTON_IMG_FILE_PATH = "media/img/buttonTextures/settingsButton.png"
    GIT_BUTTON = "media/img/buttonTextures/gitButton.png"


class PlayerTextures:
    PLAYER1_TEXTURE = "media/img/playerTextures/playerTexture1.png"


class Animations:
    class NinjaPlayer:
        MOVING_TEXTURES = [
            "media/img/animations/NinjaPlayer/mooving/0.png",
            "media/img/animations/NinjaPlayer/mooving/1.png",
        ]
        IDLING_TEXTURES = [
            "media/img/animations/NinjaPlayer/idling/0.png",
        ]

    class BoarMob:
        CASUAL_TEXTURES = [
            "media/img/mobs/kaban.png"
        ]

    SHURIKEN_FRAMES = [
        "media/img/animations/Shuriken/0.png",
        "media/img/animations/Shuriken/1.png",
        "media/img/animations/Shuriken/2.png",
        "media/img/animations/Shuriken/3.png"
    ]


BOAR_DIMS = (73, 49)
SHURIKEN_ATTACK_SPELL_TEXTURE_PATH = "media/img/spells/shurikenAttack.png"
DODGE_SPELL_TEXTURE_PATH = "media/img/spells/dodgeSpell.png"
SHURIKEN_DIMS = (18 * 2, 17 * 2)

DEXT_FOR_JUMP = (1 / 150)

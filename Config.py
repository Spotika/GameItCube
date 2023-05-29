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
PLAYER_DIFF_DIFF = 15
HUD_LAYER = 1000000
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
    "Apps.MainMenuApp",
    "Apps.PauseApp",
    "Apps.EndApp",
    "Apps.InfoApp",
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

STATE_BY_MONEY = 0.08
"""атрибут за монету"""


class Audio:
    BUTTON_CLICKED_SFX = "media/audio/minecraftButtonSfx.mp3"


class ButtonTextures:
    START_BUTTON_IMG_FILE_PATH = "media/img/buttonTextures/startButton.png"
    EXIT_BUTTON_IMG_FILE_PATH = "media/img/buttonTextures/exitButton.png"
    INFO_BUTTON_FILE_PATH = "media/img/buttonTextures/infoButton.png"
    GIT_BUTTON = "media/img/buttonTextures/gitButton.png"
    BACK_BUTTON_FILE_PATH = "media/img/buttonTextures/backButton.png"


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
MAGIC_SPELL_TEXTURE = "media/img/spells/magicSpell.png"
DEXT_FOR_JUMP = (1 / 50)


class Boss:
    class FireBoss:
        IDLING_TESTURES = [
            "media/img/animations/FireBoss/idling/pixil-frame-0.png",
            "media/img/animations/FireBoss/idling/infoButton.png",
        ]
        PREPARING_TEXTURES = [
            "media/img/animations/FireBoss/idling/pixil-frame-0.png",
        ]
        IDLING_DIMS = (73 * 3, 79 * 3)
        PREPARING_DIMS = (73 * 3, 79 * 3)

    class PoisonBoss:
        IDLING_TESTURES = [
            "media/img/animations/PoisonBoss/idling/0.png",
            "media/img/animations/PoisonBoss/idling/1.png",
            "media/img/animations/PoisonBoss/idling/2.png",
            "media/img/animations/PoisonBoss/idling/3.png",
        ]
        PREPARING_TEXTURES = [
            "media/img/animations/PoisonBoss/preparing/pixil-frame-2.png",
            "media/img/animations/PoisonBoss/preparing/pixil-frame-3.png",
            "media/img/animations/PoisonBoss/preparing/pixil-frame-4.png",
            "media/img/animations/PoisonBoss/preparing/pixil-frame-5.png",
            "media/img/animations/PoisonBoss/preparing/pixil-frame-6.png",
            "media/img/animations/PoisonBoss/preparing/pixil-frame-7.png",
            "media/img/animations/PoisonBoss/preparing/pixil-frame-8.png",
            "media/img/animations/PoisonBoss/preparing/pixil-frame-9.png",
            "media/img/animations/PoisonBoss/preparing/pixil-frame-10.png",
            "media/img/animations/PoisonBoss/preparing/pixil-frame-11.png",
            "media/img/animations/PoisonBoss/preparing/pixil-frame-12.png",
            "media/img/animations/PoisonBoss/preparing/pixil-frame-13.png",
            "media/img/animations/PoisonBoss/preparing/pixil-frame-14.png",
            "media/img/animations/PoisonBoss/preparing/pixil-frame-15.png",
            "media/img/animations/PoisonBoss/preparing/pixil-frame-16.png",
            "media/img/animations/PoisonBoss/preparing/pixil-frame-17.png",
            "media/img/animations/PoisonBoss/preparing/pixil-frame-18.png",
        ]
        IDLING_DIMS = (55 * 3, 50 * 3)
        PREPARING_DIMS = (300, 300)
        ATTACK = ["media/img/animations/PoisonBoss/attack.png"]
        ATTACK_DIMS = (6 * 5, 9 * 5)


class Meteor:
    METEOR_DIMS = (32 * 10, 32 * 10)
    speed = 400
    TYPE_TEXTURES = {
        "LD": [
            "media/img/animations/meteor/LD/_56.png",
            "media/img/animations/meteor/LD/_57.png",
            "media/img/animations/meteor/LD/_58.png",
            "media/img/animations/meteor/LD/_59.png",
            "media/img/animations/meteor/LD/_60.png",
            "media/img/animations/meteor/LD/_61.png",
            "media/img/animations/meteor/LD/_62.png",
            "media/img/animations/meteor/LD/_63.png",
        ],
        "RD": [
            "media/img/animations/meteor/RD/_40.png",
            "media/img/animations/meteor/RD/_41.png",
            "media/img/animations/meteor/RD/_42.png",
            "media/img/animations/meteor/RD/_43.png",
            "media/img/animations/meteor/RD/_44.png",
            "media/img/animations/meteor/RD/_45.png",
            "media/img/animations/meteor/RD/_46.png",
            "media/img/animations/meteor/RD/_47.png",
        ],
        "D": [
            "media/img/animations/meteor/D/_48.png",
            "media/img/animations/meteor/D/_49.png",
            "media/img/animations/meteor/D/_50.png",
            "media/img/animations/meteor/D/_51.png",
            "media/img/animations/meteor/D/_52.png",
            "media/img/animations/meteor/D/_53.png",
            "media/img/animations/meteor/D/_54.png",
            "media/img/animations/meteor/D/_55.png",
        ],
        "R": [
            "media/img/animations/meteor/R/_32.png",
            "media/img/animations/meteor/R/_33.png",
            "media/img/animations/meteor/R/_34.png",
            "media/img/animations/meteor/R/_35.png",
            "media/img/animations/meteor/R/_36.png",
            "media/img/animations/meteor/R/_37.png",
            "media/img/animations/meteor/R/_38.png",
            "media/img/animations/meteor/R/_39.png",
        ],
        "L": [
            "media/img/animations/meteor/L/_0.png",
            "media/img/animations/meteor/L/_1.png",
            "media/img/animations/meteor/L/_2.png",
            "media/img/animations/meteor/L/_3.png",
            "media/img/animations/meteor/L/_4.png",
            "media/img/animations/meteor/L/_5.png",
            "media/img/animations/meteor/L/_6.png",
            "media/img/animations/meteor/L/_7.png",
        ]
    }


INFO_IMAGE = "media/img/info.png"

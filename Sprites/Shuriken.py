import pygame
from Label import Label
from Animation import Animation
import Config
from EventHandler import EventHandler
from Game import Game
from Screen import Screen


class Shuriken(Label):
    direction = None
    """Направление движения"""

    animation = None
    """анимация"""

    mobs = None

    added_speed = 0

    @classmethod
    def link_mobs(cls, mobs):
        cls.mobs = mobs

    def __init__(self, position, direction, dims=Config.SHURIKEN_DIMS, layer=100, ):
        super().__init__(position, dims, layer)
        self.added_speed = EventHandler.DataStash.player.get_full_speed().x
        self.move(y=Config.PLAYER_DIMS[1] / 4)
        self.direction = direction
        self.animation = Animation(textures_file_path=Config.Animations.SHURIKEN_FRAMES, dims=(18, 17), frame_rate=75)
        self.d = 1
        if self.direction == "left":
            self.set_image(pygame.transform.flip(self.image, True, False))
            self.d = -1

    def update(self) -> None:
        self.set_image(self.animation.next_sprite())

        speed = (Game.get_speed(Game.Shuriken.speed, EventHandler.DataStash.player.get_dexterity()) + \
                 self.d * self.added_speed)
        self.move(x=self.d * EventHandler.get_dt() * speed / 1000)
        self.update_rect_by_pos()

        # коллизия с мобами
        collide = pygame.sprite.spritecollide(self, EventHandler.DataStash.mobGenerator.mobGroup, False)
        for mob in collide:
            mob.damage_from(self, Game.get_damage(
                Game.Shuriken.damage, EventHandler.DataStash.player.get_strength(),
                increase=speed / Game.get_speed(Game.Shuriken.speed,
                                                EventHandler.DataStash.player.get_dexterity())))

        bossCollide = pygame.sprite.spritecollide(self, EventHandler.DataStash.bossGenerator.bossGroup, False)
        for boss in bossCollide:
            boss.damage_from(self, Game.get_damage(
                Game.Shuriken.damage, EventHandler.DataStash.player.get_strength(),
                increase=speed / Game.get_speed(Game.Shuriken.speed,
                                                EventHandler.DataStash.player.get_dexterity())))

            if self.out_of_screen():
                self.kill()

    def out_of_screen(self):
        return self.position[0] + self.dims[0] + 1 < 0 or self.position[0] >= Screen.displayWidth


class ShurukenGenerator:
    app = None

    shurikenGroup = None

    def __init__(self, app):
        self.app = app
        self.all_sprites = app.allSprites
        self.player = app.player
        self.mobs = app.mobGenerator
        self.shurikenGroup = pygame.sprite.Group

    def update(self) -> None:
        ...

    def generate(self) -> None:
        newShuriken = Shuriken(self.player.position.copy(), self.player.get_state_by_name("direction"))
        self.all_sprites.add(newShuriken)
        self.shurikenGroup.add(newShuriken)

from Entity import Entity
import pygame
from EventHandler import EventHandler
import Config
from Vector2D import Vector2D
from Game import Game
import math
from Screen import Screen
from Animation import Animation
import Scripts


class PoisonAttack(Entity):
    currentAnimationState = "casual"

    def __init__(self, position, alpha):
        super().__init__(position, dims=Config.Boss.PoisonBoss.ATTACK_DIMS)

        self.speedVector = Vector2D.from_polar(r=Game.get_speed(
            Game.Boss.attack_speed, Game.EnvStats.get_any_attr()
        ), teta=alpha)  # скорость под углом alpha

        self.animations["casual"] = Animation(textures_file_path=Config.Boss.PoisonBoss.ATTACK)

    def update(self) -> None:
        # TODO: Добвить коллизию с игроком и эффект
        self.move_by_vector()
        self.update_rect_by_pos()
        self.render_image()

        if self.rect.colliderect(EventHandler.DataStash.player.rect):
            teta = Scripts.get_angle_between_points(self.rect.center, EventHandler.DataStash.player.rect.center)

            push = Vector2D.from_polar(teta=math.pi - teta, r=Game.get_speed(Game.Boss.pushing_speed,
                                                                             Game.EnvStats.get_any_attr()))
            EventHandler.DataStash.player.playerSpeedVector = push
            EventHandler.DataStash.player.damage(Game.get_damage(Game.Boss.damage, Game.EnvStats.get_any_attr()))
            EventHandler.DataStash.player.decrease_level()
            self.kill()

        if self.out_of_screen():
            self.kill()

    def out_of_screen(self):
        return self.position[0] + self.dims[0] < 0 or \
            self.position[0] > Screen.width or self.position[1] + self.dims[1] < 0 or \
            self.position[1] > Screen.height


class PoisonAttackGenerator:
    poisonAttackGroup: pygame.sprite.Group

    def __init__(self):
        self.poisonAttackGroup = pygame.sprite.Group()

    def generate(self, position) -> None:
        """Генерирует колбочки в позиции и пинает их во все стороны"""
        numAttacks = Game.Boss.num_of_attacks

        for num in range(numAttacks):
            angle = (2 * math.pi / numAttacks) * num
            newAttack = PoisonAttack(position, angle)
            self.poisonAttackGroup.add(newAttack)
            EventHandler.DataStash.app.allSprites.add(newAttack)

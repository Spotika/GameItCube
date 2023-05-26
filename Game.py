import random

from EventHandler import EventHandler
import Config
import math


class Game:
    """Класс с параметрами всей игры и приложения в целом"""

    @classmethod
    def update_stats(cls):
        ...

    @staticmethod
    def get_mana_max(mana, intelligence):
        return mana + intelligence * 12

    @staticmethod
    def get_mana_regen(mana_regen, intelligence):
        return mana_regen + 0.05 * intelligence

    @staticmethod
    def get_health_max(health_max, strength):
        return health_max + 2 * strength

    @staticmethod
    def get_speed(speed, dexterity):
        return speed + dexterity * 2

    @classmethod
    def get_damage(cls, damage, strength, increase=1):
        d = damage + 2 * strength
        r = random.randint(round(d - d * cls.damageDiff), round(d + d * cls.damageDiff))

        return r * (abs(increase) ** 0.5)

    @staticmethod
    def get_delay(delay, intelligence):
        return delay * (1 - 0.004 * intelligence)

    @staticmethod
    def get_health_regen(health_regen, strength):
        return health_regen + 0.1 * strength

    @staticmethod
    def get_next_exp_for_lvl():
        """Возвращает кол-во опыта для следующего уровня по хитрой формуле"""
        l, m = EventHandler.DataStash.player.get_level(), EventHandler.DataStash.player.get_money()
        return round(Config.BASE_EXP_FOR_NEXT * math.sqrt(25 * l / (m + 1)))

    @classmethod
    def get_chance(cls, chance):
        return chance + cls.EnvStats.get_any_attr() * 0.005

    class EnvStats:
        BASE_HEALTH = 20

        @staticmethod
        def get_any_attr():
            return EventHandler.DataStash.player.get_money() * Config.STATE_BY_MONEY

    class Audio:
        volume = 10

    class Platforms:
        speed = 200

    class Mob:
        push_speed = 1000
        speed = 0
        diff = 10
        healthBase = 100

        damage = 20
        min_exp = 10
        max_exp = 40

    class DodgeSpell:
        delay = 3000
        mana = 70

        scale_by_dexterity = 0.2

    class Shuriken:
        speed = 200
        delay = 1000
        damage_diff = 0.15
        damage = 20

    class Boss:
        chanceToSpawn = 0.2  # FIXME
        _attackForBeat = 10
        _maxBosses = 1
        showingSpeed = 100
        speed = 200
        money_for_up = 250
        attack_speed = 250
        pushing_speed = 1000
        damage = 15

        @classmethod
        @property
        def num_of_attacks(cls):
            return round(16 * round(((EventHandler.DataStash.player.get_money() // (cls.money_for_up)) + 1) ** 0.5))

        @classmethod
        @property
        def max_casts(cls):
            return 1 + EventHandler.DataStash.player.get_money() // cls.money_for_up

        @classmethod
        @property
        def max_bosses(cls):
            # return 1 + EventHandler.DataStash.player.get_money() // cls.money_for_up
            return 1

        @classmethod
        @property
        def attack_for_beat(cls):
            return cls._attackForBeat + (EventHandler.DataStash.player.get_money() // cls.money_for_up) * 5

        @classmethod
        def get_time_wait(cls, time):
            """За каждые n монет время ожидания уменьшается в money // n раз"""
            return time / (EventHandler.DataStash.player.get_money() // (cls.money_for_up) + 1)

    damageDiff = 0.2

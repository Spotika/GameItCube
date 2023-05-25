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
        return speed + dexterity * 5

    @staticmethod
    def get_damage(damage, strength):
        return damage + 2 * strength

    @staticmethod
    def get_delay(delay, intelligence):
        return delay * (1 - 0.002 * intelligence)

    @staticmethod
    def get_health_regen(health_regen, strength):
        return health_regen + 0.05 * strength

    @staticmethod
    def get_next_exp_for_lvl():
        """Возвращает кол-во опыта для следующего уровня по хитрой формуле"""
        l, m = EventHandler.DataStash.player.get_level(), EventHandler.DataStash.player.get_money()
        return round(Config.BASE_EXP_FOR_NEXT * math.sqrt(15 * l / (m + 1)))

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

        damage = 30
        min_exp = 10
        max_exp = 40

    class DodgeSpell:
        delay = 5000
        mana = 70

        scale_by_dexterity = 0.2

    class Shuriken:
        speed = 200
        delay = 1000
        damage = 20

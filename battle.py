import time
from random import random

RECHARGED = True
RECHARGING = False

class Unit(object):

    def __init__(self):
        self.health = 100
        self.recharge = float()
        self.armour = float()

    def get_recharge(self):
        counter = time.ctime()
        if counter > self.recharge:
            return RECHARGED
        else:
            return RECHARGING

    def get_health(self):
        pass

class Solder(Unit):

    def __init__(self, **kwargs):
        super(Solder, **kwargs).__init__(**kwargs)
        self.experience = 0.0
        self.recharge = random(100, 2000)

    def do_attack(self, experience):
        damage = 0,5 * (1 + self.health / 100) * random(50 + experience, 100) / 100
        return damage

    def get_armour(self):
        self.armour = 0.05 + self.experience / 100
        return self.armour

    def take_damage(self, damage):
        self.health -= damage - self.armour
        return self.health

    def get_recharge(self):
        timer = time.ctime()


class Vehicles(Unit):

    def __init__(self, **kwargs):
        super(Vehicles, **kwargs).__init__(**kwargs)
        self.operators = int()
        self.recharge = random(1000, 2000)

    def do_attack(self):
        recharge_state = self.get_recharge()
        if recharge_state:
            damage = 0.1 + sum(self.operators.experience / 100)
            return damage
        elif not recharge_state:
            return 0

    def get_armour(self, experience):
        armour = 0.05 + experience / 100
        return armour

    def take_damage(self, armour, damage):
        result_health = self.health * len(operators) - (damage - armour)
        return result_health


class Army(object):

    def __init__(self):
        squads = Squad[]
        strategy = AtackStrategy

    def attack(self,):
        pass

class Squad(object):

    def __init__(self):
        units = Unit

    def get_power(self):
        pass


class Battlefield(object):

    def __init__(self):
        armies = Army

    def start(self):
        pass

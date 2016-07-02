from units import *


class Squad(object):

    def __init__(self, number_of_units):
        self.number_of_units = number_of_units
        self.units = list()
        self.get_units()
        self.power = self.get_power()
        self.active = True

    def get_units(self):
        if self.number_of_units > 10:
            self.number_of_units = 10
        elif self.number_of_units < 5:
            self.number_of_units = 5
        for _ in xrange(0, self.number_of_units):
            self.units.append(random.choice([Solder(), Vehicle()]))

    def is_active_units(self):
        active_units = list()
        for unit in self.units:
            if unit.active:
                active_units.append(unit)
        return active_units

    def get_power(self):
        squad_power = float()
        self.units = self.is_active_units()
        for unit in self.units:
            squad_power += unit.do_attack() / len(self.units)
        return squad_power

    def take_damage(self, mutual_damage):
        if mutual_damage != 0 and len(self.units) != 0:
            damage = mutual_damage / len(self.units)
        else:
            damage = 0
        for unit in self.units:
            unit.take_damage(damage)
        self.units = self.is_active_units()
        if len(self.units) == 0:
            self.active = False


class Army(object):

    def __init__(self, number_of_squads, number_of_units, strategy):
        self.number_of_squads = number_of_squads
        self.number_of_units = number_of_units
        self.squads = list()
        self.get_squads()
        self.strategy = strategy
        self.active = True

    def get_squads(self):
        if self.number_of_squads > 50:
            self.number_of_squads = 50
        elif self.number_of_squads < 2:
            self.number_of_squads = 2
        for _ in xrange(1, self.number_of_squads):
            self.squads.append(Squad(self.number_of_units))

    def get_strategy(self, army):
        if self.strategy == "random":
            random.shuffle(army.squads)

        elif self.strategy == "weakest":
            for squad in army.squads:
                for every in army.squads:
                    if every.power < squad.power:
                        buff = army.squads[army.squads.index(squad)]
                        army.squads[army.squads.index(squad)] = every
                        army.squads[army.squads.index(every)] = buff

        elif self.strategy == "strongest":
            for squad in army.squads:
                for every in army.squads:
                    if every.power > squad.power:
                        buff = army.squads[army.squads.index(squad)]
                        army.squads[army.squads.index(squad)] = every
                        army.squads[army.squads.index(every)] = buff

    def active_squads(self):
        active_squads = list()
        for squad in self.squads:
            if squad.active:
                active_squads.append(squad)
        return active_squads

    def attack(self, army):
        self.get_strategy(army)
        if len(army.squads) != 0:
            for squad in army.squads:
                squad.take_damage(self.squads[self.squads.index(random.choice(self.squads))].power)
            self.squads = self.active_squads()
            if len(self.squads) == 0:
                self.active = False


class Battlefield(object):

    # def __init__(self):
    #    self.armies = self.armies

    def start(self):
        army_1 = Army(number_of_squads=2, number_of_units=5, strategy="random")
        army_2 = Army(number_of_squads=2, number_of_units=5, strategy="random")
        while army_1.active and army_2.active:
            army_1.attack(army_2)
            army_2.attack(army_1)
        if army_1.active:
            print "Army 1 win!"
        else:
            print "Army 1 lose"
        if army_2.active:
            print "Army 2 win!"
        else:
            print "Army 2 lose"

if __name__ == "__main__":
    go = Battlefield()
    go.start()

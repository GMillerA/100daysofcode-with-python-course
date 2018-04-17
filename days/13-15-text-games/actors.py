import random


class Creature:
    def __init__(self, name, level, health):
        self.name = name
        self.level = level
        self.health = health



    def defensive_roll(self):
        roll = random.randint(1, 12)
        return roll * self.level


class Dragon(Creature):
    def __init__(self, name, level, health, scaliness, breaths_fire):
        super().__init__(name, level, health)
        self.health = health
        self.scaliness = scaliness
        self.breaths_fire = breaths_fire

    def defensive_roll(self):
        roll = super().defensive_roll()
        value = roll * self.scaliness
        if self.breaths_fire:
            value = value * 2
        return value


class Wizard(Creature): #TODO: Change wizard to general hero? Add sublasses for Ranger, Fighter, etc.?
    def __init__(self, name, level, health, experience=0):
        super().__init__(name, level, health)
        self.experience = experience


    def attack(self, creature):
        my_roll = self.defensive_roll()
        their_roll = creature.defensive_roll()
        diff = abs(self.level - creature.level)
        if my_roll >= their_roll:
            creature.health -= diff
            self.health += creature.level
            if creature.health <= 0:
                return True
        else:
            self.health -= diff
            print('Ouch! Current health is now {}'.format(self.health))
            return False

    def update_experience(self, creature):
        exp = creature.level * 1.5
        self.experience += exp

    def level_up(self):
        if self.experience >= (.5 * self.level):
            self.level += 5 #TODO: scale levelling up by creature level?
            self.experience = 0
            self.health = self.level
            print('The hero {} is now level {}!'.format(self.name, self.level))

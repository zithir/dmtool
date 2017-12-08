'''
This file should contain purely the Character class and its methods
'''
from libs.dndutils import roll
from libs.fetch_data import *


class Character(object):
    lvl = 1
    abilities = {'Str': 0, 'Dex': 0, 'Con': 0, 'Int': 0, 'Wis': 0, 'Cha': 0}
    saves = {'Fort': 0, 'Refl': 0, 'Will': 0}
    base_attack = []
    def __init__(self, name, race, classs):
        self.name = name
        self.race = race
        self.classs = classs

    def __repr__(self):
        return "%s, a(n) %s %s" % (self.name, self.race, self.classs)

    def show_abilities(self):
        for key in get_ability_names():
            print("%s:  %s" % (key, str(self.abilities[key])))


class Fighter(Character):
    def __init__(self, name, race, classs):
        self.name = name
        self.race = race
        self.classs = classs

    abilities_order = ['Str', 'Con', 'Dex', 'Cha', 'Wis', 'Int']
    lives = roll(10, 1)
    class_skills = ['Climb', 'Craft', 'Handle Animal', 'Intimidate', 'Jump',
                    'Ride', 'Swim']
    skill_points = (2 + self.abilities['Int']) * 4
    saves_lvls = {
                    'Fort': [2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,12],
                    'Refl':[0,0,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6],
                    'Will': [0,0,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6]
                    }

    def count_base_attack(self):
        attack = self.lvl
        if self.lvl < 6:
            return [self.lvl]
        elif 5 < self < 11:
            return [self.lvl, self.lvl - 5]
        elif 10 < self.lvl < 16:
            return [self.lvl, self.lvl - 5, self.lvl - 10]
        else:
            return [self.lvl, self.lvl - 5, self.lvl - 10, self.lvl - 11]

    base_attack = count_base_attack()

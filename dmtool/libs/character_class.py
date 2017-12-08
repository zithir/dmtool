'''
This file should contain purely the Character class and its methods
'''
from libs.dndutils import roll
from libs.dndutils import ability_modifier
from libs.fetch_data import *


class Character(object):
    lvl = 1
    abilities = {'Str': 0, 'Dex': 0, 'Con': 0, 'Int': 0, 'Wis': 0, 'Cha': 0}
    saves = {'Fort': 0, 'Refl': 0, 'Will': 0}

    def __init__(self, name, race, classs):
        self.name = name
        self.race = race
        self.classs = classs

    def __repr__(self):
        return "%s, a(n) %s %s" % (self.name, self.race, self.classs)

    def count_skill_points(self):
        """
        TODO: make and use translator to convert ability score to ability bonus
        """
        self.skill_points = (2 + ability_modifier(self.abilities['Int'])) * 4

    def show_abilities(self):
        for key in get_ability_names():
            print("%s:  %s" % (key, str(self.abilities[key])))

class Barbarian(Character):
    abilities_order = ['Str', 'Dex', 'Con', 'Cha', 'Wis', 'Int']
    lives = roll(12, 1)
    class_skills = ['Climb', 'Craft', 'Handle Animal', 'Intimidate', 'Jump',
                    'Listen', 'Ride', 'Survival', 'Swim']
    saves_lvls = {
                    'Fort': [2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,12],
                    'Refl':[0,0,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6],
                    'Will': [0,0,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6]
                    }


class Fighter(Character):
    abilities_order = ['Str', 'Con', 'Dex', 'Cha', 'Wis', 'Int']
    lives = roll(10, 1)
    class_skills = ['Climb', 'Craft', 'Handle Animal', 'Intimidate', 'Jump',
                    'Ride', 'Swim']
    saves_lvls = {
                    'Fort': [2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,12],
                    'Refl':[0,0,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6],
                    'Will': [0,0,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6]
                    }

'''
NOT WORKING
    def count_base_attack(Character.lvl):
        if lvl < 6:
            Character.base_attack = [Character.lvl]
        elif 5 < Character.lvl < 11:
            return [Character.lvl, Character.lvl - 5]
        elif 10 < Character.lvl < 16:
            return [Character.lvl, Character.lvl - 5, Character.lvl - 10]
        else:
            return [Character.lvl, Character.lvl - 5, Character.lvl - 10,
                    Character.lvl - 11]

    def count_base_attack(self):
       self.base_attack = get_base_attack(self)
'''

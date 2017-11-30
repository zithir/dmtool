'''
This file should contain purely the Character class and its methods
'''
from libs.dndutils import *
from libs.xml_io import *


class Character(object):
    abilities = {'Str': 0, 'Dex': 0, 'Con': 0, 'Int': 0, 'Wis': 0, 'Cha': 0}
    saves = {'Fort': 0, 'Refl': 0, 'Will': 0}
    def __init__(self, name, race, classs):
        self.name = name
        self.race = race
        self.classs = classs

    def __repr__(self):
        return "%s, a(n) %s %s" % (self.name, self.race, self.classs)

    def show_abilities(self):
        for key in get_ability_names():
            print("%s:  %s" % (key, str(self.abilities[key])))

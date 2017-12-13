'''
This file should contain the Character class and its methods and additionaly
individual "DnD Class" classes  which inherit from the Character class
Any newly created DnD Class must be completely defined as others and it must
be added to switch in the class_selector function.
'''
from libs.dndutils import roll
from libs.dndutils import ability_modifier
import libs.fetch_data

#-----------------------------------------------------------------------------#
# GENERAL CHARACTER CLASS
#-----------------------------------------------------------------------------#

class Character(object):
    """
    Based on the Commoner NPC class
    """
    lvl = 1
    # Abilities are always based on race, they should be therefore determined
    # during character creation
    abilities = {'Str': 0, 'Dex': 0, 'Con': 0, 'Int': 0, 'Wis': 0, 'Cha': 0}
    saves = {'Fort': 0, 'Refl': 0, 'Will': 0}
    lives = 0
    # A rather random order, a randomizing function could be made
    abilities_order = ['Con', 'Wis', 'Dex', 'Cha', 'Str', 'Int']
    saves = {'Fort': 0, 'Refl': 0, 'Will': 0}
    saves_lvls = {
                    'Fort': libs.fetch_data.get_saves("001_3"),
                    'Refl': libs.fetch_data.get_saves("001_3"),
                    'Will': libs.fetch_data.get_saves("001_3")
                    }
    class_skills = [
                    'Climb', 'Craft', 'Handle Animal', 'Jump', 'Listen'
                    'Profession', 'Ride', 'Spot', 'Swim', 'Use Rope'
                    ]
    skill_points_modifier = 2
    hit_die = {'sides': 4, 'rolls': 1, 'bonus': 0}

    def count_saves(self):
        for key in self.saves:
            self.saves[key] = self.saves_lvls[key][self.lvl - 1]

    def count_skill_points(self):
        if self.lvl == 1:
            return (self.skill_points_modifier +
                                ability_modifier(self.abilities['Int'])) * 4
        else:
            return (self.skill_points_modifier +
                    ability_modifier(self.abilities['Int']))

    def count_base_attack(self):
        if self.lvl == 1:
            return [0]
        elif 2 <= self.lvl <= 11:
            return [int(self.lvl / 2)]
        elif 12 <= self.lvl:
            return [int(self.lvl / 2), int((self.lvl - 10) / 2)]

    def count_lives(self):
        return (
                self.lives + ability_modifier(self.abilities['Con']) +
                roll(self.hit_die['sides'], self.hit_die['rolls']) +
                self.hit_die['bonus']
                )

    # -------------------------------------------------------------------------
    # INITIATION
    # For simplicity, it is separated into two parts (hence init2)
    # The __init__ function makes object only with basic characteristics based
    # on selection during character creation
    # the init2 calculates attributes of the character based on ability SCORES
    # and class selection
    # -------------------------------------------------------------------------
    def __init__(self, name, race, ch_class):
        self.name = name
        self.race = race
        self.ch_class = ch_class

    def init2(self):
        """
        TODO: a function that will load new class attributes(both python and dnd)
        it should use fetch_data.py and it must run before calculation
        """
        self.skill_points = self.count_skill_points()
        self.base_attack = self.count_base_attack()
        self.count_saves()
        self.lives = self.count_lives()


    # ------------------------------------------------------------------------#
    # AUXILIARY METHODS
    # ------------------------------------------------------------------------#
    def __repr__(self):
        return "%s, a(n) %s %s" % (self.name, self.race, self.ch_class)

    def show_abilities(self):
        for key in self.abilities:
            print("%s:  %s" % (key, str(self.abilities[key])))

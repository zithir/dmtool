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
    # A rather random order, a randomizing function coud me made
    abilities_order = ['Con', 'Wis', 'Dex', 'Cha', 'Str', 'Int']


    saves = {'Fort': 0, 'Refl': 0, 'Will': 0}
    saves_lvls = {
                    'Fort': libs.fetch_data.get_saves("001_3"),
                    'Refl': libs.fetch_data.get_saves("001_3"),
                    'Will': libs.fetch_data.get_saves("001_3")
                    }

    def count_saves(self):
        for key in self.saves:
            self.saves[key] = self.saves_lvls[key][self.lvl-1]

    class_skills = [
                    'Climb', 'Craft', 'Handle Animal', 'Jump', 'Listen'
                    'Profession', 'Ride', 'Spot', 'Swim', 'Use Rope'
                    ]

    skill_points_modifier = 2

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
            return [int(self.lvl / 2), int((self.lvl) - 10) / 2]

    lives = 0
    hit_die = {'sides': 4, 'rolls': 1, 'bonus': 0}
    def count_lives(self):
        return (
                self.lives + ability_modifier(self.abilities['Con']) +
                roll(self.hit_die['sides'], self.hit_die['rolls']) +
                self.hit_die['bonus']
                )

    def __init__(self, name, race, ch_class):
        self.name = name
        self.race = race
        self.ch_class = ch_class

    def init2(self):
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


# -----------------------------------------------------------------------------#
# INDIVIDUAL DND CLASS CLASSES
# -----------------------------------------------------------------------------#
classes = [
    "fighter", "rogue", "wizard", "barbarian", "paladin", "sorcerer", "bard",
    "cleric", "druid", "monk", "ranger"
]


def class_selector(name, race, ch_class):
    '''
    This function is used to assign created character a proper character class
    Character classes are defined as python classes which inherit from
    '''
    if ch_class == "barbarian":
        return Barbarian(name, race, ch_class)
    elif ch_class == "fighter":
        return Fighter(name, race, ch_class)
    else:
        return Character(name, race, ch_class)


# class Barbarian(Character):
#     abilities_order = ['Str', 'Dex', 'Con', 'Cha', 'Wis', 'Int']
#     lives = roll(12, 1)
#     class_skills = [
#         'Climb', 'Craft', 'Handle Animal', 'Intimidate', 'Jump', 'Listen',
#         'Ride', 'Survival', 'Swim'
#     ]
#     skill_points_modifier = 2
#
#     saves_lvls = {
#         'Fort': libs.fetch_data.get_saves("233_2"),
#         'Refl': libs.fetch_data.get_saves("001_3"),
#         'Will': libs.fetch_data.get_saves("001_3")
#     }
#
#
# class Bard(Character):
#     abilities_order = ['Cha', 'Dex', 'Int', 'Con', 'Str', 'Wis']
#     lives = roll(6, 1)
#
#
# class Fighter(Character):
#     abilities_order = ['Str', 'Con', 'Dex', 'Cha', 'Wis', 'Int']
#     lives = roll(10, 1)
#     class_skills = [
#         'Climb', 'Craft', 'Handle Animal', 'Intimidate', 'Jump', 'Ride', 'Swim'
#     ]
#
#     saves_lvls = {
#         'Fort': libs.fetch_data.get_saves("233_2"),
#         'Refl': libs.fetch_data.get_saves("001_3"),
#         'Will': libs.fetch_data.get_saves("001_3")
#     }
#
#
# '''
# NOT WORKING
#     def count_base_attack(Character.lvl):
#         if lvl < 6:
#             Character.base_attack = [Character.lvl]
#         elif 6 =< Character.lvl < 11:
#             return [Character.lvl, Character.lvl - 5]
#         elif 11 =< Character.lvl < 16:
#             return [Character.lvl, Character.lvl - 5, Character.lvl - 10]
#         else:
#             return [Character.lvl, Character.lvl - 5, Character.lvl - 10,
#                     Character.lvl - 11]
#
#     def count_base_attack(self):
#        self.base_attack = get_base_attack(self)
# '''

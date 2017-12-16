'''
This file should contain the Character class and its methods and additionaly
individual "DnD Class" classes  which inherit from the Character class
Any newly created DnD Class must be completely defined as others and it must
be added to switch in the class_selector function.
'''
from libs.dndutils import roll
from libs.dndutils import ability_modifier
import libs.fetch_data as fetch_data

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
    ABILITIES_ORDER = ['Con', 'Wis', 'Dex', 'Cha', 'Str', 'Int']
    saves = {'Fort': 0, 'Refl': 0, 'Will': 0}
    SAVES_LVLS = {
                    'Fort': ("001_3"),
                    'Refl': ("001_3"),
                    'Will': ("001_3")
                    }
    CLASS_SKILLS = [
                    'Climb', 'Craft', 'Handle Animal', 'Jump', 'Listen'
                    'Profession', 'Ride', 'Spot', 'Swim', 'Use Rope'
                    ]
    SKILL_POINTS_MOD = 2
    HIT_DIE = {'sides': 4, 'rolls': 1, 'bonus': 0}
    BASE_ATTACK_LVLS = '011_12'

    def count_saves(self):
        for key in self.saves:
            self.saves[key] = fetch_data.get_saves(self.SAVES_LVLS[key],
                                                                self.lvl)

    def count_skill_points(self):
        if self.lvl == 1:
            return (self.SKILL_POINTS_MOD +
                                ability_modifier(self.abilities['Int'])) * 4
        else:
            return (self.SKILL_POINTS_MOD +
                    ability_modifier(self.abilities['Int']))

    def count_lives(self):
        return (
                self.lives
                + ability_modifier(self.abilities['Con'])
                + roll(self.HIT_DIE['sides'], self.HIT_DIE['rolls'])
                + self.HIT_DIE['bonus']
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
        self.ABILITIES_ORDER = fetch_data.get_abilities_order(self.ch_class)

    def class_adjustment(self):
        """
        Adjustment of Character class according to character class ;)
        In real, it changes the class-dependent attributes.
        """
        self.ABILITIES_ORDER = fetch_data.get_abilities_order(self.ch_class)

        for key in self.SAVES_LVLS:
            self.SAVES_LVLS[key] = fetch_data.get_class_saves(key, self.ch_class)

        self.CLASS_SKILLS = fetch_data.get_class_skills(self.ch_class)
        self.SKILL_POINTS_MOD = fetch_data.get_skillp_modifier(self.ch_class)
        self.HIT_DIE = fetch_data.get_hit_die(self.ch_class)
        self.BASE_ATTACK_LVLS = fetch_data.get_class_base_attack(self.ch_class)

    def init2(self):
        """
        This method caluclates attributes of the class that cannot be
        instantiated in the beginning but require additional data
        """
        self.skill_points = self.count_skill_points()
        self.count_saves()
        self.lives = self.count_lives()
        self.base_attack = fetch_data.get_base_attack(self.BASE_ATTACK_LVLS, self.lvl)



    # ------------------------------------------------------------------------#
    # AUXILIARY METHODS
    # ------------------------------------------------------------------------#
    def __repr__(self):
        summary = "%s, a(n) %s %s, level %s\n" % (self.name, self.race,
                                                self.ch_class, str(self.lvl))
        summary += '\n'
        for key in self.abilities:
            summary += ("%s:  %s\n" % (key, str(self.abilities[key])))
        summary += '\n'
        summary += 'Lives: %s\n' % str(self.lives)
        summary += 'Base attack: %s\n' % str(self.base_attack)
        summary += '\n'
        for key in self.saves:
            summary += ("%s:  %s\n" % (key, str(self.saves[key])))
        summary += '\n'
        summary += 'Available skill point: %s\n' % self.skill_points
        summary += 'Class skills: %s' % self.CLASS_SKILLS
        return summary


    def show_abilities(self):
        for key in self.abilities:
            print("%s:  %s" % (key, str(self.abilities[key])))

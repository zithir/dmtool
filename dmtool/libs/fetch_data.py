"""
This file will contain functions that will fetch data from and write into xml
files from the "data" directory. So far the data is in the form of py modules
and the functions respect that.
In the future the data will be converted to xml and these functions should be
modified acordingly.
"""

import data.characters

def get(query):
    if query == "races":
        return sorted(data.characters.races)
    elif query == "classes":
        return sorted(data.characters.classes)
    elif query == "ability_names":
        return data.characters.ability_names
    else:
        return


def get_ability_names():
    return data.characters.ability_names

def get_ability_adjustment(race, ability):
    try:
        return data.characters.ability_adjustment[race][ability]
    except KeyError:
        return 0


def get_saves(id, lvl):
    '''
    Returns value of save from list according to level of character
    '''
    return data.characters.saves[id][lvl - 1]

def get_class_saves(key, ch_class):
    '''
    Returns code that identifies which list of saves applies to given character
    class
    '''
    return data.characters.classes[ch_class]['SavesLvls'][key]

def get_base_attack(id, lvl):
    '''
    Returns value of base attack from list according to level of character
    '''
    return data.characters.AttackBonuses[id][lvl-1]

def get_class_base_attack(ch_class):
    '''
    Returns code that identifies which list of attack bonuses applies to given
    character class
    '''
    return data.characters.classes[ch_class]['AttackBonuses']

def get_abilities_order(ch_class):
    return data.characters.classes[ch_class]['AbilitiesOrder']

def get_class_skills(ch_class):
    return data.characters.classes[ch_class]['ClassSkills']

def get_skillp_modifier(ch_class):
    return data.characters.classes[ch_class]['SkillPointsModifier']

def get_hit_die(ch_class):
    return data.characters.classes[ch_class]['HitDie']

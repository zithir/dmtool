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
    #elif query == "classes":
    #    return libs.character_class.classes)
    elif query == "ability_names":
        return data.characters.ability_names
    else:
        return


def get_ability_names():
    return data.characters.ability_names


def get_best_abilities(ch_class):
    return data.characters.ability_best[ch_class]


def get_ability_adjustment(race, ability):
    try:
        return data.characters.ability_adjustment[race][ability]
    except KeyError:
        return 0


def get_saves(key):
    return data.characters.saves[key]

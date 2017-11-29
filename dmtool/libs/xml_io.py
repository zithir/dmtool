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
        return data.characters.races
    elif query == "classes":
        return data.characters.classes
    elif query == "ability_names":
        return data.characters.ability_names
    else:
        return


def ability_names():
    return data.characters.ability_names


def best_abilities(classs):
    return data.characters.best_ab[classs]

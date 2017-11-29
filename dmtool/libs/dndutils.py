"""
Library with general DnD functions
It can be called from every other module.
This file contains the old code, which is commented at the bottom. Only
when the function is used, it can be uncommented.
"""

import random


def roll(sides, rolls):
    """
    Classic dnd roll for any number of rolls with any-sided dice.
    First argument is number of sides of the dice and the second number of
    rolls with the dice
    """
    value = 0
    for i in range(rolls):
        x=random.randint(1, sides)
        value += x
    return value

def ensure(mode, extra = ""):
    """
    A general function to confirm selection.
    Supressed by q(uick)_mode
    """
    if 'q' in mode:
        return True
    else:
        while True:
            good = input("Do you want to proceed?  %s (y/N) " % extra)
            print()
            if good == "y":
                return True
            elif good == "N":
                return False


"""
def class_select (clas):
    attributes = attr_roll ()
    if clas == "barbarian":
        str = attributes[0]
        dex = attributes[2]
        con = attributes[1]
        ing = attributes[5]
        wis = attributes[3]
        chr = attributes[4]
        fort = 2
        ref = 0
        will = 0

    elif clas == "wizard":
        str = attributes[5]
        dex = attributes[1]
        con = attributes[2]
        ing = attributes[0]
        wis = attributes[3]
        chr = attributes[4]
        fort = 2
        ref = 0
        will = 0

    elif clas == "rogue":
        str = attributes[4]
        dex = attributes[0]
        con = attributes[3]
        ing = attributes[1]
        wis = attributes[2]
        chr = attributes[5]
        fort = 2
        ref = 0
        will = 0

    return {"Saves": {"Fortitude":fort, "Willpower":will, "Reflexes":ref},
            "Attributes": {'Str':str, 'Dex':dex, 'Con':con, 'Ing':ing, 'Wis':wis, 'Chr':chr}}


def race_select (race, character):
    if race=="human":
        character["Attributes"] = character["Attributes"]
    elif race=="dwarf":
       character["Attributes"]["Con"] =  character["Attributes"]["Con"] + 2
       character["Attributes"]["Chr"] =  character["Attributes"]["Chr"] - 2

    elif race=="elf":
        character["Attributes"]["Dex"] =  character["Attributes"]["Dex"] + 2
        character["Attributes"]["Con"] =  character["Attributes"]["Con"] - 2
    return character
"""

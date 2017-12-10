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


def ability_modifier(ability_score):
    """
    Returns modifier for any ability score
    """
    if ability_score == 1:
        return -5
    elif 1 < ability_score < 4:
        return -4
    elif 3 < ability_score < 6:
        return -3
    elif 5 < ability_score < 8:
        return -2
    elif 7 < ability_score < 10:
        return -1
    elif 9 < ability_score < 12:
        return 0
    elif 11 < ability_score < 14:
        return 1
    elif 13 < ability_score < 16:
        return 2
    elif 15 < ability_score < 18:
        return 3
    elif 17 < ability_score < 20:
        return 4
    elif 19 < ability_score < 22:
        return 5
    elif 21 < ability_score < 24:
        return 6
    elif 23 < ability_score < 26:
        return 7
    elif 25 < ability_score < 28:
        return 8
    elif 27 < ability_score < 30:
        return 9
    elif 29 < ability_score < 32:
        return 10
    elif 31 < ability_score < 34:
        return 11
    elif 33 < ability_score < 36:
        return 12
    elif 35 < ability_score < 38:
        return 13
    elif 37 < ability_score < 40:
        return 14
    elif 39 < ability_score < 42:
        return 15
    elif 41 < ability_score < 44:
        return 16
    elif 43 < ability_score < 46:
        return 17
    elif 45 < ability_score < 48:
        return 18

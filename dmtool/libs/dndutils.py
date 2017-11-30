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

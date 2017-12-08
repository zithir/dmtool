"""
This module is used to lead the user throught the interactive creation of the
character.
In the end the created characet should be imported to XML file with the name of
the character.
"""

from libs.dndutils import *
from libs.fetch_data import *
from libs.character_class import Character

MODE = ''
character = None



def main(name, race, classs, mode):
    """
    Modes:
    quick, q - quick mode supresses ensure prompts
    TODO
    standard, s - default process of character creation
    auto, a - instead of asking, predefined (best) values are used
    random, r - random selection of class and race
    """
    global MODE, character
    MODE = mode

    print("\nCharacter creation started! \n")

    #-------------------------------------------------------------------------#
    # NAME, RACE, CLASS
    #-------------------------------------------------------------------------#
    # Asking about name, race and class of the character
    # Nested in 'while' statement to allow confirmation and possibility
    # to start over

    confirm = False # Value changes with ensure() function
    while not confirm:

        # Determine missing or invalid values and instantiating character:
        if not name:
            name = name_select()

        if not race:
            race = race_select()
        elif race not in get("races"):
            print("Provided race is not availible.")
            race = race_select()

        if not classs:
            classs = classs_select()
        elif classs not in get("classes"):
            print("Provided class is not availible.")
            classs = classs_select()

        character = Character(name, race, classs)
        print("The character will be ", character, "\n" )

        # Ensuring that imput is valid, otherwise the process restarts
        confirm = ensure(MODE)
        if confirm is False:
            name = ""
            race = ""
            classs = ""

    #-------------------------------------------------------------------------#
    # ABILITY SCORES
    #-------------------------------------------------------------------------#

    # Assigning ability scores

    confirm = False # Reset the confirm value
    while confirm is False:
        ab_scores_select(character)

        print("The character will have the following ability scores:")
        print(character.abilities, "\n")
        confirm = ensure(mode, "Warning, new values will be rolled.")


    #-------------------------------------------------------------------------#
    #COMBAT NUMBERS
    #-------------------------------------------------------------------------#



    return character

###############################################################################
# Individual functions used in main:
###############################################################################
#-------------------------------------------------------------------------#
# NAME, RACE, CLASS
#-------------------------------------------------------------------------#

def name_select():
    print("Please enter name of your character:")
    name = str(input(""))
    while not name:
        print("Name is empty, please try again:")
        name = str(input(""))
    print("Name of character: ", name, "\n")
    return name


def race_select():
    print("Select race of your character, following are available:")
    print(get("races"))
    race = str(input("")).lower()
    while race not in get("races"):
        print("Such race is not available, please select one from ",
            "the following list: ")
        print(get("races"))
        race = str(input("")).lower()
    print("Race of character: ", race, "\n")
    return race


def classs_select():
    print("Select class of your character, following are available:")
    print(get("classes"))
    classs = str(input("")).lower()
    while classs not in get("classes"):
        print("Such class is not available, please select one from "
            "the following list: ")
        print(get("classes"))
        classs = str(input("")).lower()
    print("Class of character: ", classs, "\n")
    return classs


#-------------------------------------------------------------------------#
# ABILITY SCORES
#-------------------------------------------------------------------------#

def ab_scores_roll():
    """
    ATTRIBUTES ROLL
    Roll for character creation.
    Returns array of 6 3d6 rolls. Rolls 4 times and removes the smallest value.
    """
    value = [0,0,0,0,0,0]
    for i in range (6):
        rolls = [0,0,0,0]
        for x in range (4):
            rolls[x] = roll(6,1)
        rolls.remove(min(rolls))
        z = sum(rolls)
        value[i] = z

    value.sort(reverse=True)
    return (value)


def ab_scores_select(character):
    print("Starting ability scores asignment")

    confirm = False
    while confirm is False:
        rolls = ab_scores_roll()
        print("Following values have been rolled: ")
        print(rolls)
        confirm = ensure(MODE)

    if 'a' in MODE:
        print("Automated ability scores assignment")
        for ability in get_best_abilities(character.classs):
            character.abilities[ability] = rolls.pop(0)
    else:
        print("Manual ability scores assignment")
        for ability in get_ability_names():
            character.abilities[ability] = ab_scores_assign(character,
                                                            rolls, ability)

            character.abilities[ability] += get_ability_adjustment(
                                                        character.race, ability)


def ab_scores_assign(character, rolls, ability):
    print('Assign a value for %s, following are availiable:\n%s'
            % (ability, str(rolls)))
    if get_ability_adjustment(character.race, ability) != 0:
        print('(Race modifier for this ability: %s)' %
                get_ability_adjustment(character.race, ability))
    while True:
        assignment = input('%s = ' % ability)
        try:
            assignment = int(assignment)
            if assignment in rolls:
                rolls.remove(assignment)
                return assignment
        except ValueError:
            pass
        print("Value not available try again.")


#-------------------------------------------------------------------------#
# COMBAT NUMBERS
#-------------------------------------------------------------------------#

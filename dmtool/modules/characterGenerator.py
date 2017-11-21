from libs.dndutils import *
from libs.xml_io import *


class Character(object):
    def __init__(self, name, race, classs):
        self.name = name
        self.race = race
        self.classs = classs


def main():
    print("Random test roll: ", roll(1, 6)) #DEBUG
    print("\nCharacter creation started! \n")

    name = name_select()
    race = race_select()


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
    print(get_races())
    race = str(input("")).lower()
    while race not in get_races():
        print("Such race is not available, please select one from"
            "the following list: ")
        print(get_races())
        race = str(input("")).lower()
    print("Race of character: ", race, )
    return race

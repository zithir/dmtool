from libs.dndutils import *
from libs.xml_io import *


class Character(object):
    def __init__(self, name, race, classs):
        self.name = name
        self.race = race
        self.classs = classs

    def __repr__(self):
        return "%s, a(n) %s %s" % (self.name, self.race, self.classs)


def main():
    print("\nCharacter creation started! \n")

    # Asking about name, race and class of the character
    # Nested in 'while' statement to allow confirmation and possiby
    confirm = False
    while confirm == False:
        name = name_select()
        race = race_select()
        classs = classs_select()
        character = Character(name, race, classs)
        print("The character will be ", character)
        confirm = ensure()

"""
Function  not necessary
def name_race_classs():
    name = name_select()
    race = race_select()
    classs = classs_select()
    nrc = [name, race, classs]
    return nrc
"""
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
        print("Such race is not available, please select one from",
            "the following list: ")
        print(get("races"))
        race = str(input("")).lower()
    print("Race of character: ", race, "\n" )
    return race

def classs_select():
    print("Select class of your character, following are available:")
    print(get("classes"))
    classs = str(input("")).lower()
    while classs not in get("classes"):
        print("Such class is not available, please select one from"
            "the following list: ")
        print(get("classes"))
        classs = str(input("")).lower()
    print("Class of character: ", classs, "\n" )
    return classs

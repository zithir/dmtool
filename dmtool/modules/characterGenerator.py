import libs.dndutils

class Character(object):
    def __init__(self, name, race, classs):
        self.name = name
        self.race = race
        self.classs = classs



def make_character():
    print("Character creation started")
    print("Please enter your name:")
    name = input("")
    while not name.isalpha:
        print("Invalid name, please try again (only alphabetical characters allowed).")
        name = input("")
    print(name)
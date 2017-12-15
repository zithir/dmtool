"""
This is the "main" function of the whole program. It should be run in the int-
eractive mode and then its individual functions should be called. Each function
will run a main function of individual module from "modules" directory.
The modules should handle the specific functionality.
"""

import modules.character_generator as character_generator

character = None

def make_character(name = "", race = "", ch_class = "", mode = "s"):
     global character
     character = character_generator.main(name, race, ch_class, mode)
     return character

print("Welcome to dmtool")
make_character("Monty", "human", "bard", "qa" )  # DEBUG
character.show_abilities() # DEBUG

"""
This is the "main" function of the whole program. It should be run in the int-
eractive mode and then its individual functions should be called. Each function
will run a main function of individual module from "modules" directory.
The modules should handle the specific functionality.
"""

import modules.characterGenerator as characterGenerator


def make_character():
    return characterGenerator.main()


print("Welcome to dmtool")
make_character()  # DEBUG

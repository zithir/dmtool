import random
import dnd_lib

clas = "barbarian"
race = "elf"
character = dnd_lib.class_select (clas)
print (character)

character = dnd_lib.race_select (race, character)
print (character)

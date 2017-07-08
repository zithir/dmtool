import random
import dnd_lib

clas = "rogue"
race = "dwarf"
attributes = dnd_lib.class_select (clas)

dnd_lib.race_select (race, attributes)


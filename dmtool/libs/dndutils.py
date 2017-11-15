# Library with basic DnD functions 
import random

# DICE ROLL
# Basic dice roll for sum of any number of any-sided dices
# Arguments:
#   side = number of sides 
#   rolls = number of dices
def dnd_dice (sides, rolls):

    value = 0
    for i in range (rolls):
        x=random.randint(1,sides)
        value = value + x
    return value

# ATTRIBUTES ROLL
# Roll for character creation.
# Returns array of 6 3d6 rolls. Rolls 4 times and removes the smallest value.
def attr_roll ():

    value = [0,0,0,0,0,0]
    for i in range (6):
        rolls = [0,0,0,0]
        for x in range (4):
            rolls[x] = dnd_dice (6,1)
        rolls.remove(min(rolls))
        z = sum(rolls)
        value[i] = z

    value.sort(reverse=True)
    return (value)
       
def class_select (clas):
    attributes = attr_roll ()
    if clas == "barbarian":
        str = attributes[0]
        dex = attributes[2]
        con = attributes[1]
        ing = attributes[5]
        wis = attributes[3]
        chr = attributes[4]
        fort = 2
        ref = 0
        will = 0 
    
    elif clas == "wizard":
        str = attributes[5]
        dex = attributes[1]
        con = attributes[2]
        ing = attributes[0]
        wis = attributes[3]
        chr = attributes[4]
        fort = 2
        ref = 0
        will = 0 
    
    elif clas == "rogue":
        str = attributes[4]
        dex = attributes[0]
        con = attributes[3]
        ing = attributes[1]
        wis = attributes[2]
        chr = attributes[5]
        fort = 2
        ref = 0
        will = 0 

    return {"Saves": {"Fortitude":fort, "Willpower":will, "Reflexes":ref}, 
            "Attributes": {'Str':str, 'Dex':dex, 'Con':con, 'Ing':ing, 'Wis':wis, 'Chr':chr}}
  

def race_select (race, character):
    if race=="human":
        character["Attributes"] = character["Attributes"]          
    elif race=="dwarf":
       character["Attributes"]["Con"] =  character["Attributes"]["Con"] + 2
       character["Attributes"]["Chr"] =  character["Attributes"]["Chr"] - 2
        
    elif race=="elf":
        character["Attributes"]["Dex"] =  character["Attributes"]["Dex"] + 2
        character["Attributes"]["Con"] =  character["Attributes"]["Con"] - 2
    return character
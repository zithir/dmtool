"""
Data regarding player characters. In the future they should be converted
into xmls.
"""


races = ["human", "elf", "dwarf"]
classes = ["fighter", "rogue", "wizard"]

ability_names = ['Str', 'Dex', 'Con', 'Int', 'Wis', 'Cha']



best_ab = {
# Manually created list of best order of abilities for a given class
# The order can be adjusted
# Descending order (from high priority to low)
           'fighter':['Str', 'Con', 'Cha', 'Dex', 'Wis', 'Int'],
           'rogue'  :['Dex','Int','Wis', 'Con', 'Str', 'Cha'],
           'mage'   :['Int', 'Dex', 'Con', 'Wis', 'Cha', 'Con']
           }

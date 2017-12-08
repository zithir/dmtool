"""
Data regarding player characters. In the future they should be converted
into xmls.
"""


races = ["human", "elf", "dwarf", "gnome", "half-elf", "half-orc", "halfling"]
classes = ["fighter", "rogue", "wizard", "barbarian", "paladin", "sorcerer",
                                    "bard", "cleric", "druid", "monk", "ranger"]

# Fixed ability order that should be used any time
ability_names = ['Str', 'Dex', 'Con', 'Int', 'Wis', 'Cha']

ability_best = {
# Manually created list of best order of abilities for a given class
# The order can be adjusted
# Descending order (from high priority to low)
                'fighter':['Str', 'Con', 'Cha', 'Dex', 'Wis', 'Int'],
                'rogue'  :['Dex','Int','Wis', 'Con', 'Str', 'Cha'],
                'wizard'   :['Int', 'Dex', 'Con', 'Wis', 'Cha', 'Str'],
                'barbarian' :['Str', 'Dex', 'Con', 'Wis', 'Chr', 'Int'],
                'paladin' :['Chr', 'Str', 'Wis', 'Con', 'Int', 'Dex'],
                'sorcerer' :['Chr', ''],
                'bard' :[],
                'cleric' :[],
                'druid' :[],
                'monk' :[],
                'ranger' :[],

                }

ability_adjustment = {
                    'dwarf': {'Con': 2, 'Cha': -2},
                    'elf': {'Dex': 2, 'Con': -2},
                    'gnome':{'Con': 2, 'Str': -2},
                    'half-orc': {'Str': 2, 'Int': -2, 'Chr': -2},
                    }

"""
Data regarding player characters. In the future they should be converted
into xmls.
"""

races = ["human", "elf", "dwarf", "gnome", "half-elf", "half-orc", "halfling"]


# Fixed ability order that should be used any time
ability_names = ['Str', 'Dex', 'Con', 'Int', 'Wis', 'Cha']

ability_best = {
# Manually created list of best order of abilities for a given class
# The order can be adjusted
# Descending order (from high priority to low)
                'fighter'   :['Str', 'Con', 'Cha', 'Dex', 'Wis', 'Int'],
                'rogue'     :['Dex', 'Int', 'Wis', 'Str', 'Con', 'Cha'],
                'wizard'    :['Int', 'Wis', 'Cha', 'Con', 'Dex', 'Str'],
                'barbarian' : None, #Done
                'paladin'   :['Con', 'Str', 'Wis', 'Cha', 'Int', 'Dex'],
                'sorcerer'  :['Cha', 'Int', 'Con', 'Dex', 'Str', 'Wis'],
                'bard'      : None,
                'cleric'    : None,
                'druid'     :['Wis', 'Int', 'Dex', 'Cha', 'Con', 'Str'],
                'monk'      :['Wis', 'Dex', 'Str', 'Con', 'Int', 'Cha'],
                'ranger'    :['Dex', 'Str', 'Wis', 'Con', 'Int', 'Cha'],

                }

ability_adjustment = {
                    'dwarf'   : {'Con': 2, 'Cha':-2},
                    'elf'     : {'Dex': 2, 'Con':-2},
                    'gnome'   : {'Con': 2, 'Str':-2},
                    'half-orc': {'Str': 2, 'Int':-2, 'Chr':-2},
                    }

saves = {
        '001_3': [0,0,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6],
        '233_2': [2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,12]
        }

AttackBonuses = {
                '011_12':[  [0],
                            [1],
                            [1],
                            [2],
                            [2],
                            [3],
                            [3],
                            [4],
                            [4],
                            [5],
                            [5],
                            [6, 1],
                            [6, 1],
                            [7, 2],
                            [7, 2],
                            [8, 3],
                            [8, 3],
                            [9, 4],
                            [9, 4],
                            [10, 5]
                            ],
                '012_8':[   [0],
                            [1],
                            [2],
                            [3],
                            [3],
                            [4],
                            [5],
                            [6, 1],
                            [6, 1],
                            [7, 2],
                            [8, 3],
                            [9, 4],
                            [9, 4],
                            [10, 5],
                            [11, 6, 1],
                            [12, 7, 2],
                            [12, 7, 2],
                            [13, 8, 3],
                            [14, 9, 4],
                            [15, 10, 5]
                            ],
                '123_6':[   [1],
                            [2],
                            [3],
                            [4],
                            [5],
                            [6, 1],
                            [7, 2],
                            [8, 3],
                            [9, 4],
                            [10, 5],
                            [11, 6, 1],
                            [12, 7, 2],
                            [13, 8, 3],
                            [14, 9, 4],
                            [15, 10, 5],
                            [16, 11, 6, 5],
                            [17, 12, 7, 6],
                            [18, 13, 8, 7],
                            [19, 14, 9, 8],
                            [20, 15, 10, 9]
                            ],

                }

classes = {
            'barbarian': {
                'AbilitiesOrder': ['Str', 'Dex', 'Con', 'Cha', 'Wis', 'Int'],
                'SavesLvls':["233_2", "001_3", "001_3"],
                'ClassSkills': ['Climb', 'Craft', 'Handle Animal', 'Intimidate',
                                    'Jump', 'Listen','Ride', 'Survival', 'Swim'],
                'SkillPointsModifier': 2,
                'HitDie': {'sides': 12, 'rolls': 1, 'bonus': 0},
                'AttackBonuses': '123_6',
                'Special': [    ['Fast movement, iliteracy, rage 1/day'],
                                ['Uncanny dodge'],
                                ['Trap sense +1'],
                                ['Rage 2/day'],
                                ['Improved uncanny dodge'],
                                ['Trap sense +2'],
                                ['Damage reduction 1/-'],
                                ['Rage 3/day'],
                                ['Trap sense +3'],
                                ['Damage reduction 2/-'],
                                ['Greater rage'],
                                ['Rage 3/day, Trap sense +4'],
                                ['Damage reduction 3/-'],
                                ['Indomitable will'],
                                ['Trap sense +5'],
                                ['Damage reduction 4/-, Rage 5/day'],
                                ['Tireless rage'],
                                ['Trap sense +6'],
                                ['Damage reduction 5/-'],
                                ['Mighty rage, Rage 6/day']]
            },
            'bard': {
                'AbilitiesOrder': ['Cha', 'Dex', 'Int', 'Con', 'Str', 'Wis'],
                'SavesLvls':["001_3", "233_2", "233_2"],
                'ClassSkills': ['Appraise', 'Balance', 'Bluff', 'Climb',
                                'Concentration', 'Craft', 'Decipher Script',
                                'Diplomacy', 'Disguise', 'Escape Artist',
                                'Gather Information', 'Hide', 'Jump', 'Knowledge(all)',
                                'Listen', 'Move Silently', 'Perform', 'Profession',
                                'Sense Motive', 'Sleight of Hand', 'Speak Language',
                                'Spellcraft', 'Swim', 'Tumble', 'Use Magic Device'],
                'SkillPointsModifier': 6,
                'HitDie': {'sides': 6, 'rolls': 1, 'bonus': 0},
                'AttackBonuses': '012_8',
                'Special': [    ['Bardic music, bardic knowledge, countersong, ',
                                'fascinate, inspire courage +1'],
                                ['-'],
                                ['Inspire competence'],
                                ['-'],
                                ['-'],
                                ['Suggestion'],
                                ['-'],
                                ['Inspire courage +2'],
                                ['Inspire greatness'],
                                ['-'],
                                ['-'],
                                ['Song of freedom'],
                                ['-'],
                                ['Inspire courage +3'],
                                ['Inspire heroics'],
                                ['-'],
                                ['-'],
                                ['Mass suggestion'],
                                ['-'],
                                ['Inspire courage +4']
                                ]
            },
            'cleric': {
                'AbilitiesOrder': ['Wis', 'Con', 'Cha', 'Int', 'Str', 'Dex'],
                'SavesLvls': ["233_2", "001_3", "233_2"],
                'ClassSkills': ['Concentration', 'Craft', 'Diplomacy', 'Heal',
                                'Knowledge(arcana)', 'Knowledge(history)',
                                'Knowledge(religion)', 'Knowledge(planes)',
                                'Profession', 'Spellcraft', 'ADDITIONAL SKILLS'],
                'SkillPointsModifier': 2,
                'HitDie': {'sides': 8, 'rolls': 1, 'bonus': 0},
                'AttackBonuses': '012_8',
                'Special': [    ['Turn or rebuke undead'],
                                ['-']
                                ]
            },
}

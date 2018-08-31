from random import randrange
from weighted_list import *
from basic_m_item_tables import *
from basic_spell_tables import *

TREASURE_TABLE = {## LAIR TREASURES
                  'A' : {'cp':[25,'1D6'  ], 'sp':[30,'1D6'  ], 'ep':[20, '1D4'  ], 'gp':[35, '2D6'  ], 'pp':[25,'1D2'  ], 'gems':[50,'6D6'  ],                           'magic items':[30,'Any 3']                                      },
                  'B' : {'cp':[50,'1D8'  ], 'sp':[25,'1D6'  ], 'ep':[25, '1D4'  ], 'gp':[25, '1D3'  ],                    'gems':[25,'1D6'  ],                           'magic items':[10,'1 sword, armor, or weapon']                  },
                  'C' : {'cp':[20,'1D12' ], 'sp':[30,'1D4'  ], 'ep':[10, '1D4'  ],                                        'gems':[25,'1D4'  ],                           'magic items':[10,'Any 2']                                      },
                  'D' : {'cp':[10,'1D8'  ], 'sp':[15,'1D12' ],                     'gp':[60, '1D6'  ],                    'gems':[30,'1D8'  ],                           'magic items':[15,'Any 2 + 1 potion']                           },
                  'E' : {'cp':[ 5,'1D10' ], 'sp':[30,'1D12' ], 'ep':[25, '1D4'  ], 'gp':[25, '1D8'  ],                    'gems':[10,'1D10' ],                           'magic items':[25,'Any 3 + 1 scroll']                           },
                  'F' : {                   'sp':[10,'2D10' ], 'ep':[20, '1D8'  ], 'gp':[45, '1D12' ], 'pp':[30,'1D3'  ], 'gems':[20,'2D12' ], 'more gems':[10, '1D12'], 'magic items':[30,'Any 3 except weapons + 1 potion + 1 scroll'] },
                  'G' : {                                                          'gp':[50,'10D4'  ], 'pp':[50,'1D6'  ], 'gems':[25,'3D6'  ], 'more gems':[25, '1D10'], 'magic items':[35,'Any 4 + 1 scroll']                           },
                  'H' : {'cp':[25,'3D8'  ], 'sp':[50,'1D100'], 'ep':[50,'10D4'  ], 'gp':[50,'10D6'  ], 'pp':[25,'5D4'  ], 'gems':[50,'1D100'], 'more gems':[50,'10D4' ], 'magic items':[15,'Any 4 + 1 potion + 1 scroll']                },
                  'I' : {                                                                              'pp':[30,'1D8'  ], 'gems':[50,'2D12' ],                           'magic items':[15,'Any 1']                                      },
                  'J' : {'cp':[25,'1D4'  ], 'sp':[10,'1D3'  ]                                                                                                                                                                            },
                  'K' : {                   'sp':[30,'1D6'  ], 'ep':[10, '1D10']                                                                                                                                                         },
                  'L' : {                                                                                                 'gems':[50,'1D4'  ]                                                                                            },
                  'M' : {                                                          'gp':[40, '2D4'  ], 'pp':[50,'5D6'  ], 'gems':[55,'5D4'  ], 'more gems':[45, '2D6' ]                                                                  },
                  'N' : {                                                                                                                                                'magic items':[40,'2D4 potions']                                },
                  'O' : {                                                                                                                                                'magic items':[50,'1D4 scrolls']                                },
                  ## INDIVIDUAL TREASURES
                  'P' : {'cp':[100,'3D8']},
                  'Q' : {'sp':[100,'3D6']},
                  'R' : {'ep':[100,'2D6']},
                  'S' : {'gp':[100,'2D4']},
                  'T' : {'pp':[100,'1D6']},
                  'U' : {'cp':[10,'1D100'], 'sp':[10,'1D100'],                     'gp':[ 5, '1D100'],                    'gems':[ 5,'1D4'  ],                           'magic items':[ 2,'Any 1']},
                  'V' : {                   'sp':[10,'1D100'], 'ep':[10, '1D100'], 'gp':[10, '1D100'], 'pp':[ 5,'1D100'], 'gems':[10,'1D4'  ],                           'magic items':[ 5,'Any 1']}}

COIN_XP = {'cp':0.01, 'sp':0.1, 'ep':0.5, 'gp':1, 'pp':10}

SPELL_CLASS_TABLE = WeightedList({'magic user': 3,
                                  'cleric':     1})

MU_SPELL_LEVEL_TABLE = WeightedList({'level 1': 3,
                                     'level 2': 2,
                                     'level 3': 1})

CL_SPELL_LEVEL_TABLE = WeightedList({'level 1': 3,
                                     'level 2': 2})

MAGIC_ITEM_TABLE = WeightedList({'sword':           4,
                                 'armor/weapon':    4,
                                 'potion':          5,
                                 'scroll':          4,
                                 'ring':            1,
                                 'wand/staff/rod':  1,
                                 'miscellaneous':   1})

GEM_VALUE_TABLE = WeightedList({  '10': 4,
                                  '50': 5,
                                 '100': 6,
                                 '500': 4,
                                '1000': 1})

def roll(roll_str):
    result = 0
    args = roll_str.casefold().split('d')
    if len(args) == 2:
        for i in range(int(args[0])):
            result += randrange(1,int(args[1])+1)
    return result

def random_magic_item(only_weapons = False, no_weapons = False):
    look_up_table = MAGIC_ITEM_TABLE
    if no_weapons:
        look_up_table['sword'] = 0
        look_up_table['armor/weapon'] = 0
    if only_weapons:
        look_up_table['potion'] = 0
        look_up_table['scroll'] = 0
        look_up_table['ring'] = 0
        look_up_table['wand/staff/rod'] = 0
        look_up_table['miscellaneous'] = 0
        
    item_type = look_up_table.get_random()
    if   item_type == 'sword':          return MAGIC_SWORD_TABLE.get_random()
    elif item_type == 'armor/weapon':   return MAGIC_WEAP_ARM_TABLE.get_random()
    elif item_type == 'potion':         return POTION_TABLE.get_random()
    elif item_type == 'scroll':         return get_random_scroll()
    elif item_type == 'ring':           return RING_TABLE.get_random()
    elif item_type == 'wand/staff/rod': return WSR_TABLE.get_random()
    elif item_type == 'miscellaneous':  return MISC_MAGIC_TABLE.get_random()

def get_random_scroll():
    scroll = SCROLL_TABLE.get_random()
    if 'spell scroll' in scroll:
        num_spells = int(scroll.split(':')[1].split(' ')[1])
        spell_class = SPELL_CLASS_TABLE.get_random()

        if   spell_class == 'magic user':
            spell_level = MU_SPELL_LEVEL_TABLE.get_random()
            if   spell_level == 'level 1': spell_look_up = SPELL_TABLE_MU1
            elif spell_level == 'level 2': spell_look_up = SPELL_TABLE_MU2
            elif spell_level == 'level 3': spell_look_up = SPELL_TABLE_MU3
        elif spell_class == 'cleric':
            spell_level = CL_SPELL_LEVEL_TABLE.get_random()
            if   spell_level == 'level 1': spell_look_up = SPELL_TABLE_CL1
            elif spell_level == 'level 2': spell_look_up = SPELL_TABLE_CL2

        spells = ''
        for i in range(num_spells):
            spells += spell_look_up.get_random() + ', '
        spells = spells[:-2]

        num_spells_str = str(num_spells) + ' ' + spell_class + ' spells'
        if num_spells == 1: num_spells_str = num_spells_str[:-1]
        scroll = 'spell scroll (' + num_spells_str + ', ' + spell_level + '): ' + spells
            
    return(scroll)

def detail_magic(t_type):
    result = []
    if   t_type == 'A':
        for i in range(3): result += [random_magic_item()]
    elif t_type == 'B':
        result += [random_magic_item(only_weapons = True)]
    elif t_type == 'C':
        for i in range(2): result += [random_magic_item()]
    elif t_type == 'D':
        for i in range(2): result += [random_magic_item()]
        result += [POTION_TABLE.get_random()]
    elif t_type == 'E':
        for i in range(3): result += [random_magic_item()]
        result += [get_random_scroll()]
    elif t_type == 'F':
        for i in range(3): result += [random_magic_item(no_weapons = True)]
        result += [POTION_TABLE.get_random()]
        result += [get_random_scroll()]
    elif t_type == 'G':
        for i in range(4): result += [random_magic_item()]
        result += [get_random_scroll()]
    elif t_type == 'H':
        for i in range(4): result += [random_magic_item()]
        result += [POTION_TABLE.get_random()]
        result += [get_random_scroll()]
    elif t_type == 'I':
        result += [random_magic_item()]
    elif t_type == 'N':
        for i in range(randrange(2,8)): result += [POTION_TABLE.get_random()]
    elif t_type == 'O':
        for i in range(randrange(1,5)): result += [get_random_scroll()]
    elif t_type == 'U':
        result += [random_magic_item()]
    elif t_type == 'V':
        result += [random_magic_item()]
    return(result)

def print_table(t_type):
    treasure = TREASURE_TABLE[t_type]
    for i in treasure:
        if treasure[i]:
            if (t_type < 'P') and (i in ['cp','sp','ep','gp','pp']):
                mult = 'x1000 '
            else:
                mult = ''
            chance = str(treasure[i][0]) + '%'
            print(chance, 'chance of', treasure[i][1], mult + i)
        else:
            print('No', i)

def generate_treasure(t_type):
    treasure = TREASURE_TABLE[t_type]
    result = []
    xp = 0
    for i in treasure:
        if treasure[i]:
            if (t_type < 'P') and (i in ['cp','sp','ep','gp','pp']): mult = 1000
            else: mult = 1
            if randrange(0,100) < treasure[i][0]:
                item = i
                if item == 'magic items': result += detail_magic(t_type)
                else:
                    if item == 'more gems': item = 'gems'
                    count = roll(treasure[i][1])*mult
                    result += [(str(count) + ' ' + item)]
                    if item in COIN_XP: xp += COIN_XP[item]*count
                    if 'gems' in i:
                        gem_value = GEM_VALUE_TABLE.get_random()
                        result[-1] += ' worth ' + gem_value + ' gp'
                        xp += int(gem_value)
    result += [('Total XP Value: ' + str(xp))]
    return(result)

def print_treasure(treasure):
    if len(treasure) == 0: print('No treasure')
    else:
        for i in treasure: print(i)

def gen_and_print(t_type):
    print_treasure(generate_treasure(t_type))

if __name__ == "__main__":
    for i in TREASURE_TABLE:
        print('----- TREASURE', i, '-----')
        gen_and_print(i)

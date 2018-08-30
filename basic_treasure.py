## This module collects and references the treasure tables from the
##   Moldvay Basic D&D Rules Set.
##
##                                           +----------------------------+   
## You can print out a treasure type with:   | print_table(treasure_type) |
## This lets you roll the dice for yourself  +----------------------------+
##
##                                           +------------------------------+
## If you want the dice rolled for you, use: | gen_and_print(treasure_type) |
##                                           +------------------------------+
##
## If you want to manipulate the treasure in some way, you can get it as a list
##   using the command: +---------------------------+
##                      | generate_treasure(t_type) |
##                      +---------------------------+
## Note that the last entry in this list is the total xp value of the treasure
##
##
## You can generate individual magical items with:
##   +-----------------+-------------------------------+
##   |         Command | Item Type                     |
##   +-----------------+-------------------------------+
##   |      rand_any() | randomly generated type       |
##   |  rand_m_sword() | magical sword                 |
##   |    rand_m_arm() | magical armor or misc. weapon |
##   |   rand_scroll() | scroll                        |
##   |   rand_potion() | potion                        |
##   |     rand_ring() | ring                          |
##   |      rand_wsr() | wand, staff, or rod           |
##   |     rand_misc() | misc. magic item              |
##   +-----------------+-------------------------------+
##
##
## Use this at your own risk. There is no error correction or garbage collection.
## I wrote this for use with a Slack bot, which I'm not distributing at this time
##   because the code is cobbled together garbage. If you want to integrate this
##   into a Slack bot, I recommend you do it! It's great! Slack + Hangouts is my
##   preferred way to play old-school D&D online. If you want to try it out, you'll
##   do better to get instructions on how to set up a Slack bot from a Google search
##   than from me.



## Distributed under the MIT License - Copyright 2018 Rabi Fiotto
##
## Permission is hereby granted, free of charge, to any person obtaining a copy of this
##   software and associated documentation files (the "Software"), to deal in the Software
##   without restriction, including without limitation the rights to use, copy, modify,
##   merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
##   permit persons to whom the Software is furnished to do so, subject to the following
##   conditions:
##
## The above copyright notice and this permission notice shall be included in all copies
##   or substantial portions of the Software.
##
## THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
##   INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
##   PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE
##   FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
##   OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
##   DEALINGS IN THE SOFTWARE.



from random import randrange

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

MAGIC_SWORD_TABLE = ['sword +1',
                     'sword +1 (+2 against lycanthropes)',
                     'sword +1 (+2 against spell users)',
                     'sword +1 (+3 against undead)',
                     'sword +1 (+3 against dragons)',
                     'sword +1 (casts Light on command)',
                     'sword -1 (cursed)']

MAGIC_WEAP_ARM_TABLE = ['arrows +1 (x10)',
                        'axe +1',
                        'dagger +1',
                        'mace +1',
                        'armor +1',
                        'shield +1',
                        'armor +1 & shield +1',
                        'cursed armor (AC9, looks like +1)']

POTION_TABLE = ['potion of diminution',
                'potion of ESP',
                'potion of gasseous form',
                'potion of growth',
                'potion of healing',
                'potion of invisibility',
                'potion of levitation',
                'potion of poison']

SCROLL_TABLE = ['spell scroll: 1 spell',
                'spell scroll: 2 spells',
                'spell scroll: 3 spells',
                'cursed scroll',
                'scroll of protection from lycanthropes',
                'scroll of protection from undead',
                'treasure map: 1D4 x1000 gp treasure',
                'treasure map: magic item']

RING_TABLE = ['ring of animal control',
              'ring of fire resistance',
              'ring of invisibility',
              'ring of protection +1',
              'ring of water walking',
              'ring of weakness']

WSR_TABLE = ['wand of enemy detection',
             'wand of magic detection',
             'wand of paralyzation',
             'staff of healing',
             'snake staff',
             'rod of cancellation']

MISC_MAGIC_TABLE = ['bag of devouring',
                    'bag of holding',
                    'broom of flying',
                    'crystal ball',
                    'elven cloak & boots',
                    'gauntlets of ogre power',
                    'helm of alignment changing',
                    'helm of telepathy',
                    'medallion of ESP',
                    'rope of climbing']

SPELL_TABLE_MU1 = ['Charm Person',
                   'Detect Magic',
                   'Floating Disc',
                   'Hold Portal',
                   'Light',
                   'Magic Missile',
                   'Protection from Evil',
                   'Read Languages',
                   'Read Magic',
                   'Shield',
                   'Sleep',
                   'Ventriloquism']

SPELL_TABLE_MU2 = ['Continual Light',
                   'Detect Evil',
                   'Detect Invisible',
                   'ESP',
                   'Invisibility',
                   'Knock',
                   'Levitate',
                   'Locate Object',
                   'Mirror Image',
                   'Phantasmal Force',
                   'Web',
                   'Wizard Lock']

SPELL_TABLE_MU3 = ['Dispel Magic',
                   'Fire Ball',
                   'Fly']

SPELL_TABLE_CL1 = ['Cure Light Wounds',
                   'Detect Evil',
                   'Detect Magic',
                   'Light',
                   'Protection from Evil',
                   'Purify Food and Water',
                   'Remove Fear',
                   'Resist Cold']

SPELL_TABLE_CL2 = ['Bless',
                   'Hold Person',
                   "Silence 15' Radius"]

def roll(roll_str):
    result = 0
    args = roll_str.casefold().split('d')
    if len(args) == 2:
        for i in range(int(args[0])):
            result += randrange(1,int(args[1])+1)
    return result

def rand_spell_mu():
    rnum = randrange(0,6)
    if   rnum < 3: return(SPELL_TABLE_MU1[randrange(0,len(SPELL_TABLE_MU1))] + '(MU1)')
    elif rnum < 5: return(SPELL_TABLE_MU2[randrange(0,len(SPELL_TABLE_MU2))] + '(MU2)')
    else:          return(SPELL_TABLE_MU3[randrange(0,len(SPELL_TABLE_MU3))] + '(MU3)')

def rand_spell_cl():
    rnum = randrange(0,5)
    if   rnum < 3: return(SPELL_TABLE_CL1[randrange(0,len(SPELL_TABLE_CL1))] + '(CL1)')
    elif rnum < 5: return(SPELL_TABLE_CL2[randrange(0,len(SPELL_TABLE_CL2))] + '(CL2)')

def rand_magic_type(num = None):
    if not(num): num = randrange(0,100)
    if   num < 20: return('sword')
    elif num < 40: return('armor/weapon')
    elif num < 65: return('potion')
    elif num < 85: return('scroll')
    elif num < 90: return('ring')
    elif num < 95: return('wand/staff/rod')
    else:          return('miscellaneous')

def rand_m_sword():
    rnum = randrange(0,len(MAGIC_SWORD_TABLE))
    return(MAGIC_SWORD_TABLE[rnum])
    
def rand_m_arm():
    rnum = randrange(0,len(MAGIC_WEAP_ARM_TABLE))
    return(MAGIC_WEAP_ARM_TABLE[rnum])
    
def rand_potion():
    rnum = randrange(0,len(POTION_TABLE))
    return(POTION_TABLE[rnum])
    
def rand_scroll():
    rnum = randrange(0,len(SCROLL_TABLE))
    if   rnum <  3:
        if randrange(0,4) == 0: spell_type = 'cleric'
        else:                   spell_type = 'magic user'
    if   rnum == 0:
        if spell_type == 'cleric': return('spell scroll: ' + rand_spell_cl())
        else:                      return('spell scroll: ' + rand_spell_mu())
    elif rnum == 1:
        if spell_type == 'cleric': return('spell scroll: ' + rand_spell_cl() + ' & ' + rand_spell_cl())
        else:                      return('spell scroll: ' + rand_spell_mu() + ' & ' + rand_spell_mu())
    elif rnum == 2:
        if spell_type == 'cleric': return('spell scroll: ' + rand_spell_cl() + ', '  + rand_spell_cl() + ', & ' + rand_spell_cl())
        else:                      return('spell scroll: ' + rand_spell_mu() + ', '  + rand_spell_mu() + ', & ' + rand_spell_mu())
    else: return(SCROLL_TABLE[rnum])
    
def rand_ring():
    rnum = randrange(0,len(RING_TABLE))
    return(RING_TABLE[rnum])
    
def rand_wsr():
    rnum = randrange(0,len(WSR_TABLE))
    return(WSR_TABLE[rnum])
    
def rand_misc():
    rnum = randrange(0,len(MISC_MAGIC_TABLE))
    return(MISC_MAGIC_TABLE[rnum])

def rand_any(num = None):
    rtype = rand_magic_type(num)
    if   rtype == 'sword':          return rand_m_sword()
    elif rtype == 'armor/weapon':   return rand_m_arm()
    elif rtype == 'potion':         return rand_potion()
    elif rtype == 'scroll':         return rand_scroll()
    elif rtype == 'ring':           return rand_ring()
    elif rtype == 'wand/staff/rod': return rand_wsr()
    elif rtype == 'miscellaneous':  return rand_misc()

def get_gem_value():
    rnum = randrange(0,100)
    if   rnum < 20: return(  10)
    elif rnum < 45: return(  50)
    elif rnum < 75: return( 100)
    elif rnum < 95: return( 500)
    else:           return(1000)

def detail_magic(t_type):
    result = []
    if   t_type == 'A':
        for i in range(3): result += [rand_any()]
    elif t_type == 'B':
        rnum = randrange(0,40)
        result += [rand_any(rnum)]
    elif t_type == 'C':
        for i in range(2): result += [rand_any()]
    elif t_type == 'D':
        for i in range(2): result += [rand_any()]
        result += [rand_potion()]
    elif t_type == 'E':
        for i in range(3): result += [rand_any()]
        result += [rand_scroll()]
    elif t_type == 'F':
        for i in range(3):
            rnum = randrange(40,100)
            result += [rand_any(rnum)]
        result += [rand_potion()]
        result += [rand_scroll()]
    elif t_type == 'G':
        for i in range(4): result += [rand_any()]
        result += [rand_scroll()]
    elif t_type == 'H':
        for i in range(4): result += [rand_any()]
        result += [rand_potion()]
        result += [rand_scroll()]
    elif t_type == 'I':
        result += [rand_any()]
    elif t_type == 'N':
        for i in range(randrange(2,8)): result += [rand_potion()]
    elif t_type == 'O':
        for i in range(randrange(1,5)): result += [rand_scroll()]
    elif t_type == 'U':
        result += [rand_any()]
    elif t_type == 'V':
        result += [rand_any()]
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
                        gem_value = get_gem_value()
                        result[-1] += ' worth ' + str(gem_value) + ' gp'
                        xp += gem_value
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

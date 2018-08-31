from weighted_list import *

MAGIC_SWORD_TABLE = WeightedList({'sword +1':                           1,
                                  'sword +1 (+2 against lycanthropes)': 1,
                                  'sword +1 (+2 against spell users)':  1,
                                  'sword +1 (+3 against undead)':       1,
                                  'sword +1 (+3 against dragons)':      1,
                                  'sword +1 (casts Light on command)':  1,
                                  'sword +2':                           1,
                                  'sword -1 (cursed)':                  1})

MAGIC_WEAP_ARM_TABLE = WeightedList({'arrows +1 (x10)':                     1,
                                     'axe +1':                              1,
                                     'dagger +1':                           1,
                                     'mace +1':                             1,
                                     'armor +1':                            1,
                                     'shield +1':                           1,
                                     'armor +1 & shield +1':                1,
                                     'cursed armor (AC9, looks like +1)':   1})

POTION_TABLE = WeightedList({'potion of diminution':    1,
                             'potion of ESP':           1,
                             'potion of gasseous form': 1,
                             'potion of growth':        1,
                             'potion of healing':       1,
                             'potion of invisibility':  1,
                             'potion of levitation':    1,
                             'potion of poison':        1})

SCROLL_TABLE = WeightedList({'spell scroll: 1 spell':                   1,
                             'spell scroll: 2 spells':                  1,
                             'spell scroll: 3 spells':                  1,
                             'cursed scroll':                           1,
                             'scroll of protection from lycanthropes':  1,
                             'scroll of protection from undead':        1,
                             'treasure map: 1D4 x1000 gp treasure':     1,
                             'treasure map: magic item':                1})

RING_TABLE = WeightedList({'ring of animal control':    1,
                           'ring of fire resistance':   1,
                           'ring of invisibility':      1,
                           'ring of protection +1':     1,
                           'ring of water walking':     1,
                           'ring of weakness':          1})

WSR_TABLE = WeightedList({'wand of enemy detection':    1,
                          'wand of magic detection':    1,
                          'wand of paralyzation':       1,
                          'staff of healing':           1,
                          'snake staff':                1,
                          'rod of cancellation':        1})

MISC_MAGIC_TABLE = WeightedList({'bag of devouring':            1,
                                 'bag of holding':              1,
                                 'broom of flying':             1,
                                 'crystal ball':                1,
                                 'elven cloak & boots':         1,
                                 'gauntlets of ogre power':     1,
                                 'helm of alignment changing':  1,
                                 'helm of telepathy':           1,
                                 'medallion of ESP':            1,
                                 'rope of climbing':            1})

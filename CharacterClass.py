##########################################################################
# Dependencies
##########################################################################
from FighterSubClass import *
from ClericSubClass import *
from MageSubClass import *

########################################################################
# Character Class
########################################################################
class Character():
    def __init__(self,choice):                                          # Init Function                                      
        if choice == "M": Mage.__init__(self)                           # Init Mage Class
        if choice == "F": Fighter.__init__(self)                        # Init Fighter Class
        if choice == "C": Cleric.__init__(self)                         # Init Cleric Class
        self.weapons = {"Sword":1}                                      # Dict to store weapons
        self.armor = {"Clothes": 1}                                     # Dict to store armor
        self.items = {"Potion": 1}                                      # Dict to store items
        self.inventory = {"Weapons":self.weapons,"Armor":self.armor,"Items":self.items} # Dict to stoe all inventory structs
    
    def printStats(self):                                               # printStats function
        print(self.stats)                                               # Prints all player stats
        
##########################################################################
# Dependencies
##########################################################################
from CharacterClass import *
from Menu import *

##########################################################################
# Player Creation
##########################################################################
def createPlayer():
    result = False
    while result == False:
        playerClass = input("(F)ighter, (M)age, or (C)leric?: ")
        if playerClass == "M" or playerClass == "F" or playerClass == "C": 
            player = Character(playerClass)
            result = True
        else: print("Not a valid response.")
    del result
    return player

##########################################################################
# Main
##########################################################################
def main():
    player = createPlayer()
    openMenu(player)

if __name__ == "__main__":
    main()


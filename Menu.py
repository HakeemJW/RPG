######################################################
# Player initiated Game Exit
######################################################
def Exit(player):
    x = input('Would you like to save the game?:  ')    # Prompts player choice to save game
    if x == 'Y':
        print("Saving...")                              # "Saving" state
        file = open("save.txt","a")                     # Creates/Opens save file
        file.write(str(player.stats))                   # Writes player stats to save file
        file.write(str(player.inventory))               # Writes player inventory to save file
        file.close()                                    # Closes save data file
        print("Game Saved!")                            # "Successful Save" state 
        print("Exiting...")                             # "Closing Game" state
        return
    else: 
        print("Exiting...")                             # "Closing Game" state
        return

######################################################
# Player Inventory
######################################################
def Inventory(player):
    for key in player.inventory:
        print(player.inventory[key])                    # Prints dictionaries stored in inventory list

######################################################
# Game Options (not implemented)
######################################################
def Options():
    print('Thre are no options at this time:')          # Working on it

######################################################
# Player Summary
######################################################
def playerSummary(player):
    print(player.stats)                                 # Prints palyer stats

######################################################
# Opens Menu
######################################################
def openMenu(player):
    playerSummary(player)                                        
    x = input("(1) Player Summary | (2) Inventory | (3) Options | (4) Exit")
    if x == "1": playerSummary(player)
    elif x == "2": Inventory(player)
    elif x == "3": Options()
    elif x == "4": Exit(player)
    else: print("Not a valid option")
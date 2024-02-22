import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3

""" print(RPS(2))
print(RPS.ROCK)
print(RPS['ROCK'])
print(RPS.ROCK.value)
sys.exit() """

playagain = True

while playagain:    
    playerchoice = input("\nEnter...\n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")

    player = int(playerchoice)

    if player < 1 or player > 3:
        sys.exit("You must enter 1, 2, or 3.")
                
    computerchoice = random.choice("123")

    computer = int(computerchoice)

    print("\nYou chose " + str(RPS(player)).replace('RPS.',"") + ".")
    print("Python chose " + str(RPS(computer)).replace('RPS.',"") + ".\n")

    if player == 1 and computer == 3:
        print("You win!")
    elif player == 2 and computer == 1:
        print("You win!")
    elif player == 3 and computer == 2:
        print("You win!")
    elif player == computer:
        print("Tie game!")
    else:
        print("Python wins!")

    continuegame = input("Do you want to play again?\n 0 for no\n 1 for yes\n\n")
    
    if continuegame == '0' or continuegame == '1':
        continuegameInt = int(continuegame)
        playagain = bool(continuegameInt)
    else:
        playagain = False
sys.exit("Bye!")

""" playagain = input("\Play again? \nY for Yes or \Q for Quit \n\n")
    if playagain.lower() == "y":
       continue
    else:
        print("\nlets go")
        print("Thank you for playing")
        playagain = False
    print("")
print("The game was ended by the player - what a bad looser") """

                         




            


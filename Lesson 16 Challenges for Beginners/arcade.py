from guess_number import guess_number
from rps import rps
import sys


def arcade_menu(name='PlayerOne'):
    welcome_back = False

    while True:
        if welcome_back == True:
            print(f"\n{name}, welcome back to the Arcade menu.")

        playerchoice = input(f"Please choose a game:\n1 = Rock Paper Scissors\n2 = Guess my Number or\nX = exit the Arcade\n")
        
        if playerchoice not in ["1", "2", "x", "X"]:
           print(f"\n{name}, please enter 1, 2, or x.")
           return arcade_menu(name)

        welcome_back = True    

        if playerchoice == "1":
            rock_paper_scissors = rps(name)
            rock_paper_scissors()
        elif playerchoice == "2":
            guess_my_number = guess_number(name)
            guess_my_number()
        else:
            print(f"Bye {name}, thank you for playing the Arcade and see ya!")
            sys.exit(f"Bye {name}! 👋")

    


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )


    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person playing the game."
    )

    args = parser.parse_args()

    print(f"\n{args.name}, welcome to the Arcade!")

    """ arcade_menu = arcade_menu(args.name) #play variable needed to hold the return play_rps. """
    arcade_menu(args.name)
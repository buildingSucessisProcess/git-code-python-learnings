import random


def guess_number(name='PlayerOne'):

    gamecount = 0
    playerwins = 0

    def play_guess_number():
        nonlocal name
        nonlocal gamecount
        nonlocal playerwins

        playerchoice = input(f"{name}, guess which number I'm thinking of...1, 2 or 3.\n")

        while playerchoice not in ["1", "2", "3"]:
            playerchoice = input(f"{name}, guess which number I'm thinking of...1, 2 or 3.")
        
        playerchoiceint = int(playerchoice)

        computerchoice = random.choice("123")
        computerchoiceint = int(computerchoice)

        print(f"{name}, you choose {playerchoice}.\nI was thinking of {computerchoice}.")

        def gameresult(computerchoiceint, playerchoiceint):
            nonlocal playerwins
            nonlocal gamecount

            gamecount += 1
            if playerchoiceint == computerchoiceint:
                playerwins += 1
                return f"{name}, you win!"
            else:
                return f"{name}, you loose!"                  

        gameresult = gameresult(computerchoiceint, playerchoiceint)

        print(gameresult)
        print(f"\nGame count: {gamecount}\nYour winning percentage: {playerwins / gamecount:.2%}")

        while True:
            playagain = input(f"\nPlay again {name}?\nY for Yes or\nQ to quit\n\n")
            
            if playagain.lower() in ["q", "y"]:
                break
            else:
                continue
    
        if playagain.lower() == "y":
            return play_guess_number()
        else:
            print(f"Thank you for playing {name}!\n See ya next time!")
    
    return play_guess_number

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

    guess_my_number = guess_number(args.name) #play variable needed to hold the return play_rps. 
    guess_my_number()
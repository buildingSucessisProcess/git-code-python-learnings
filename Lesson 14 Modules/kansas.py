from random import choice

capital = "Topeka"

bird = "Western Meadowlark"

flower = "Sunflower"

song = "Home on the Range"


def randomfunfact():
    funfacts = [
        "Kansas is considered flat, but it does have a mountain.",
        "Wichita is the largest city in the state, but many would guess that it is Kansas City.",
        "A considerable portion of Kansas City is actually in Missouri.",
        "Most Kansans are annoyed by Wizard of Oz references from people outside of Kansas."
    ]

    index = choice("0123")

    print(funfacts[int(index)])


if __name__ == "__main__": # prevents when kansas module is imported and the function randomfunfact
    # is used a second run of the function
    randomfunfact()

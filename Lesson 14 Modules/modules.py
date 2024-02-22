from math import pi
import sys
import random as rdm
from enum import Enum
import kansas
from rps7 import rock_paper_scissors

print(pi)

for item in dir(rdm):
    print(item)

print(kansas.capital)
kansas.randomfunfact()

print(__name__)  # results in __main__ as this is the module running
print(kansas.__name__) # results in kansas

rock_paper_scissors()
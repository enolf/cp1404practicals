"""
CP1404/CP5632 - Practical - Florian N Eisen
Program to build a list of random integers and format accordingly
"""

import random

# predefined constants
QUICK_PICK_LIST_LENGTH = 6
MIN_QUICK_PICK = 1
MAX_QUICK_PICK = 45


picks_count = int(input("How many picks do you want? "))  # get user input for number of lists
for i in range(0, picks_count):
    quick_picks = []
    for j in range(QUICK_PICK_LIST_LENGTH):  # build list as per instructions
        random_pick = random.randint(MIN_QUICK_PICK, MAX_QUICK_PICK)
        while random_pick in quick_picks:  # avoid repeats
            random_pick = random.randint(MIN_QUICK_PICK, MAX_QUICK_PICK)
        quick_picks.append(random_pick)
        quick_picks.sort()
    print(" ".join(f"{str_picks:2}" for str_picks in quick_picks))  # print with str formatting

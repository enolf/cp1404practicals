"""
CP1404 - Practical - Florian N Eisen
Function to determine status of a score between 0 and 100
"""

from random import randint


def main():
    """Determine a grade status based on score given by user as well as a random score"""
    score = float(input("Enter score: "))
    print(get_grade(score))

    score_random = randint(1, 100)
    print("Random Score is: ", score_random)
    print(get_grade(score_random))


def get_grade(score):
    """Indicate status of input score"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()

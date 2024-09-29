"""
CP1404 - Practical - Florian N Eisen
Program to rate score via a menu selection
"""


# from score import get_grade
# how would one import the get_grade fn from score.py without the rest of the program running?


def main():
    """Take user input of a score and then query an action"""
    valid_score = get_score()
    menu = """\nWhat would you like to do with your score?
    G - Get new score
    P - Print result
    S - Show score in *s
    Q - Quit\n"""
    selection = input(menu).upper()
    while selection != "Q":
        if selection == "G":
            valid_score = get_score()
        elif selection == "P":
            print(get_grade(valid_score))
        elif selection == "S":
            print("*" * valid_score)
        else:
            print("Invalid Selection!")
        selection = input(menu).upper()
    print("Goodbye")


def get_score():
    """Get input score and check it is within the range 0 and 100"""
    valid_score = int(input("Enter your score, it must be between 0 and 100: "))
    while valid_score > 100 or valid_score < 0:
        valid_score = int(input("Enter your score again, it must be between 0 and 100: "))
    return valid_score


def get_grade(valid_score):
    """Rate the input score"""
    if valid_score < 0 or valid_score > 100:
        return "Invalid score"
    elif valid_score >= 90:
        return "Excellent"
    elif valid_score >= 50:
        return "Passable"
    else:
        return "Bad"


main()

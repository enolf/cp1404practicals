"""
CP1404/CP5632 - Practical - Florian N Eisen
Broken program to determine score status
"""


def main():
    """Determine a grade status based on score given by user"""
    score = float(input("Enter score: "))
    grade = get_grade(score)
    print(grade)


def get_grade(score):
    """Indicate status of input score"""
    if score < 0 or score > 100:
        grade = "Invalid score"
        return grade
    elif score >= 90:
        grade = "Excellent"
        return grade
    elif score >= 50:
        grade = "Passable"
        return grade
    elif score < 50:
        grade = "Bad"
        return grade


main()

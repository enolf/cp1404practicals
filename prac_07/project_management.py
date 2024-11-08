"""
CP1404 - prac_07 - Florian N Eisen
estimated: 2 hours
actual
"""

from prac_07.project import Project

MENU = """
- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit
"""


def main():

    print(MENU)
    user_input = input(">>> ").upper()
    while user_input != "Q":
        if user_input == "L":
            load_projects()
            # elif user_input == "S":
            # elif user_input == "D":
            # elif user_input == "F":
            # elif user_input == "A":
            # elif user_input == "U":
        else:
            print("Invalid Input")

        user_input = input(">>> ").upper()


def load_projects():

    projects = []
    valid_try = False
    while not valid_try:
        try:
            user_filename = str(input("Enter file name: "))
            with open(file=user_filename, mode='r') as readfile:
                readfile.readline()
                for line in readfile:
                    line.split('\t')

                    print(line)

            valid_try = True
        except FileNotFoundError or TypeError:
            print("File not found try again")
            valid_try = False

#
# def save_projects():
#
# def display_projects():
#
# def filter_projects():
#
# # def add_project():
#
# def update_project():



main()

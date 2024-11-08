"""
CP1404 - prac_07 - Florian N Eisen
estimated: 2 hours
actual
"""

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

        elif user_input == "S":
        elif user_input == "D":
        elif user_input == "F":
        elif user_input == "A":
        elif user_input == "U":
        else:
            print("Invalid Input")

        user_input = input(">>> ").upper()
def load_projects(filename):

    try:
        filename = str(input("Enter file name: "))
        with open(filename, mode='r', newline='') as readfile:
            for line in readfile:
    except TypeError:
        print("Must be a valid string")
    except FileNotFoundError:
        print("File not found try again")


def save_projects():

def display_projects():

def filter_projects():

def add_project():

def update_project():



main()

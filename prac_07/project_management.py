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

    projects = []

    print(MENU)
    user_input = input(">>> ").upper()
    while user_input != "Q":
        if user_input == "L":
            load_projects(projects)
            # elif user_input == "S":
            # print(projects)
        elif user_input == "D":
            display_projects(projects)
            # elif user_input == "F":
            # elif user_input == "A":
            # elif user_input == "U":
        else:
            print("Invalid Input")

        user_input = input(">>> ").upper()


def load_projects(projects):

    valid_try = False
    while not valid_try:
        try:
            user_filename = str(input("Enter file name: "))
            with open(file=user_filename, mode='r') as project_file:
                project_file.readline()
                for project in project_file:
                    project = project.split('\t')
                    project_object = Project(project[0], project[1], project[2], project[3], project[4])
                    # print(project_object)
                    projects.append(project_object)
                return projects
        except FileNotFoundError or TypeError:
            print("File not found try again")
            valid_try = False

#
# def save_projects():
#


def display_projects(projects):
    for project in projects:
        print(project)
#
# def filter_projects():
#
# # def add_project():
#
# def update_project():



main()

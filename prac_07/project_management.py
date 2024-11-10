"""
CP1404 - prac_07 - Florian N Eisen
estimated: 2 hours
actual: 2 hours, and going
"""

from prac_07.project import Project
import datetime

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
        elif user_input == "D":
            display_projects(projects)
        elif user_input == "F":
            filter_projects(projects)
        elif user_input == "A":
            add_project(projects)
        elif user_input == "U":
            update_project(projects)
        else:
            print("Invalid Input")

        user_input = input(">>> ").upper()


def load_projects(projects):
    """Ask user for project name and extract data in projects list"""
    valid_try = False
    while not valid_try:
        try:
            user_filename = "projects.txt"  # str(input("Enter file name: "))
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


# def save_projects():


def display_projects(projects):
    """Print objects and sort by priority"""
    if projects:  # check if projects exist
        projects.sort()  # sort by priority by define __lt__
        for project in projects:
            print(project)
    else:
        print("No projects")


def filter_projects(projects):
    """Filter projects by date, starting after given date"""
    if projects:
        try:
            input_date = input("Date to sort from (d/m/yyyy): ")
            user_date = datetime.datetime.strptime(input_date, "%d/%m/%Y").date()
            is_printed = False
            for project in projects:
                project_date = datetime.datetime.strptime(project.date, "%d/%m/%Y").date()
                if project_date >= user_date:
                    print(project)
                    is_printed = True
            if not is_printed:
                print("All projects are before that date")
        except ValueError:
            print("Invalid Date")
    else:
        print("No projects")


def add_project(projects):
    """Allow user to add a new project"""
    name = input("Enter project name: ")
    date = input("Enter the start of the project or press enter if its today (dd/mm/yyyy): ")
    if date == "":
        date = datetime.date.today()
    priority = input("Enter the priority of the project: ")
    cost = input("Enter the cost of the project: ")
    if cost == "":
        cost = 0
    completion = input("Enter the completion of the project (%): ")
    if priority == "":
        priority = 0
    project_object = Project(name, date, priority, cost, completion)
    projects.append(project_object)
    print(project_object)


def update_project(projects):
    if projects:
        for project in enumerate(projects):
            print(project)
    else:
        print("No projects")


main()

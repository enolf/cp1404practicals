"""
CP1404 - prac_07 - Florian N Eisen
estimated: 2 hours
actual: 3.5 hours
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
    """A program to use and update a project list"""
    projects = []

    print(MENU)
    user_input = input(">>> ").upper()
    while user_input != "Q":
        if user_input == "L":
            load_projects(projects)
        elif user_input == "S":
            save_projects(projects)
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
            user_filename = str(input("Enter file name: "))
            with open(file=user_filename, mode='r') as project_file:
                project_file.readline()
                for project in project_file:
                    project = project.strip().split('\t')
                    project_object = Project(project[0], project[1], project[2], project[3], project[4])
                    projects.append(project_object)
                return projects, user_filename
        except FileNotFoundError or TypeError:
            print("File not found try again")
            valid_try = False


def save_projects(projects):
    """Ask user for filename to save project list to"""
    if projects:
        valid_try = False
        while not valid_try:
            try:
                user_filename = str(input("Enter file name: "))
                with open(file=user_filename, mode='w') as project_file:
                    print(f"Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=project_file)
                    for project in projects:
                        print(f"{project.name}\t{project.date}\t{project.priority}\t{project.cost}"
                              f"\t{project.completion}", file=project_file)
                        valid_try = True
                        print(f"Saved into {project_file}")
            except FileNotFoundError or TypeError:
                print("File not found try again")
                valid_try = False
    else:
        print("No projects")


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
    """Update project's priority and completion"""
    if projects:
        print("Select a project you want to update: ")
        for project in enumerate(projects, 1):
            print(project[0], project[1])
        valid_try = False
        while not valid_try:
            try:
                project_number = int(input(""))
                valid_try = True
            except ValueError:
                print("Invalid input")
                valid_try = False
        new_priority = input(f"Update Priority {projects[project_number-1].priority}\nto: ")
        projects[project_number - 1].priority = new_priority
        new_completion = input(f"Update completion {projects[project_number - 1].completion}\nto: ")
        projects[project_number - 1].completion = new_completion
        print(f"Update project:\n{projects[project_number - 1]}")
    else:
        print("No projects")


main()

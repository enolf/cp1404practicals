"""
CP1404 - prac_07 - Florian N Eisen
program to use my guitars
"""

# import csv
from prac_07.guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Use Guitars class, allow user to add new guitars and sort them by year"""

    # initialise my_guitars list
    my_guitars = []

    # open FILENAME safely and extract data
    with open(file=FILENAME, mode='r') as readfile:
        for line in readfile:
            parts = line.split(',')
            new_guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
            my_guitars.append(new_guitar)
            print(new_guitar)

    add_new_guitar(my_guitars )

    sort_by_year(my_guitars)


def add_new_guitar(my_guitars ):
    """Add new guitar to my_guitars"""
    new_guitar_name = input("Enter new guitar name: ")
    while new_guitar_name != "":
        # accept empty inputs for year and cost and set them to zero
        try:
            new_guitar_year = int(input("Enter new guitar year: "))
        except ValueError:
            new_guitar_year = 0
        try:
            new_guitar_cost = float(input("Enter new guitar cost: "))
        except ValueError:
            new_guitar_cost = 0

        new_guitar = Guitar(new_guitar_name, new_guitar_year, new_guitar_cost)
        my_guitars .append(new_guitar)
        new_guitar_name = input("Enter new guitar name: ")
    return my_guitars


def sort_by_year(my_guitars):
    """print a sorted version based on ascending order of guitars years"""
    print("\nHere is a sorted version of the guitars based on the ascending order of years:")
    my_guitars.sort()
    for my_guitar in my_guitars:
        print(my_guitar)




main()

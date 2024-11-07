"""
CP1404 - prac_07 - Florian N Eisen
program to use my guitars
"""

# import csv
from prac_07.guitar import Guitar

FILENAME = "guitars.csv"


def main():
    my_guitars = []

    with open(file=FILENAME, mode='r') as readfile:
        for line in readfile:
            parts = line.split(',')
            new_guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
            my_guitars.append(new_guitar)
            print(new_guitar)

    # print a sorted version based on ascending order of guitars years
    print("\nHere is a sorted version of the guitars based on the ascending order of years")
    my_guitars.sort()
    for my_guitar in my_guitars:
        print(my_guitar)


main()

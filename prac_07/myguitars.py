"""
CP1404 - prac_07 - Florian N Eisen
program to use my guitars
"""

# import csv
from prac_07.guitar import Guitar


def main():
    my_guitars = []

    readfile = open(file="guitars.csv", mode='r')
    for line in readfile:
        parts = line.split(',')
        new_guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        my_guitars.append(new_guitar)
        print(new_guitar)

    my_guitars.sort()


main()

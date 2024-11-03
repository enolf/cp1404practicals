"""
estimated: 32
actual
"""

from prac_06.guitar import Guitar


def main():

    guitar = []
    guitar_name = input("Name: ")

    while guitar_name != "":
        guitar_year = int(input("Year: "))
        guitar_cost = float(input("Cost: $"))

        new_guitar = Guitar(guitar_name, guitar_year, guitar_cost)
        guitar.append(new_guitar)
        print(f"{new_guitar} added")
        guitar_name = input("Name: ")


main()

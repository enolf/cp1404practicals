"""
CP1404 - prac_06 - Florian N Eisen
estimated: 32
actual: 29
"""

from prac_06.guitar import Guitar


def main():

    guitars = []
    guitar_name = input("Name: ")

    while guitar_name != "":
        guitar_year = int(input("Year: "))
        guitar_cost = float(input("Cost: $"))

        new_guitar = Guitar(guitar_name, guitar_year, guitar_cost)
        guitars.append(new_guitar)
        print(f"{new_guitar} added")
        guitar_name = input("Name: ")

        # Guitars to test
        # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
        # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    if guitars:
        print("These are my guitar")
        for i, guitar in enumerate(guitars, 1):
            vintage_string = " (vintage)" if guitar.is_vintage() else ""
            print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
    else:
        print("Where did I leave your guitar?")


main()

from prac_06.guitar import Guitar


def main():
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    guitar = Guitar(name, year, cost)
    print(guitar)

    another_name = "Another Guitar"
    another_year = 2013

    another_guitar = Guitar(another_name, another_year)

    print(f"{guitar.name} get_age() - Expected 102. Got {guitar.get_age()}")
    print(f"{another_guitar.name} get_age() - Expected 11. Got {another_guitar.get_age()}")
    print(f"{guitar.name} is_vintage() - Expected True. Got {guitar.is_vintage()}")
    print(f"{another_guitar.name} is_vintage() - Expected False. Got {another_guitar.is_vintage()}")

main()


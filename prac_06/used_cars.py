"""
CP1404 - prac_06 - Florian N Eisen
Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car("My small car", 180)  # my_car has 180L/km of fuel
    my_car.drive(30)  # my_car drive for 30km using 1L/km fuel
    print(f"Car has fuel: {my_car.fuel}")  # prints the current fuel level
    print(my_car)  # prints __str__ method

    limo = Car("My Limousine", 100)  # create limo object
    limo.add_fuel(20)  # add 20L/km of fuel
    print(f"Limo has fuel: {limo.fuel}")  # print updated fuel level
    limo.drive(115)  # drive car for 115km
    print(limo)  # prints __str__ method


main()

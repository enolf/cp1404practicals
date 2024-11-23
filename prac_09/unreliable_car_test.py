"""
CP1404 - prac_09 - Florian N Eisen
Test UnreliableCar class
"""

from prac_09.unreliable_car import UnreliableCar


def main():
    broken_car = UnreliableCar('FIAT', 30, 16.66)  # This fiat has 30km worth of fuel and will only work 1/6 of the time
    print(broken_car.drive(10))  # does it break down a lot? Yes
    print(broken_car.fuel)


if __name__ == '__main__':
    main()

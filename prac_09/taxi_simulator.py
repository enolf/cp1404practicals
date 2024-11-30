"""
CP1404 - prac_09 - Florian N Eisen
Simulate a taxi service
"""

from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = '''q)uit, c)hoose, d)rive'''


def main():
    """Simulate a taxi service"""
    taxis = [
        Taxi('VW Kombi', 70),
        SilverServiceTaxi('TX4', 100, 1.5),
        SilverServiceTaxi('Bobby Car', 5, 5)
    ]
    current_taxi = None
    passenger_bill = 0

    user_choice = input(f'{MENU}\n').lower()
    while user_choice != 'q':
        if user_choice == 'c':
            current_taxi = choose_taxi(taxis, current_taxi)
        elif user_choice == 'd':
            passenger_bill = drive_taxi(current_taxi, passenger_bill)
        else:
            print('Invalid Option')
        print(f'Here is your bill: ${passenger_bill:.2f}')
        user_choice = input(f'{MENU}\n').lower()
    print(f'Here is your bill: ${passenger_bill:.2f}')
    print('Taxis are now:')
    display_taxis(taxis)


def choose_taxi(taxis, current_taxi):
    """Make choice of a Taxi from list"""
    display_taxis(taxis)
    try:
        taxi_choice = int(input('Choose Taxi #: '))
        current_taxi = taxis[taxi_choice - 1]
    except IndexError:
        print('Option not available')
    except ValueError:
        print('Not a number')
    return current_taxi


def display_taxis(taxis):
    """Display the taxis available"""
    for taxi in enumerate(taxis, 1):
        print(f'{taxi[0]}: {taxi[1]}')


def drive_taxi(current_taxi, passenger_bill):
    """Drive the selected taxi"""
    if current_taxi is None:
        print('Choose a taxi prior to departing')
    else:
        drive_distance = int(input('Drive distance: '))
        current_taxi.start_fare()
        current_taxi.drive(drive_distance)
        passenger_bill += current_taxi.get_fare()
    return passenger_bill


if __name__ == '__main__':
    main()

from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = '''q)uit, c)hoose, d)rive'''

def main():
    taxis = [Taxi('VW Kombi', 70), SilverServiceTaxi('TX4', 100, 1.5), SilverServiceTaxi('Bobby Car', 5, 5)]

    choice = input(MENU).lower
    while choice != 'q':
        if choice == 'c'
            choose_taxi(taxis)
        if choice == 'd':
            drive_taxi()

def choose_taxi(taxis):
    """Make choice of a Taxi from list"""
    print(taxis)
def drive_taxi():
    """Drive the selected taxi"""


if __name__ == '__main__':
    main()

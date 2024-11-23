"""
CP1404 - prac_09 - Florian N Eisen
Test SilverServiceTaxi class
"""

from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    mumbai_taxi = SilverServiceTaxi('Tuk Tuk', 20, 2)
    print(mumbai_taxi)
    mumbai_taxi.drive(18)  # drive 18km
    print(f'{mumbai_taxi} = ${mumbai_taxi.get_fare():.2f}')
    # assert mumbai_taxi.get_fare() == 48.78 # assert an 18 km trip in a SilverServiceTaxi with fanciness of 2
    assert mumbai_taxi.get_fare() == 48.80  # assert the 18km trip is rounded

if __name__ == "__main__":
    main()

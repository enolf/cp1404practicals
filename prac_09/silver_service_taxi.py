"""
CP1404 - prac_09 - Florian N Eisen
Class for a silver taxi service: SilverServiceTaxi
"""

from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """SilverServiceTaxi is a subclass of Taxi"""

    flagfall = 4.5  # extra charge for silver service

    def __init__(self, name, fuel, fanciness=0.0):
        """name, price_per_km, fanciness"""
        super().__init__(name, fuel)
        self.price_per_km = Taxi.price_per_km * fanciness

    def __str__(self):
        """Return Taxi's __str__"""
        return f'{super().__str__()} plus flagfall of ${self.flagfall:.2f}'

    def get_fare(self):
        """Get fare incl. flagfall price"""
        return Taxi.get_fare(self) + self.flagfall

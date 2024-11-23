"""
CP1404 - prac_09 - Florian N Eisen
Class for a silver taxi service: SilverServiceTaxi
"""

from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """SilverSeriveTaxi is a subclass of Taxi"""

    def __init__(self, name, price_per_km, fanciness=0.0):
        super().__init__(name, price_per_km)
        self.price_per_km = Taxi.price_per_km * fanciness

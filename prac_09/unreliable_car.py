"""
CP1404 - prac_09 - Florian N Eisen
Class for an unreliable car object: UnreliableCar
"""

from prac_09.car import Car
from random import randint


class UnreliableCar(Car):
    """
    UnreliableCar is a subclass of Car
    Attributes:
        reliability: a float between 0 and 100, that represents the percentage chance that the drive method will actually drive the car
    """
    def __init__(self, name='', fuel=0, reliability=0.0):
        """
        name, fuel, reliability
        """

        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive UnrealiableCar aslong as the reliability is greater than to the randint (0,100) generated"""
        random_int = randint(0, 100)
        if random_int > self.reliability:
            distance = 0
        else:
            distance = super().drive(distance)
        return distance





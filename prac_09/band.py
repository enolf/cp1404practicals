"""
CP1404 - prac_09 - Florian N Eisen
Band Class for experimenting with associations
"""

from musician import Musician


class Band:

    def __init__(self, name):
        self.name = name
        self._musicians = []

    def __str__(self):
        return f'{self.name} ({[musician.__str__() for musician in self._musicians]})'

    def play(self):
        for musician in self._musicians:
            if musician.instruments:
                print(f'{musician.name} is playing: {musician.instruments}')
            else:
                print(f'{musician.name} needs an instrument!')
        return ''

    def add(self, musician):
        self._musicians.append(musician)

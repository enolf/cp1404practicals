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
        musicians = ''.join([str(musician) for musician in self._musicians])
        return f'{self.name} ({musicians})'

    def play(self):
        return '\n'.join([musician.play() for musician in self._musicians])

    def add(self, musician):
        self._musicians.append(musician)

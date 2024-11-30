"""
CP1404 - prac_09 - Florian N Eisen
Band Class for experimenting with associations
"""


class Band:
    """Band class for experimenting with associations between musicians (Musician objects)"""

    def __init__(self, name):
        """Band constructor (name)"""
        self.name = name
        self._musicians = []

    def __str__(self):
        """String of musicians"""
        musicians = ''.join([str(musician) for musician in self._musicians])
        return f'{self.name} ({musicians})'

    def play(self):
        """Print all musician's information in a list"""
        return '\n'.join([musician.play() for musician in self._musicians])

    def add(self, musician):
        """Add a musician to the band"""
        self._musicians.append(musician)

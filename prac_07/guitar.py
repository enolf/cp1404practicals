"""
CP1404 - prac_07 - Florian N Eisen
Guitars class to use as an object in myguitars.py
"""

CURRENT_YEAR = 2024


class Guitar:
    def __init__(self, name="", year=0, cost=0):
        """Initialise the class"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Define how string is printed"""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def __lt__(self, other):
        """Define how sorting is performed"""
        return self.year < other.year

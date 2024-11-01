"""
estimate: 20min
actual: 13 min
"""


class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) :{self.cost}"

    def get_age(self, year_now):
        if year_now > self.year:
            return year_now - self.year
        else:
            return f"{self.name} did not exist before {self.year}"

    def is_vintage(self, time):
        if time.get_age(self.year) >= 50:
            return True
        else:
            return False

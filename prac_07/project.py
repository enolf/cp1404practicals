"""
CP1404 - prac_07 - Florian N Eisen
estimated: 2 hours
actual
"""


class Project:
    def __init__(self, name, date, priority, cost, completion):
        """Take the following project data: name, start date, priority, cost estimate, completion percentage"""
        self.name = name
        self.date = date
        self.priority = priority
        self.cost = cost
        self.completion = completion

    def __str__(self):
        """Return a string representation of the project"""
        return (f"Name: {self.name}, Start Date: {self.date}, Priority: {self.priority},"
                f"Cost Estimate: {self.cost}, Completion Percentage: {self.completion}")


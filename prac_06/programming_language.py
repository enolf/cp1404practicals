"""
CP1404 - prac_06 - Florian N Eisen
estimated: 25
actual: 35
"""


class ProgrammingLanguage:
    def __init__(self, lang="", typing="", reflection=False, year=0):
        """Init"""
        self.lang = lang
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return f"{self.lang}, {self.typing} typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        return self.typing == "Dynamic"

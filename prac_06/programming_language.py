"""
estimate: 25min
"""

# data = [
#             ["(Field)", "Typing", "Reflection", "Year"],
#             ["Java", "Static", "Yes", 1995],
#             ["C++", "Static", "No", 1983],
#             ["Python", "Dynamic", "Yes", 19910],
#             ["Ruby", "Dynamic", "Yes", 1995]
#         ]
data = [
            ["(Field)", "Java", "C++", "Python", "Ruby"],
            ["Typing", "Static", "Static", "Dynamic", "Dynamic"],
            ["Reflection", "Yes", "No", "Yes", "Yes"],
            ["Year", 1995, 1983, 1991, 1995]
        ]


class ProgrammingLanguage:
    def __init__(self):
        """Init"""
        self.language = ""
        for element in data:
            print(f"{element:}")


    # def is_dynamic(self):
    #     if self.language

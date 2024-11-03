"""
CP1404 - prac_06 - Florian N Eisen
estimated: 25
actual: 35
"""

from prac_06.programming_language import ProgrammingLanguage


def main():
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)

    print("The dynamically typed languages are:")
    languages_list = [python, ruby, visual_basic]
    for lang in languages_list:
        if lang.is_dynamic():
            print(lang.lang)


main()

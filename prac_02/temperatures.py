"""
CP1404 - Practical - Florian N Eisen
Function for temperature conversion
"""


def main():
    """Converts temperatures between Celsius and Fahrenheit"""
    menu = """\nC - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ - Quit"""
    print(menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            convert = float(input("Celsius: "))
            fahrenheit = to_fahrenheit(convert)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            convert = float(input("Fahrenheit: "))
            celsius = to_celsius(convert)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(menu)
        choice = input(">>> ").upper()
    print("Thank you.")


def to_celsius(convert):
    """Convert Fahrenheit to Celsius"""
    celsius = (convert - 32) / 1.8
    return celsius


def to_fahrenheit(convert):
    """Convert Celsius to Fahrenheit"""
    fahrenheit = convert * 9.0 / 5 + 32
    return fahrenheit


main()

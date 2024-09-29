"""
CP1404 Sandbox | password_stars.py | Florian N Eisen
program to detect password
"""


def main():
    """Convert password into stars based on its length"""
    password = get_password()

    print_asterisks(password)


def print_asterisks(password):
    """Print password with stars"""
    print("password secured as:\n", "*" * len(password))


def get_password():
    """Take a password with a minimum length of 4 characters"""
    password = input("Enter your minimum 4 character long password: \n")
    while len(password) < 4:
        password = input("\nTry again, must be 4 characters: \n")
    return password


main()

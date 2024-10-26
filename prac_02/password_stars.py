"""
CP1404 - Practical - Florian N Eisen
Function for password to be converted into *s
"""


def main():
    """Convert min. 4 character password into *s based on its length"""
    password = get_password()
    print_asterisks(password)


def print_asterisks(password):
    """Print password with *s"""
    print("password secured as:\n", "*" * len(password))


def get_password():
    """Take a password with a minimum length of 4 characters"""
    password = input("Enter your minimum 4 character long password: \n")
    while len(password) < 4:
        password = input("\nTry again, must be 4 characters: \n")
    return password


main()

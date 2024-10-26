"""
CP1404 - Prac 05 - Florian N Eisen
Program to interpret  selected color names to their respective hexadecimal
"""

NAMES_TO_HEX_CODES = {"AliceBlue": "#f0f8ff", "British Racing Green": "#004225",
                      "Cherry Blossom Pink": "#ffb7c5", "Deep Saffron": "#ff9933",
                      "Vanilla": "#f3e5ab", "Teal": "#008080", "Pistachio": "#93c572",
                      "Opal": "#a8c3bc", "LimeGreen": "#32cd32", "Key Lime": "#e8f48c"}

# build lower case dict allow caseless calling of hex names
lower_case_names_to_hex_codes = {hex_name.lower(): NAMES_TO_HEX_CODES[hex_name] for hex_name in NAMES_TO_HEX_CODES}

colour_name = input("What color would you like to? ").lower()
while colour_name != "":  # allows blank input to exit loop
    try:
        print(f"The colour {colour_name} has a hex code of {lower_case_names_to_hex_codes[colour_name]}")
    except KeyError:
        print("This colour name is not known")
    colour_name = input("What color would you like to? ").lower()

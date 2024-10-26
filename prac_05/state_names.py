"""
CP1404/CP5632 Practical
State names in a dictionary, also added South Australia
"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania", "SA": "South Australia"}

for code_name, full_name in CODE_TO_NAME.items():
    print(f"{code_name:3} is {full_name}:")
state = input("Enter short state: ").upper()

while state != "":
    try:
        print(f"{state:3} is {CODE_TO_NAME[state]}")
    except KeyError:
        print("Invalid short state")
    state = input("Enter short state: ").upper()

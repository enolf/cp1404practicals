"""
CP1404/CP5632 Practical | Prac_04 | Florian N Eisen
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    print(data)
    print_stats(data)


def print_stats(data):
    """Use the stored data to print some stats about the teachers and their students"""
    for i in enumerate(data):
        print(f"{i[1][0]} is taught by {i[1][1]} and has {i[1][2]} students")


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data_storage = []
    input_file = open(FILENAME)
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        print("----------")
        data_storage.append(parts)
    input_file.close()
    return data_storage


main()

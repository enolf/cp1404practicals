"""
CP1404 - prac_05 - Florian N Eisen
Program will analyse past Wimbledon gentlemen's singles championships to display:
- the champions and how many times they have won.
- the countries of the champions in alphabetical order
Estimated: 35 mins
Actual: 92 mins
"""

FILENAME = "wimbledon.csv"


def main():
    """Read, extract and display the Wimbledon gentlemen's champions, total wins and respective countries.'"""

    champions_stats = {}
    champions_nations = set()
    data_extract = read_extract_dataset(FILENAME)
    process_data(data_extract, champions_stats, champions_nations)
    display_processes_data(champions_stats, champions_nations)


def read_extract_dataset(filename):
    """Read dataset from FILENAME and return extract data necessary for this program"""
    extracted_data = []
    with open(filename, "r", encoding="utf-8-sig") as dataset:
        dataset.readline()  # skip over the header line
        for raw_line in dataset:
            line = raw_line.split(",")
            extracted_data.append([line[1], line[2]])
        return extracted_data


def process_data(data_extract, champions_stats, champions_nations):
    """Mutate the extracted data into a dictionary of champions and their total wins and a set of champion's nations"""
    for entries in data_extract:
        champions_stats[entries[1]] = champions_stats.get(entries[1], 0) + 1
        champions_nations.add(entries[0])
    return champions_stats


def display_processes_data(champions_stats, champions_nations):
    """Display the Champions, their total wins and their respective countries"""
    print("Wimbledon Champions:")
    for champions, wins in champions_stats.items():
        print(f"{champions} {wins}")
    print(f"\nThese {len(champions_nations)} countries have won Wimbledon:\n{", ".join(sorted(champions_nations))}")


main()

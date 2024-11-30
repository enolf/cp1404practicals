"""
CP1404 - Prac_10 - Florian N Eisen
Program using an API to access Wikipedia
"""

import wikipedia

def main():

    entry = input("Enter a Wikipedia Search: ")
    while entry != '':
        wiki_result = wikipedia.summary(entry, sentences=1)
        print(wiki_result)
        entry = input("Enter a Wikipedia Search: ")

if __name__ == "__main__":
    main()

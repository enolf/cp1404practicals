"""
CP1404 - Prac_10 - Florian N Eisen
Program using an API to access Wikipedia
"""

import wikipedia

def main():

    entry = input("Enter a Wikipedia Search: ")
    while entry != '':
        try:
            wiki_result = wikipedia.page(entry, auto_suggest=False)
            print(wiki_result)

        except wikipedia.exceptions.DisambiguationError as e:
            print(e.options)
        except wikipedia.exceptions.PageError as e:
            print(e)
        entry = input("Enter a Wikipedia Search: ")


if __name__ == "__main__":
    main()

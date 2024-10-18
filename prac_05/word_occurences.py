"""
Estimated: 20 mins
Actual:
"""

string_user = input("Enter your string you want to analyse:\n").lower().split()

string_lookup = {}  # initialising dictionary used to store string components and properties
longest_word = ""  # variable to store longest word used for formatting width later on

for word in string_user:  # analyse each word in string
    if word in string_lookup:  # add to running count if word exists already
        string_lookup[word] = string_lookup[word] + 1
    else:
        string_lookup[word] = 1
    if len(word) > len(longest_word):  # look for longest word
        longest_word = word  # store longest word

for key, count in sorted(string_lookup.items()):  # print the results of analysis
    print(f"{key:{len(longest_word)}} : {count}")

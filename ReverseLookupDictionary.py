# Write a function named reverseLookup that finds all of the keys
# in a dictionary that map to a specific value. The function will
# take the dictionary and the value to search for as its only parameters.
# It should return a (possibly empty)
# list of keys from the dictionary that map to the provided value.


def reverseLookup(dict, value):

    keys = []

    for key in dict.keys():
        if dict[key] == value:
            keys.append(key)

    return keys

# sample main program to test the solution

def main():

    frenchEnglish = {"le" : "the", "la" : "the", "livre" : "book", "pomme" : "apple"}

    print("The French words for 'the' are:", reverseLookup(frenchEnglish,"the"))
    print("Expected results: ['le', 'la']")
    print()
    print("The French word for 'apple' is:", reverseLookup(frenchEnglish,"apple"))
    print("Expected results: ['pomme']")
    print()

main()


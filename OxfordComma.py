# When writing out a list in English, one normally spearates
# the items with commas. In addition, the word "and" is normally
# included before the last item, unless the list only contains
# one item. Consider the following four lists:

#   apples
#   apples and oranges
#   apples, oranges, and bananas
#   apples, oranges, bananas, and lemons

# Write a function that takes a list of strings as
# its only parameter. Your function should return a
# string that contains all of the items in the list
# formatted in the manner described above. Your function
# should work correctly for lists of any length. If the
# user does not enter any strings, it should print "<empty>".

# Include a main program that prompts the user for items, calls
# your function to create the properly formatted string,
# and displays the result.

def oxfordComma(lst):
    
    oCommas = ""
    
    if len(lst) == 0:
        return "<empty>"
    elif len(lst) == 1:
        return str(lst[0])
    elif len(lst) > 1:
        for i in range(0, len(lst) - 1):
            oCommas += str(lst[i]) + ", "

    oCommas += "and " + str(lst[-1]) + "." 

    return oCommas

def main():

    words = []

    entry = str(input("Enter a series of words (hit 'return' to discontinue): "))

    while entry != "":
        words.append(entry)
        entry = str(input("Enter a series of words (hit 'return' to discontinue): "))

    print(oxfordComma(words))
        

main()

# Write a program that reads words from the user, one at a time,
# until the user enters a blank line. After the user enters the blank line,
# your program should display each word entered by the user, one per line,
# but only once. The words should be displayed in the same order that they
# were entered. For example, if the user enters:

#	first
#	second
#	first
#	third
#	second
	
# then your program should display:

#	first
#	second


def main():

    words = []

    word = str(input("Please type in a word: "))

    while word != "":
        if word not in words:
            words.append(word)
        for word in words:
            print(word)
        word = str(input("Please type in a word (enter w/o a word ends the cycle): "))

main()

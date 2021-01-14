# In a particular lottery, a player purchases a ticket with six numbers
# of his or her choice. The numbers must be between 1 and 49. Duplicate
# numbers are not permitted.

# Write a program that generates a random
# selection of 6 numbers for a lottery ticket. Ensure that the 6 numbers
# selected do not contain any duplicates, and display the numbers in
# ascending order.

import random

def main():

    choiceNumbers = list(input("Enter 6 integers between 1 and 49 (with no spaces between): "))

    ticketNumbers = []

    for i in range(6):
        num = random.randint(1,49)
        while num in ticketNumbers:
            num = random.randint(1,49)

        ticketNumbers.append(num)

    ticketNumbers.sort()
    
    print("Here are the lottery numbers: ")
    print(ticketNumbers)
    print("Here are the numbers you selected: ")
    print(choiceNumbers)

    if ticketNumbers == choiceNumbers:
        print("You win!")
    else:
        print("You lose.")

main()

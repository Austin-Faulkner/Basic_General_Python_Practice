# Write a program that reads integers from
# the user until a blank line is entered.

# Once all of the integers have been entered,
# your program should display all of the negative numbers,
# followed by all of the zeroes, followed by all
# of the positive numbers.

# Within each group, the numbers should appear in the same order that
# they were entered by the user. For example, if the user
# enters the values 3, -4, 1, 0, -1, 0, and -2, the program
# should output the values -4, -1, -2, 0, 0, 3, and 1 in that order.

# However, your program should display each value on a separate line.


def main():

    negatives = []
    zeroes = []
    positives = []

    line = input("Enter an integer (one per line; enter to stop): ")

    while line != "":

        num = int(line)

        if num < 0:
            negatives.append(num)
        elif num > 0:
            positives.append(num)
        else:
            zeroes.append(num)

        line = input("Enter an integer (one per line; enter to stop): ")

    for n in negatives:
        print(n)
    for z in zeroes:
        print(z)
    for p in positives:
        print(p)

main()


# The Twelve Days of Christmas is a repetitive song that describes an increasingly
# long list of gifts sent to one's true love on each of 12 days. A single gift is
# sent on the first day. A new gift is added on each additional day until the complete collection is sent.

# The first three verses of the song are shown below:

#     On the first day of Christmas
#     My true love gave to me
#     A partridge in a pear tree.
#     On the second day of Christmas
#     My true love gave to me
#     Two turtle doves,
#     And a partridge in a pear tree.

#     On the third day of Christmas
#     My true love gave to me
#     Three French hens,
#     Two turtle doves,
#     And a partridge in a pear tree.	

# Subsequent gifts include:

#     Four calling birds,
#     Five golden rings,
#     Six geese a-laying,
#     Seven swans a-swimming,
#     Eight maids a-milking,
#     Nine ladies dancing,
#     Ten lords a-leaping,
#     Eleven pipers piping,
#     Twelve drummers drumming,
     
# Write a program that displays the complete lyrics for the song. Write a function that takes
# the verse number as its only parameter, and displays the specified verse of the song. Then call
# that function 12 times with integers that increase from 1 to 12.

# Each line should appear only once in your program, with the exception of the line with the
# partridge. It may have two versions, because on the first day, the line reads
# "A partridge in a pear tree", and on all other days, the line reads, "And a partridge in a pear tree."

# Hint: use the code you wrote in problem 4.2 for cardinalToOrdinal() to help you print the
# first line of each verse.


def twelveDaysOfChristmas(n):

    if n == 1:
        return("                  " + "On the first day of Chrismas" + "\n" + "                  " + "My true love gave to me" + "\n" + "                  " + "A partidge in a pear tree." + "\n")
    elif n == 2:
        return("                  " + "On the second day of Chrismas" + "\n" + "                  " + "My true love gave to me" + "\n" + "                  " \
                                    + "Two turtle doves," + "\n" "                  " + "A partidge in a pear tree." + "\n")
    elif n == 3:
        return("                  " + "On the third day of Chrismas" + "\n" + "                  " + "My true love gave to me" + "\n" + "                  " \
                                    + "Three French hens," + "\n" + "                  " + "Two turtle doves," + "\n" + "                  " + "And a partidge in a pear tree." + "\n")
    elif n == 4:
        return("                  " + "On the fifth day of Chrismas" + "\n" + "                  " + "My true love gave to me" + "\n" + "                  " \
                                    + "Four calling birds," + "\n" + "                  " + "Three French hens," + "\n" + "                  " + "Two turtle doves," + "\n" + "                  " \
                                    + "And a partidge in a pear tree." + "\n")
    elif n == 5:
        return("                  " + "On the fourth day of Chrismas" + "\n" + "                  " + "My true love gave to me" + "\n" + "                  " \
                                    + "Five golden rings," + "\n" + "                  " + "Four calling birds," + "\n" + "                  " + "Three French hens," + "\n" + "                  " + "Two turtle doves," + "\n" + "                  " \
                                    + "And a partidge in a pear tree." + "\n")
    elif n == 6:
        return("                  " + "On the sixth day of Chrismas" + "\n" + "                  " + "My true love gave to me" + "\n" + "                  " \
                                    + "Six geese a-laying," + "\n" + "                  " + "Five golden rings," + "\n" + "                  " + "Four calling birds," + "\n" + "                  " \
                                    + "Three French hens," + "\n" + "                  " + "Two turtle doves," + "\n" + "                  " \
                                    + "And a partidge in a pear tree." + "                  " + "\n")
    elif n == 7:
        return("                  " + "On the seventh day of Chrismas" + "\n" + "                  " + "My true love gave to me" + "\n" + "                  " \
                                    + "Seven swans a s-swimming," + "\n" + "                  "  \
                                    + "Six geese a-laying," + "\n" + "                  " + "Five golden rings," + "\n" + "                  " + "Four calling birds," + "\n" + "                  " \
                                    + "Three French hens," + "\n" + "                  " + "Two turtle doves," + "\n" + "                  " \
                                    + "And a partidge in a pear tree." + "\n")
    elif n == 8:
        return("                  " + "On the eigth day of Chrismas" + "\n" + "                  " + "My true love gave to me" + "\n" + "                  " + "Eigth maids a-milking," + "\n" + \
                                    "                  " + "Seven swans a s-swimming," + "\n" + "                  "  \
                                    + "Six geese a-laying," + "\n" + "                  " + "Five golden rings," + "\n" + "                  " + "Four calling birds," + "\n" + "                  " \
                                    + "Three French hens," + "\n" + "                  " + "Two turtle doves," + "\n" + "                  " \
                                    + "And a partidge in a pear tree." + "\n")
    elif n == 9:
        return("                  " + "On the nineth day of Chrismas" + "\n" + "                  " + "My true love gave to me" + "\n" + "                  " + "Nine ladies dancing," \
                                    + "\n" + "                  " + "Eigth maids a-milking," + "\n" + \
                                    "                  " + "Seven swans a s-swimming," + "\n" + "                  "  \
                                    + "Six geese a-laying," + "\n" + "                  " + "Five golden rings," + "\n" + "                  " + "Four calling birds," + "\n" + "                  " \
                                    + "Three French hens," + "\n" + "                  " + "Two turtle doves," + "\n" + "                  " \
                                    + "And a partidge in a pear tree." + "\n")
    elif n == 10:
        return("                  " + "On the tenth day of Chrismas" + "\n" + "                  " + "My true love gave to me" + "\n" + "                  " + "Ten lords a-leaping," \
                                    + "\n" + "                  " +"Nine ladies dancing," \
                                    + "\n" + "                  " + "Eigth maids a-milking," + "\n" + \
                                    "                  " + "Seven swans a s-swimming," + "\n" + "                  "  \
                                    + "Six geese a-laying," + "\n" + "                  " + "Five golden rings," + "\n" + "                  " + "Four calling birds," + "\n" + "                  " \
                                    + "Three French hens," + "\n" + "                  " + "Two turtle doves," + "\n" + "                  " \
                                    + "And a partidge in a pear tree." + "\n")
    elif n == 11:
        return("                  " + "On the eleventh day of Chrismas" + "\n" + "                  " + "My true love gave to me" + "\n" + "                  " + "Eleven pipers piping," + "\n" \
                                    + "                  " + "Ten lords a-leaping," 
                                    + "\n" + "                  " +"Nine ladies dancing," \
                                    + "\n" + "                  " + "Eigth maids a-milking," + "\n" + \
                                    "                  " + "Seven swans a s-swimming," + "\n" + "                  "  \
                                    + "Six geese a-laying," + "\n" + "                  " + "Five golden rings," + "\n" + "                  " + "Four calling birds," + "\n" + "                  " \
                                    + "Three French hens," + "\n" + "                  " + "Two turtle doves," + "\n" + "                  " \
                                    + "And a partidge in a pear tree." + "\n")
    elif n == 12:
        return("                  " + "On the twelfth day of Chrismas" + "\n" + "                  " + "My true love gave to me" + "\n" + "                  " + "Twelve drummers druming," \
                                    + "\n" + "                  " + "Eleven pipers piping," + "\n" \
                                    + "                  " + "Ten lords a-leaping," 
                                    + "\n" + "                  " +"Nine ladies dancing," \
                                    + "\n" + "                  " + "Eigth maids a-milking," + "\n" + \
                                    "                  " + "Seven swans a s-swimming," + "\n" + "                  "  \
                                    + "Six geese a-laying," + "\n" + "                  " + "Five golden rings," + "\n" + "                  " + "Four calling birds," + "\n" + "                  " \
                                    + "Three French hens," + "\n" + "                  " + "Two turtle doves," + "\n" + "                  " \
                                    + "And a partidge in a pear tree." + "\n")
    
def main():

    for i in range(1,13):
        print(twelveDaysOfChristmas(i))
        
main()

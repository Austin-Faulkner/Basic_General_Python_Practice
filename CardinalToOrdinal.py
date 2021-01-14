# TASK: 12/27/2019

# Words like first, second, and third are referred to as ordinal numbers.
# They correspond to the cardinal numbers 1, 2, and 3.

# Write a function called "cardinalToOrdinal()" that takes an integer from 1 to 15 and
# returns a string containing the corresponding English ordinal number as
# its only result. It should return the string, "Integer out of range" if a
# value outside of this range is provided as a parameter.

# Include a main program that demonstrates your function by displaying each integer
# from 1 to 15 and its corresponding ordinal number (or the out of range message).

import random

def cardinalToOrdinal(num):

    if num < 1 or num > 15:
           print(format("Integer out of range: " + str(num), ">52s"))

    first = ''
    second = ''
    third = ''
    fourth = ''
    fifth = ''
    sixth = ''
    seventh = ''
    eigth = ''
    nineth = ''
    tenth = ''
    eleventh = ''
    twelfth = ''
    thirteenth = ''
    fourteenth = ''
    fifteenth = ''
    
    if num == 1:
        first = "first"
    elif num == 2:
        second = "second"
    elif num == 3:
        third = "third"
    elif num == 4:
        fourth = "fourth"
    elif num == 5:
        fifth = "fifth"
    elif num == 6:
        sixth = "sixth"
    elif num == 7:
        seventh = "seventh"
    elif num == 8:
        eigth = "eigth"
    elif num == 9:
        nineth = "nineth"
    elif num == 10:
        tenth = "tenth"
    elif num == 11:
        eleventh = "eleventh"
    elif num == 12:
        twelfth = "twelfth"
    elif num == 13:
        thirteenth = "thirteenth"
    elif num == 14:
        fourteenth = "fourteenth"
    elif num == 15:
        fifteenth = "fifteenth"

    return first, second, third, fourth, fifth, sixth, seventh, eigth, nineth, tenth, eleventh, twelfth, thirteenth, fourteenth, fifteenth

def main():

    print("TABLE OF INTEGERS AND ORDINAL NUMBERS".center(80))
    print("-------------------------------------".center(80))

    for i in range(1,16):
       num1, num2, num3, num4, num5, num6, num7, num8, num9, num10, num11, num12, num13, num14, num15 = cardinalToOrdinal(i)
       print(format(i, "30d") + "              " + num1 + num2 + num3 + num4 + num5 \
             + num6 + num7 + num8 + num9 + num10 + num11 + num12 + num13 + num14 + num15)

main()



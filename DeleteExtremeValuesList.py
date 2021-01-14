# Austin Faulkner: faulkner.austin@gmail.com
# January 10, 2020

# When analyzing large amounts of data, it it often desirable to remove the most
# extreme values (some of the largest and some of the smallest) before performing
# other calculations. Write a function that takes a list of numeric values and a
# non-negative integer n as its parameters.

# The function should create a new copy
# of the list with the n largest and n smallest elements removed, and then return
# the new copy of the list. The order of the elements in the returned list does not
# have to match the order of the elements in the original list. (This means you can
# sort the original list to help you find the extreme values.)


def removeExtremes(lst, n):

    lst.sort()

    for i in range(n):
        lst.pop()
        lst.pop(0)

    print(lst)
    
    return lst


def main():

    data = [-3.2, 4.2, 10.9, -12.78, 190.0, 588.00, -1123, 1, 0]

    REMOVE = int(input("Enter the the number of max and min extreme values you would like to remove from the data set (no more than " + str(len(data)) + "): ")) 

    removeExtremes(data, REMOVE)

main()

# Time Intervals:

# Create a class called Time to represent a time interval.
# Every instance of Time will have two properties: hours and
# minutes, both integers passed in at the time of creation.

# Then to model a time interval of 5 hours and 4 minutes, you might say:

#   interval = Time(5,4)
   
# Create the following methods for class Time:

# displayTime, which returns a string suitable for printing.
# For the above example, interval.displayTime() would return         ****DONE****
# the string "5 hours and 4 minutes".

# addTime, which adds two Time objects together. For example,
# if t1 is a time interval of 2 hours and 18 minutes and t2 is a time interval
# of 4 hours and 51 minutes, then t1.addTime(t2) would change t1 to
# 7 hours and 9 minutes.

# equivalentMinutes, which returns an integer representing the number of
# minutes contained in a time interval. For example, for the time interval
# above corresponding to 5 hours and 4 minutes, interval.equivalentMinutes()
# would return 304.

class Time:

    def __init__(self, hrs, mins):
        self.__hours = hrs
        self.__minutes = mins

    def displayTime(self):
        return str(self.__hours) + " hours and " + str(self.__minutes) + " minutes."

    def addTime(self, otherTime):
        self.__hours += otherTime.__hours
        self.__minutes += otherTime.__minutes
        if self.__minutes >= 60:
            self.__hours += 1
            self.__minutes -= 60

    def equivalentMinutes(self):
        return 60 * self.__hours + self.__minutes
    

def main():

    t1 = Time(5,4)
    t2 = Time(2, 56)

    print(t1.equivalentMinutes())

    t1.addTime(t2)

    print(t1.displayTime())
    print(t2.displayTime())

main()

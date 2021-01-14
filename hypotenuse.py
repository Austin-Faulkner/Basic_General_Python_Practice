# This program uses a function to compute and output to std output
# the hypotenuse of a right triangle

def hypotenuse(a, b):

    c = (a**2 + b**2)**(1/2)

    return c

def main():

    legA = int(input("Enter leg A of the right triangle: "))
    legB = int(input("Enter leg B of the right triangle: "))
    
    hypotenuseC = hypotenuse(legA,legB)

    print("The hypotenuse of the right triangle is", hypotenuseC)

main()

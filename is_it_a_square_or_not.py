# Take values of length and breadth of a rectangle from user and check if it is square or not.

def square_not(length,breadth):
    if length == breadth:
        print("It is a square")
    else:
        print("It is not a square")

length,breadth = 5, 5
square_not(length,breadth)

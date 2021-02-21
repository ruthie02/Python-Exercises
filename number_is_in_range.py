# Write a Python function to check whether a number is in a given range

def number_range(number):
    if number in range(0,15):
        print("The number " + str(number) + " is in range(0,15)")
    else:
        print("The number " + str(number) + " is not in range(0,15)")


number = 16
number_range(number)

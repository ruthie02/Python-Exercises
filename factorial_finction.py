# Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.

def factorial_number(number):
    if number <= 0:
        print("You cannot compute for a factorial of a negative number!")
    else:
        total = 1
        for i in range(1, number+1):
            total = total *i
        return total
number = -5
print(factorial_number(number))

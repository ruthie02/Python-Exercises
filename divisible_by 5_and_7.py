# Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).

def number_div(number1,number2):
    for i in range(number1,number2+1):
        if i%5== 0 and i%7==0:
            print(i)

number_div(1500,2700)

# compute for sum of the squares

def sum_square(number):
    sum = 0
    for num in range(number):
        sum += num**2
    return sum

print(sum_square(10))

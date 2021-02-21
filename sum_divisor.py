# Question 4
# Fill in the empty function so that it returns the sum of all the divisors of a number, without including it. A divisor is a number that divides into another without a remainder.

def sum_divisors(n):
    sum = 0
    start = 1
    while start < n:
        if n % start == 0:
            sum += start
            start += 1
        else:
            start += 1

    return sum

print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# 55



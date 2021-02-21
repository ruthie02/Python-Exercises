# Write a Python program to calculate the length of a string

def length(word):
    length_w = 0
    for letter in word:
        length_w += 1
    return(length_w)


print(length("i am beautiful"))

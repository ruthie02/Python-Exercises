# Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
# If the string length is less than 2, return instead of the empty string.

def strings(chars):
    if len(chars) < 2:
        return("")
    else:
        return(chars[:2]+chars[-2:])

print(strings("w3resource"))

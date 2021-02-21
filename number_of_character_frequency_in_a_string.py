# Write a Python program to count the number of characters (character frequency) in a string.

def dicti(lettercount):
    dict = {}
    for n in lettercount:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1

    return(dict)

print(dicti('google.com'))
        

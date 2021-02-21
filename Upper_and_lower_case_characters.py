# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

def count_str(string):
    lowstring = 0
    upperstring = 0
    for i in string:
        if i.islower():
            lowstring += 1
        else:
            upperstring += 1
   
    print("No. if Upper case characters: " + str(upperstring))
    print("No. if lower case characters: " + str(lowstring))


string = "AmIfnoangao"
print(count_str(string))
                
            

# Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.



def change(words):
    first = words[0]
    words_1 = words.replace(first, "$")
    new_word = first + words_1[1:]

    return(new_word)


print(change("restart"))



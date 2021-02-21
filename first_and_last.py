def first_and_last(message):
    first = message[0]
    second = message[-1]
    if len(message) == 0:
        return True
    elif first ==  second:
        return True
    else:
        return False

print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))

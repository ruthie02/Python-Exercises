# A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
# Ask user for quantity
# Suppose, one unit will cost 100.
# Judge and print total cost for user.

def discount_not(quantity):
    if quantity > 1000:
        return quantity - quantity * 0.10
    else:
        return quantity * 1.1


quantity = int(input("What is the cost of the purchased quantity?"))
print(discount_not(quantity))



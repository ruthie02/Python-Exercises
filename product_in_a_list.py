# Write a Python function to multiply all the numbers in a list. Go to the editor
# Sample List : (8, 2, 3, -1, 7)
# Expected Output : -336
def sum_list(list):
    total = 1
    for numbers in list:
        total *= numbers
    return total
list = (8,2,3,-1,7)
print(sum_list(list))

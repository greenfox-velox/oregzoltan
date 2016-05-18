numbers = [7, 5, 8, -1, 2]
# Write a function that returns the minimal element
# in a list (your own min function)
def return_min(arg):
    min = arg[0]
    for each in arg:
        if min > each:
           min = each
    return min

print(return_min(numbers))

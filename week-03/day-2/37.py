numbers = [3, 4, 5, 6, 7]
# write a function that filters the odd numbers
# from a list and returns a new list consisting
# only the evens
def filteroddout(arg):
    filtered = []
    for each in arg:
        if each % 2 == 0:
            filtered.append(each)
    return filtered

print (filteroddout(numbers))

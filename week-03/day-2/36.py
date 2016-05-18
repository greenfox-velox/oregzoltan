numbers = [3, 4, 5, 6, 7]
# write a function that reverses a list

def rev_list(inp):
    rev_numbers = []
    i = len(inp)
    while i != 0:
        i -= 1
        rev_numbers.append(inp[i])
    return rev_numbers

print (rev_list(numbers))

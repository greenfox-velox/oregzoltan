names = ['Zakarias', 'Hans', 'Otto', 'Ole']
# create a function that returns the shortest string
# from a list
def returnshortest(arg):
    shortest = arg[0]
    for each in arg:
        if len(each) < len(shortest):
            shortest = each
    return shortest

print(returnshortest(names))

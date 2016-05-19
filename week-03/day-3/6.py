# create a function that takes a list and returns a new list that is reversed
def rev_list(a):
    a2 = []
    for i in range(len(a)-1,-1,-1):
        a2.append(a[i])
    return a2

a = [1, 2, 3, 4]
print(rev_list(a))
print(a)

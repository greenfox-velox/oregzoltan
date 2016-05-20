# create a function that takes a list and returns a new list with all the elements doubled
def double_elements (list):
    l2=[]
    for item in list:
        l2.append(item*2)
    return l2

l = [5,8,2,16,'hi']
print(double_elements(l))
print(l)

def digitize(n):
    num_str = str(n)
    num_list = []
    for i in range(len(num_str)-1,-1,-1):
        num_list.append(int(num_str[i]))
    return num_list

print(digitize(35231))
# [1,3,2,5,3]

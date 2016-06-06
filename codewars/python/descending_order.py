def Descending_Order(num):
    num_str = str(num)
    num_list = []
    for i in num_str:
        num_list.append(i)
    num_list.sort()
    num_str = ''
    for i in range(len(num_list)-1,-1,-1):
        num_str += num_list[i]
    return int(num_str)

print(Descending_Order(126345789))
# 987654321

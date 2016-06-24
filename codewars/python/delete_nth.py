def delete_nth(order,max_e):
    new_list = []
    for number in order:
        counter = 0
        for each in new_list:
            if each == number:
                counter += 1
        if counter < max_e:
            new_list.append(number)
    return new_list


print(delete_nth([20,37,20,21], 1))
# [20,37,21])
print(delete_nth([1,1,3,3,7,2,2,2,2], 3))
# [1, 1, 3, 3, 7, 2, 2, 2])

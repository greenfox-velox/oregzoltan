def remove_smallest(numbers):
    if numbers == []:
        return []
    smallest = numbers[-1]
    index = len(numbers)-1
    for i in range(len(numbers)-1,-1,-1):
        if numbers[i] <= smallest:
            smallest = numbers[i]
            index = i
    del numbers[index]
    return numbers

print(remove_smallest([5, 1, 3, 2, 1, 4]))
 # [5, 3, 2, 1, 4]

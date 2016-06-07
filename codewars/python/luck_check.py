def luck_check(string):
    left_sum = 0
    right_sum = 0
    if len(string) % 2 == 0:
        for i in range(int(len(string)/2)):
            left_sum += int(string[i])
        string_rev = string[-1::-1]
        for i in range(int(len(string)/2)):
            right_sum += int(string_rev[i])
    else:
        for i in range(len(string)//2):
            left_sum += int(string[i])
        string_rev = string[-1::-1]
        for i in range(len(string)//2):
            right_sum += int(string_rev[i])
    if left_sum == right_sum:
        return True
    else:
        return False

print(luck_check('17935'))
    #     8 + 1 + 3 = 3 + 7 + 2
# 17935     #         1 + 7 = 3 + 5))

def divisors(integer):
    div_nums = []
    for i in range(2, integer):
        if integer % i == 0:
            div_nums.append(i)
    if len(div_nums) == 0:
        return '%d is a prime' % (integer)
    else:
        return div_nums

print(divisors(12))
# [2, 3, 4, 6]))

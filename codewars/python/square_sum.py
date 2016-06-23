def square_sum(numbers):
    total = 0
    for number in numbers:
        total += number*number
    return total

print(square_sum([0, 3, 4, 5]))
# 50

def sumDigits(number):
    if number < 0:
        number *= -1
    number_str = str(number)
    total = 0
    for i in number_str:
        total += int(i)
    return total

print(sumDigits(-32))

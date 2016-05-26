# 3. Given a non-negative int n,
# return the sum of its digits recursively (no loops).
# Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6),
# while divide (/) by 10 removes the rightmost digit (126 // 10 is 12).

def sumdigits(number):
    digit = number % 10
    number = number // 10
    if number < 10:
        return digit+number
    else:
        return digit + sumdigits(number)
print(sumdigits(133))

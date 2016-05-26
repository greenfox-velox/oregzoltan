# 2. write a recursive function
# that takes one parameter: n
# and adds numbers from 1 to n

def total(number):
    if number <= 0:
        return number
    else:
        return number + total(number - 1)

print(total(6))

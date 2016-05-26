# 1. write a recursive function
# that takes one parameter: n
# and counts down from n

def count_down(number):
    if number <= 0:
        return number
    else:
        print(number)
        return count_down(number - 1)

print(count_down(5))

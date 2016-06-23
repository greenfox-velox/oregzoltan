from math import sqrt
def is_square(n):
    if type(n) == int and n > 0:
        if (sqrt(n)*int(sqrt(n))) == n:
            return True
    return False

print(is_square(81))

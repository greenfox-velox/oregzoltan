
# Adds a and b, returns as result
def add(a, b):
    return a+b

# Returns the highest value from the three given params
def max_of_three(a, b, c):
    if a > b and a > c:
        return a
    else:
        if b > c:
            return b
        else:
            return c

# Returns the median value of a list given as param
def median(pool):
    half = len(pool) // 2
    pool.sort()
    if not len(pool) % 2:
        return (pool[half - 1] + pool[half]) / 2.0
    return pool[half]

# Returns true if the param is a vovel
def is_vovel(char):
    if char.lower() in 'aeiou':
        return True

# Create a method that translates hungarian into the teve language
def translate(hungarian):
    teve = ''
    for char in hungarian:
        if is_vovel(char):
            teve += char + 'v' + char
        else:
            teve += char
    return teve

# create a function that returns it's input factorial
def factorial(input):
    total = 1
    for i in range(input):
        total *= i+1
    return total

print (factorial(6))

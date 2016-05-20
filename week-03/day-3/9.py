# Create a function that prints a triangle like this:
#   *
#   **
#   ***
#   ****
#   *****
#   ******
# It should take a number as parameter that describes how many lines the triangle has

def printtriangle(lines):
    for i in range(lines):
        print('*'*(i+1))

printtriangle(6)

# Create a function that prints a triangle like this:
#       *
#      ***
#     *****
#    *******
#   *********
#  ***********
#
# It should take a number as parameter that describes how many lines the triangle has

def printtriangle(lines):
    for i in range(1, lines+1):
        print(' '*(lines-i) + '*'*(i*2-1))

printtriangle(5)

# Create a function that prints a diamond like this:
#       *
#      ***
#     *****
#    *******
#   *********
#  ***********
#   *********
#    *******
#     *****
#      ***
#       *
#
# It should take a number as parameter that describes how many lines the diamond has

def printtriangle(lines):
    for i in range(1, (lines//2)+2):
        print(' '*((lines//2)-i+1) + '*'*(i*2-1))
    for i in range((lines//2), 0, -1):
        print(' '*((lines//2)-i+1) + '*'*(i*2-1))

printtriangle(9)

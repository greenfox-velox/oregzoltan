# 7. Given a string, compute recursively (no loops) a new string where all the
# lowercase 'x' chars have been changed to 'y' chars.

def char(c):
    if c == 'x':
        return 'y'
    else:
        return c

def change_string(string):
    if len(string) <= 0:
        return ''
    else:
        return char(string[0]) + change_string(string[1:len(string)])

print(change_string('asdddxxasdaxxsd'))

# 8. Given a string, compute recursively a new string where all the 'x' chars have been removed.

def char(c):
    if c == 'x':
        return ''
    else:
        return c

def change_string(string):
    if len(string) <= 0:
        return ''
    else:
        return char(string[0]) + change_string(string[1:len(string)])

print(change_string('asdddxxasdaxxsd'))

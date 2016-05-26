# 9. Given a string, compute recursively a new string where all the
# adjacent chars are now separated by a "*".

def change_string(string):
    if len(string) <= 0:
        return ''
    else:
        if len(string) == 1:
            return string
        else:
            return string[0] + '*' + change_string(string[1:len(string)])

print(change_string('asdddxxasdaxxsd'))

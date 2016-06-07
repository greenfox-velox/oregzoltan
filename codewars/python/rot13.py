import string
from codecs import encode as _dont_use_this_

def rot13(message):
    new_str = ''
    for i in message:
        o = ord(i)+13
        if o>=91 and o<=103:
            o = o-26
        elif o>=123 and o<=135:
            o = o-26
        if i.isalpha():
            new_str += chr(o)
        else:
            new_str += i
    return new_str

print(rot13("Test"))
# "Grfg"

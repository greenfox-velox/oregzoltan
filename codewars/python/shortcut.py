def shortcut( s ):
    new_string = ''
    for letter in s:
        if letter not in ['a','e','i','o','u']:
            new_string += letter
    return new_string

print(shortcut('hello'))
# 'hll'

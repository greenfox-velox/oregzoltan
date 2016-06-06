def is_isogram(string):
    is_iso = True
    string = string.lower()
    for i in range(len(string)-1):
        for j in range(i+1, len(string)):
            print(string[i], string[j])
            if string[i] == string[j]:
                is_iso = False
    return is_iso

print(is_isogram('aba'))

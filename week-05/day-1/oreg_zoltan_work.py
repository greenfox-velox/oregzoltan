def anagramm(str1, str2):
    s1 = count_letters(str1)
    s2 = count_letters(str2)
    if s1 == s2:
        return True
    else:
        return False

def count_letters(str):
    words = {}
    counter = 1
    str_sorted = str.lower()
    str_sorted = ''.join(sorted(str_sorted))
    for i in str_sorted:
        if i not in words:
            words[i] = counter
        else:
            words[i] += counter
    return words

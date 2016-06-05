def reverse_words(str):
    rev_list = []
    words_list = str.split(' ')
    for i in range(len(words_list)):
        str = words_list[i]
        rev_list.append(str[-1::-1])
        print(rev_list)
    str = ' '.join(rev_list)
    return str
print(reverse_words('The greatest victory is that which requires no battle'))

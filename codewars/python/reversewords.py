def reverseWords(str):
    words_list = str.split(' ')
    reversed_list = []
    for i in range(len(words_list)-1,-1,-1):
        reversed_list.append(words_list[i])
    str = ' '.join(reversed_list)
    return str

print(reverseWords('The greatest victory is that which requires no battle'))

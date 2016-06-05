def title_case(title, minor_words = ''):
    if title == '':
        return ''
    title = title.lower()
    minor_words = minor_words.lower()
    title_list = title.split(' ')
    minor_list = minor_words.split(' ')
    correct_list = []
    word = title_list[0]
    if len(word) > 1:
        word = word[0].upper() + word[1:]
    else:
        word = word[0].upper()
    correct_list.append(word)
    for i in range(1,len(title_list)):
        word = title_list[i]
        if title_list[i] in minor_list:
            word = title_list[i]
        elif len(word) > 1:
            word = word[0].upper() + word[1:]
        elif len(word) == 1:
            word = word[0].upper()
        correct_list.append(word)
    title = ' '.join(correct_list)
    return title

print(title_case('First a of in', 'an often into'))
# 'First A Of In' but got 'First a Of In'.

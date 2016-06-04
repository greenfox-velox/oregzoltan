def pig_it(text):
    #your code here
    words_list = text.split()
    for i in range(len(words_list)):
        if words_list[i][-1].isalpha():
            words_list[i] = words_list[i][1:] + words_list[i][0] + 'ay'
        elif len(words_list[i]) > 1:
            words_list[i] = words_list[i][1:-1] + words_list[i][0] + 'ay' + ' ' + words_list[i][-1]
    text = ' '.join(words_list)
    return text

print(pig_it('Pig latin is cool !'))

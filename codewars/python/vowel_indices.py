def vowel_indices(word):
    word = word.lower()
    vowels = 'aeiouy'
    vowel_indexlist = []
    for i in range(len(word)):
        if vowels.find(word[i]) != -1:
            vowel_indexlist.append(i+1)
    return vowel_indexlist

print(vowel_indices('YoMama'))
 # -> [1,2,4,6]

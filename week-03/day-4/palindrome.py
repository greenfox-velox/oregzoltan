def create_palindrome(word):
    new_word = word
    for i in range(len(word)-1, -1, -1):
        new_word += word[i]
    return new_word

word = 'pear'
print(create_palindrome(word))

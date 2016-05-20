def search_palindrome(inp):
    palindromes = []
    for i in range(len(inp)):
        for j in range(i+2, len(inp)):
            if inp[i:j+1] == inp[j:i-1:-1]:
                palindromes.append(inp[i:j+1])
    return(palindromes)
words = 'dog goat dad duck doodle never neasen'
print(search_palindrome(words))

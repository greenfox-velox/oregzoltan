def capitals(word):
    indexes = []
    counter = 0
    for letter in word:
        if ord(letter) >= 65 and ord(letter) <= 90:
            indexes.append(counter)
        counter += 1
    return indexes
    
print(capitals('CodEWaRs'))
 # [0,3,4,6] ))

def encryptor(key, message):
    #Program me!
    coded_msg = ''
    letter = ''
    for i in message:
        if i.isalpha():
            letter = ord(i)
            if key > 26 or key < -26:
                key = key % 26
            if letter >= 65 and letter <= 90:
                letter = ord(i) + key
                if letter < 65:
                    letter = letter + 26
                elif letter > 90:
                    letter = letter - 26
            if letter >= 97 and letter <= 122:
                letter = ord(i) + key
                if letter < 97:
                    letter = letter + 26
                elif letter > 122:
                    letter = letter - 26
            coded_msg = coded_msg + chr(letter)
        else:
            coded_msg = coded_msg + i
    return coded_msg

print(encryptor(27, 'Whoopi Goldberg'))

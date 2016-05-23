# Create a method that decrypts the texts/duplicated_chars.txt

def decrypt(file_name):
    f = open(file_name)
    text = f.read()
    text2 = ''
    counter = 0
    while counter != len(text):
        if text[counter] == '\n':
            text2 += text[counter]
        elif counter % 2 == 0:
            text2 += text[counter]
        counter += 1
    f.close()
    return text2

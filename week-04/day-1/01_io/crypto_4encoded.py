# Create a method that decrypts texts/encoded_zen_lines.txt
def decrypt(file_name):
    f = open(file_name)
    text = f.read()
    text2 = ''
    for i in text:
        if i != '\n' and i != ' ':
            text2 += chr(ord(i)-1)
        else:
            text2 += i
    return text2
#print(decrypt('texts/encoded_zen_lines.txt'))

# Create a method that decrypts texts/reversed_zen_lines.txt
def decrypt(file_name):
    f = open(file_name)
    text = f.readlines()
    str = ''
    rev = ''
    for line in text:
        str = line[0:len(line)-1]
        str = str[::-1]
        rev += str + '\n'
    f.close()
    return rev

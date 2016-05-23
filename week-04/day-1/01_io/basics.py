# 1. Create a method that reads all contents of a file when its name given as param
def readfile(file_name):
    f = open(file_name)
    result = f.read()
    f.close()
    return result

# 2. Create a method that gets a file_name and a number as param and reads the numberth line of the file
def readline(file_name, number):
    f = open(file_name)
    i = 0
    while i != number:
        result = f.readline().rstrip()
        i += 1
    f.close()
    return result

# 3. Create a method that gets a long sentence as param and gives back the contained words in a list
def words(sentence):
    ls = []
    sentence = sentence[:-1]
    ls = sentence.split()
    return ls

# 4. Create a method that gets a list of words and creates a sentence with the words separated by spaces
def sentence(words):
    sentence = ''
    for i in words:
        sentence += i + ' '
    sentence = sentence[0:len(sentence)-1] + '.'
    return sentence

# 5. Create a method that gets a string and gives back the character codes in a list
def char_codes(string):
    ls = []
    for i in string:
        ls.append(ord(i))
    return ls

# 6. Create a method that gets a list of integers and gives back a string which characters are created from the numbers used as character codes
def string(char_codes):
    str = ''
    for i in char_codes:
        str += chr(i)
    return str    

def char_freq(message):
    freq = {}
    for i in message:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq

print(char_freq("I like cats"))
 # Returns {'a': 1, ' ': 2, 'c': 1, 'e': 1, 'I': 1, 'k': 1, 'l': 1, 'i': 1, 's': 1, 't': 1}

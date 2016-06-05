def alphabet_position(text):
    text = text.lower()
    text_numbers = []
    for i in text:
        if i.isalpha():
            text_numbers.append(str(ord(i)-96))
    text = ' '.join(text_numbers)
    return text

print(alphabet_position("The sunset sets at twelve o' clock."))

def countBits(n):
    number = bin(n)[2:]
    counter = 0
    for i in number:
        if i == '1':
            counter += 1
    return counter

print(countBits(10))

# write a function that takes a filename and returns the number of lines the
# file consists. It should return zero if the file not exists.

def line_counter(filename):
    try:
        f = open(filename)
        text = f.readlines()
        f.close()
        counter = 0
        for i in text:
            counter += 1
        return(counter)
    except:
        return(0)
print(line_counter(input('Enter filename: ')))

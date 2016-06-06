def getMiddle(s):
    half = len(s) // 2
    if len(s) % 2 != 0:
        return s[half]
    else:
        return(s[half-1] + s[half])

print (getMiddle("te"))

def count_sheeps(arrayOfSheeps=[]):
    counter = 0
    if len(arrayOfSheeps) < 1:
        return []
    for i in arrayOfSheeps:
        if i == True:
            counter += 1
    return 'There are %s sheeps in total, not %s' % (counter, len(arrayOfSheeps))

array1 = [True,  True,  True,  False,
          True,  True,  True,  True ,
          True,  False, True,  False,
          True,  False, False, True ,
          True,  True,  True,  True ,
          False, False, True,  True ]

print(count_sheeps(array1))

u = 123
# print 'Hooray!' if the number is bigger than 100
if u > 100:
    print ("Hooray!")

v = 426
# print 'Yeah!' if dividable by 4 but print 'End of program' after regardless
if v % 4 == 0:
    print ("Yeah!")
print ("End of program")

w = 24
out = 0
# if w is even increment out by one
if w % 2 == 0:
    out +=1
print (out)

x = 'monkey'
# if the string is longer than 4 characters
# print 'Long!' otherwise print 'Short!'
if len(x) > 4:
    print ("Long!")
else:
    print ("Short")

x = 'cheese'
# Tell if the x has even or odd number of
# characters with a True for even and
# false False output otherwise
if len(x) % 2 == 0:
    print (True)
else:
    print (False)

y = 'seasons'
out = 6
# if the last and the first letter of the string
# are the same double the variable
# called out, if not half it
if y[0] == y[-1]:
    out *= 2
else:
    out /= 2
print (out)

z = 13
# if z is between 10 and 20 print 'Sweet!'
# if less than 10 print 'More!',
# if more than 20 print 'Less!'
if 10 < z and 20 > z:
    print ("Sweet!")
elif z < 10:
    print ("More!")
else:
    print ("Less!")

aa = [1, 2, 3]
out = 0
# if the aa list contains one element set the out to 1
# if the aa list contains two element set the out to 2
# if the aa list contains more than 2 set the out to 10
# if the aa contains no elements it should set to -1
if len(aa) == 1:
    out = 1
elif len(aa) == 2:
    out = 2
elif len(aa) > 2:
    out = 10
else:
    out = -1
print (out)

ab = 123
credits = 100
is_bonus = False
# if credits are at least 50,
# and is_bonus is False decrement ab by 2
# if credits are smaller than 50,
# and is_bonus is False decrement ab by 1
# if is_bonus is True ab should remain the same
if credits >= 50 and is_bonus == False:
    ab -= 2
if credits < 50 and is_bonus == False:
    ab -= 1
print (ab)

ac = 8
time = 120
out = ''
# if ac is dividable by 4
# and time is not more than 200
# set out to 'check'
# if time is more than 200
# set out to 'Time out'
# otherwise set out to 'Run Forest Run!'
if ac % 4 == 0 and time <= 200:
    out = "check"
elif time > 200:
    out = "Time out"
else:
    out = "Run Forest Run"
print (out)

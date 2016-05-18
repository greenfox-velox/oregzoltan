ad = 6
# print the numbers till ad from 0
for a in range(ad+1):
    print (a)

ae = 4
text = 'Gold'
# print content of the text variable ae times
for a in range(ae):
    print (text)

af = [4, 5, 6, 7]
# print all the elements of af
for a in af:
    print (a)

ag = [3, 4, 5, 6, 7]
# please double all the elements of the list
for a in range(len(ag)):
    ag[a] *= 2
print (ag)

ah = ['kuty', 'macsk', 'cic']
# add to all elements an 'a' on the end
for a in range(len(ah)):
    ah[a] += "a"
print (ah)

ah = [3, 4, 5, 6, 7]
# print the sum of all numbers in ah
total = 0
for a in ah:
    total += ah
print(total)

# print the even numbers till 20
for a in range(1, 21):
    if a % 2 == 0:
        print(a)

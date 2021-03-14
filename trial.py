from itertools import zip_longest

a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]


a1 = a[:5]
a2 = a[5:10]
a3 = a[10:]

print(a1)
print(a2)
print(a3)


long = zip_longest(a1,["\t"], a2,["/t"], a3)
print(list(long))
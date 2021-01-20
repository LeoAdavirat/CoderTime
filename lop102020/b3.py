a = open('KTDB.INP', 'r')
A = a.read()
a.close()
from collections import Counter
aa = Counter(A)
aa = dict({(value,key) for (key, value) in aa.items()})
x = aa[1]
b = open('KTDB.OUT', 'w+')
b.write(str(A.index(x)+1))
b.close()
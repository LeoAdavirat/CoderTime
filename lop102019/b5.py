a = open('CLB.INP')
A = a.read().split()
a.close()
A.pop(0)
A = [int(i) for i in A]
from collections import Counter
A = Counter(A)
b = open('CLB.OUT','w+')
b.write(str((A.most_common(1))[0][1]))
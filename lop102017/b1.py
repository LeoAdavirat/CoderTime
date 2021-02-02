a = open('SOCP.INP')
A = a.read().split()
A.pop(0)
A = [int(i) for i in A]
B = set()
import math
for i in range(math.ceil(math.sqrt(max(A))) + 1):
	B.add(i^2)
b = open('SOCP.OUT','w+')
b.write(str(len(B.intersection(set(A)))))
b.close()
a = open('COVUA.INP')
A = a.read().split()
a.close()
A.pop(0)
A = [int(i) for i in A]
B = [A[i] for i in range(len(A)) if i % 2 != 0]
A = [A[i] for i in range(len(A)) if i % 2 == 0]
A.sort()
B.sort()
for i in A:
	if i > max(B):
		A.remove(i)
		B.remove(min(B))
sscore = 0
for i in range(len(A)):
	if B[i] > A[i]:
		sscore += 2
	else:
		sscore += 1
b = open('COVUA.OUT','w+')
b.write(str(sscore))
b.close()
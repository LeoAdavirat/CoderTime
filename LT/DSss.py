a = open('DSSS.IN')
A = a.read().split()
a.close()
A = [int(i) for i in A]
N = A.pop(0)
cnt = lambda k: (sum(A) - N * k)/2
K = []
for k in range(1, max(A) + 1):
	if int(cnt(k)) == cnt(k):
		K.append(k)
P = []
Q = []
for i in K:
	for j in A:
		if i + j in A:
			P.append(j)
			Q.append(i + j)
	if len(P) == len(Q) and len(P) == N:
		b = open('DSSS.OUT', 'w+')
		P = [str(i) for i in P]
		b.write(' '.join(P))
		break
		break
	else:
		P = []
		Q = []
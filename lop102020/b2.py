a = open('GVT.INP', 'r')
A = a.read().split()
a.close()
A = [int(i) for i in A]
d = A[0]*A[4] - A[1]*A[3]
dx = A[2]*A[4] - A[1]*A[5]
dy = A[0]*A[5] - A[3]*A[2]
b = open('GVT.OUT','w+')
if d != 0:
	b.write(str(dx/d) + ' ' + str(dy/d))
if d == 0:
	if dx == dy:
		b.write('ptvsn')
	elif dx != 0 or dy != 0:
		b.write('ptvn')
b.close()
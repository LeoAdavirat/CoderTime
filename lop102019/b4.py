a = open('DATHUC.INP')
A = a.read().split()
A = [int(i) for i in A]
n = A[0]
A.pop(0)
x = A[0]
A.pop(0)
A = [A[i] * x ** (n-i) for i in range(n + 1)]
b = open('DATHUC.OUT','w+')
b.write(str(sum(A)))
b.close()
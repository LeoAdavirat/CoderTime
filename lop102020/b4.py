a = open('PT.INP', 'r')
A = a.read().split()
a.close()
A = [int(i) for i in A]
m = A[0]
n = A[1]
A.pop(0)
A.pop(0)
A1 = [A[i] for i in range(m)]
A2 = [A[-(i+1)] for i in range(n)]
A1.sort()
A2.sort()
A1 = [A1[-(i+1)] for i in range(3)]
A2 = [A2[-(i+1)] for i in range(3)]
A3 = A1 + A2
A3.sort()
b = open('PT.OUT', 'w+')
b.write(str(sum(list([A3[-(i+1)] for i in range(4)]))))
b.close()
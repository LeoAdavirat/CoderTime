a.open('SODB.INP', 'r')
A = a.read().split()
A = [int(i) for i in A]
a.close()
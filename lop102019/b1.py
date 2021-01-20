a = open('TONGBP.INP', 'r')
A = [int(i) for i in str(a.read())]
a.close()
b = open('TONGBP.OUT','w+')
A = [i ** 2 for i in A]
b.write(str(sum(A)))
b.close()
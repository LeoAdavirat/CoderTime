a = open('DAYSO.INP')
A = a.read().split()
A.pop(0)
a.close()
A = [int(i) for i in A]
B = {i for i in range(min(A), max(A) + 1)}
b = open('DAYSO.OUT','w+')
ww = B.symmetric_difference(set(A))
ww = [str(i) for i in ww]
b.write(' '.join(ww) if ww != False else '0')
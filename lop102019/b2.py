a = open('LAPDAT.INP','r')
T = int(a.read())
a.close()
def Ktra(T):
	A = 400 + 50 * T
	B = 90 * T
	if A < B:
		return 'A' + '\n' + str(A)
	elif B < A:
		return 'B' + '\n' + str(B)
	elif A == B:
		return 'A' + '\n' + str(A)
b = open('LAPDAT.OUT', 'w+')
b.write(Ktra(T))
b.close()
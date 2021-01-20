def f(n):
	Uoc = [n]
	for i in range(n//2 + 1):
		try:
			if n % i == 0:
				Uoc.append(i)
		except ZeroDivisionError:
			pass
	return Uoc
n = int(input("Hay nhap so uoc:  "))
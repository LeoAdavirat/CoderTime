n = int(input("Please enter n:  "))
import functools
@functools.cache
def fibonacci(n):
	n -= 1
	if n == 0 or n == 1:
		return 1
	elif n <= -1:
		return 0
	elif n >= 2:
		return fibonacci(n) + fibonacci(n - 1)
print('fibonacci of '+ str(n) +' is:  ' + str(fibonacci(n)))
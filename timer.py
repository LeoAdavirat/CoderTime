n = int(input("Please enter time in seconds:  "))
print('Countdown Starts!!!')
def timer(n, k):
	print(k)
	if not k == n:
		timer(n, k + 1)
timer(n, 1)
print('Countdown is over!!!')
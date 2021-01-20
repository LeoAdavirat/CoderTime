s = open("SODEP.INP", "r")
n = s.read().split()
n.pop(0)
n = [int(i) for i in n]
x = n[0]
n.pop(0)
count = 0
for i in n:
	if i % x == 0:
		count += 1
a = open("SODEP.OUT","w+")
a.write(str(count))
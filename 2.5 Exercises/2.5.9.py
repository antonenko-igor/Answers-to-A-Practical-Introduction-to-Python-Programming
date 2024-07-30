x = eval(input("How many Fibonacci numbers? - "))
a = 0
b = 1
print(b, end = ",  ")
for i in range(x):
	c = a + b
	print(c, end =",  ")
	a = b
	b = c 
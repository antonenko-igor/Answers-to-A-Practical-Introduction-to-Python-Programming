num = eval(input("Enter a number:  "))
a = 1
d = 1
b = num
while d >= 0.00000000001:
	n =(a+(num/a))/2
	a = n
	d = b - n
	b = n
print("The square root of ",num,"is ",n) 
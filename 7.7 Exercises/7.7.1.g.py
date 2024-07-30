L = eval(input("Enter a list of integers: "))
c = 0
for i in L:
	if i < 5:
		c = c + 1
print("The number of integers less than 5 is ",c)		
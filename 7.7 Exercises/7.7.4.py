L = eval(input("Enter a list containing numbers between 1 and 12: "))

M = []
for i in L:
	if i > 10:
		i = 10
	M.append(i)
print(M) 
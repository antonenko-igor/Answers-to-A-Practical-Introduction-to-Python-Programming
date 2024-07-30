L = eval(input("Enter a list:  "))

M = []
for i in L:
	if i not in M:
		M.append(i)
print(M) 
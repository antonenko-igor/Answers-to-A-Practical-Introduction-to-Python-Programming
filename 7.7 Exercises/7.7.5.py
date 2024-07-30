L = eval(input("Enter a list of strings:  "))

M = []
for i in range(len(L)):
	M.append(L[i][1:])
print(M)    
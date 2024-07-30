L = eval(input("Enter a first list:   "))
M = eval(input("Enter a second list of the same length:  "))

N = []
for i in range(len(M)):
	N.append(L[i] + M[i])
print(N) 
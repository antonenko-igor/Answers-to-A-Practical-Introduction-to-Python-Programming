from random import randint

L = []
for i in range(5):
	M = []
	for j in range(5):
		M.append(randint(0,1))
	L.append(M)
i = eval(input("Enter a row:  "))
j = eval(input("Enter a column: "))
if L[i-1][j-1] == 1:
	print("Hit")
else:
	print("Miss")  
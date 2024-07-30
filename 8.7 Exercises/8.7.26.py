from random import randint
r = eval(input("Enter a number of rows:  "))
c = eval(input("Enter a number of columns: "))
print()
print("The random 2d array.")
L = []
for i in range(r):
	M = []
	for j in range(c):
		M.append(randint(0,9))
	L.append(M)
for i in range(len(L)):
	for j in range(len(L[i])):
		print(L[i][j], end = "  ")
	print()
print()
print()
print("The coordinates of the entity(row and column numbers)")
for i in range(len(L)):
	for j in range(len(L[i])):
		print("(",i,",",j,")", end = " ")
	print()
print()
print("The coordinates of entity(The number of the entity)")
a = 0
for i in range(len(L)):
	for j in range(len(L[i])):
		if a >9:
			print(a, end = "  ")
		else:
			print( " "+str(a) + " ", end = "  ")		
		a += 1
	print()
print()
x = eval(input("Enter a number of a entity: "))
print(L[x//c][x%c])
r, c = eval(input("The coordinates of the entity(separeted by comma): "))
print(L[r][c])		
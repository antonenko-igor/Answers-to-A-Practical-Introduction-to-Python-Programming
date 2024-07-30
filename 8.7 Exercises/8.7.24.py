from random import randint, choice
L = [[(randint(0,1)) for _ in range(5)] for _ in range(5)]
print("The starting list")
for row in L:
	print(row)
while True:
	for row in L:
		if 0  in row:
			True
	False
	zero = [(i,j) for i in range(5) for j in range(5) if L[i][j] == 0]
	if not zero:
		break
	random_zero = choice(zero)
	L[random_zero[0]][random_zero[1]] = 1		
print("The ending list")
for row in L:
	print(row) 
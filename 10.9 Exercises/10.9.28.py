"""
The partially filled magic square presented for example is not such, 
since in a magic square with numbers from 1 to 9, the sum of each row, 
each column and each diagonal is 15.
Below in the program is a partially filled magic square.
"""
from random import randint
L = [[2,0,0],
     [0,5,1],
     [4,3,0]]
while True:
	L[0][1] = randint(0,9)
	L[0][2] = randint(0,9)
	L[1][0] = randint(0,9)
	L[2][2] = randint(0,9)
	if sum(L[0]) == sum(L[1]) == sum(L[2]):		
		d1 = 0
		d2 = 0
		for i in range(3):
			d1 += L[i][i]
			d2 += L[i][2-i]
		if sum(L[0]) == d1 == d2:
			M = []
			for i in range(3):
				K = []
				for j in range(3):
					K.append(L[j][i])
				M.append(K)
			if sum(L[0]) == sum(M[0]) == sum(M[1]) == sum(M[2]):				
				for row in L:
					print(row)
				break 
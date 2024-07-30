from random import randint
M = []
print("The amount of simulated rolls - 1000 ")
for i in range(1000):
	L = []	 
	for i in range(4):
		r = randint(1,6)
		L.append(r)	
	M.append(L[0]+L[1])
	M.append(L[0]+L[2])
	M.append(L[0]+L[3])
	M.append(L[1]+L[2])
	M.append(L[1]+L[3])
	M.append(L[2]+L[3])
for k in range(2,13):
	print("The sum - ", k," the simulated rolls - ",M.count(k),
		  " -- {:.1f}".format((M.count(k)/1000)*100),"%")
	print()  
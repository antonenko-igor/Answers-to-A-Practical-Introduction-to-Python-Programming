from random import randint

L = []
for i in range(20):
	L.append(randint(1,100))
L.sort()
print(L)
print("The second largest value - ",L[-2])
print("The second lowest value - ",L[1])  
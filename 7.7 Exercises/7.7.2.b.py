from random import randint

L = []
for i in range(20):
	L.append(randint(1,100))

print("The average of the elements is  ",sum(L)/len(L))	
from random import randint

L = []
for i in range(20):
	L.append(randint(1,100))
print("The largest value - ",max(L))
print("The lowest value - ",min(L)) 
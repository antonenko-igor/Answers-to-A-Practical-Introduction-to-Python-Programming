from random import randint,shuffle
deck = [{'value':i, 'suit':c}
for c in ['spades', 'clubs', 'hearts', 'diamonds']
for i in range(2,15)]
shuffle(deck)
L = []
for i in range(3):
	L.append(deck[randint(0,51)]["value"])
L.sort()
if L[2] - L[1] == 1 and L[1] - L[0] == 1:
	print("The straight", L[0],L[1],L[2])
else:
	print("No") 
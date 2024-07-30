from random import randint,shuffle
deck = [{'value':i, 'suit':c}
for c in ['spades', 'clubs', 'hearts', 'diamonds']
for i in range(2,15)]
shuffle(deck)
L = []
for i in range(3):
	L.append(deck[randint(0,51)]["value"])
if L.count(L[0]) == 2 or L.count(L[2]) == 2:
	print("The pair ")
else:
	print("No") 
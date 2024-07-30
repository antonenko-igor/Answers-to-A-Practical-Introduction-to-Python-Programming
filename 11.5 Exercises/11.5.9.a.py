from random import randint,shuffle
deck = [{'value':i, 'suit':c}
for c in [['spades', 'clubs', 'hearts', 'diamonds']
for i in range(2,15)]
shuffle(deck)
L = []
for i in range(3):
	L.append(deck[randint(0,51)]["suit"])
if L[0] == L[1] == L[2]:
	print("The flush - ",L[0])
else:
	print("No flush") 
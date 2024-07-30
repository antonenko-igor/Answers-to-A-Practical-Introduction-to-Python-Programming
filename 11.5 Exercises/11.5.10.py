from random import randint,shuffle
deck = [{'value':i, 'suit':c}
for c in ['spades', 'clubs', 'hearts', 'diamonds']
for i in range(2,15)]
shuffle(deck)
count = 0
for _ in range(100000):
	L = []
	for i in range(5):
		L.append(deck[randint(0,51)]["suit"])
		if L.count(L[0]) == 5:
			count += 1
print("The probability of being dealt a flush in a five card",(count/100000)*100, "%") 
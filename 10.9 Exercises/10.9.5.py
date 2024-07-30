suits =  ['Hearts', 'Diamonds', 'Clubs', 'Spades']
values =  ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
          'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
L = []
for i in range(len(values)):
	for j in range(len(suits)):
		x = "{}  {}".format(values[i],suits[j])
		L.append((x + " "))		
print(L) 
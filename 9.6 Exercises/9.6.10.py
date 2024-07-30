from random import choice
L = ["word","letter","program","different","seven","value",
    "right","root","list","guess"]
c = 0

while c != 1:
	word = choice(L)	
	for i in range(len(word)):
		c = word.count(word[i])
		if c == 2:
			break					
print(word)	
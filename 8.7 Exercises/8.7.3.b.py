string = input("Enter a sentence:  ")

L = string.split()
c = 2
for i in range(len(L)):
	if c < len(L):
		print(L[c])
		c = c + 3 
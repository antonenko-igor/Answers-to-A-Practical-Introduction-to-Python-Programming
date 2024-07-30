s = "abcdefghijklmnopqrstuvwxyz"
L = list(s)
word = input("Enter a word - ")
M = list(word)
S = []

for i in range(len(L)):
	for j in range(len(M)):
		if L[i] == M[j]:
			S.append(L[i])
print(" ".join(S)) 
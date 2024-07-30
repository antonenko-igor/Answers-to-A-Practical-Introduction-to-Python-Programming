from random import choice,shuffle

names = input("Enter the names separeted by commas:  ")
entries = eval(input("Enter the entries each person separeted by commas:  "))
L = names.split(",")
X = list(entries)
M = []
for i in range(len(X)):
	for _ in range(X[i]):
		M.append(L[i])	
	shuffle(M)
print("The lottery wins ",choice(M))  
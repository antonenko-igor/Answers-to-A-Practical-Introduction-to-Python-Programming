string = input("Enter a string - ")
string = string.lower()

for c in ", . ":
	string = string.replace(c," ")
print(string)  
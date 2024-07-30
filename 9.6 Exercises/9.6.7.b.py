string = input("Enter a string:  ")
letter = input("Enter a letter:  ")
string = string.lower()
letter = letter.lower()
for i in string:	
	if i == letter:
		print("The index is",string.index(letter))
		break
else:
	print("The string does not contain the letter",letter)
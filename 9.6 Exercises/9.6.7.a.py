string = input("Enter a string:  ")
letter = input("Enter a letter:  ")
i = 2
string = string.lower()
letter = letter.lower()

while i!= 0:
	if letter in string:
		print("The index is ",string.index(letter))
		i = 1
		break		
	i = 0
if i == 0:
	print("The string does not contain the letter",letter)